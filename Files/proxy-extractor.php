<?php

// --- Configuration ---
$inputJsonFile = 'Files/usernames.json';
$outputJsonFile = 'Files/extracted_proxies.json';
$outputProxyFile = 'proxy.txt'; // برای ادغام با پایتون
$outputOfflineFile = 'Files/offline_proxies.txt'; // برای پروکسی‌های آفلاین
$telegramBaseUrl = 'https://t.me/s/';
$proxyCheckTimeout = 5; // افزایش timeout برای تست پروکسی
$historyLength = 24;

// --- User-Agentهای متنوع برای دور زدن CAPTCHA ---
$userAgents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
];

// --- Script Logic ---
ob_start();
date_default_timezone_set('Asia/Tehran');
echo "--- Telegram Proxy Extractor v4.5 (Debug Enhanced) ---\n";

// --- Phase 0: Read Previous Run's Data ---
$indexedOldProxies = [];
if (file_exists($outputJsonFile)) {
    echo "Reading previous proxy data from '$outputJsonFile'...\n";
    $oldJsonContent = file_get_contents($outputJsonFile);
    $oldProxiesData = json_decode($oldJsonContent, true);
    if (is_array($oldProxiesData)) {
        foreach ($oldProxiesData as $proxy) {
            if (isset($proxy['tg_url'])) {
                $indexedOldProxies[$proxy['tg_url']] = $proxy;
            }
        }
        echo "Loaded history for " . count($indexedOldProxies) . " previous proxies.\n";
    } else {
        echo "No previous proxy data found or invalid JSON in '$outputJsonFile'.\n";
    }
} else {
    echo "No previous proxy data file found at '$outputJsonFile'.\n";
}

// --- Phase 1: Read Input ---
$usernames = [];
if (file_exists($inputJsonFile)) {
    $jsonContent = file_get_contents($inputJsonFile);
    if ($jsonContent !== false) {
        $usernames = json_decode($jsonContent, true);
        if ($usernames === null) {
            echo "Error: Could not decode JSON. Details: " . json_last_error_msg() . "\n";
            $usernames = [];
        } else {
            echo "Read " . count($usernames) . " usernames from '$inputJsonFile': " . implode(", ", $usernames) . "\n";
        }
    } else {
        echo "Error: Could not read input JSON file '$inputJsonFile'\n";
        $usernames = [];
    }
} else {
    echo "Error: Input JSON file not found at '$inputJsonFile'. Using empty username list.\n";
}

// --- Phase 2: Parallel Fetching of Channel Content ---
$multiHandle = curl_multi_init();
$urlHandles = [];
foreach ($usernames as $username) {
    if (!is_string($username) || empty(trim($username))) {
        echo "Skipping invalid username: '$username'\n";
        continue;
    }
    $channelUrl = $telegramBaseUrl . urlencode(trim($username));

    $ch = curl_init($channelUrl);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_TIMEOUT => 60, // افزایش timeout
        CURLOPT_USERAGENT => $userAgents[array_rand($userAgents)], // user-agent تصادفی
        CURLOPT_VERBOSE => true, // لاگ‌های دقیق‌تر
        CURLOPT_STDERR => fopen('php://stderr', 'w'), // لاگ‌های curl به stderr
        CURLOPT_SSL_VERIFYPEER => false, // برای دور زدن مشکلات SSL
        CURLOPT_SSL_VERIFYHOST => false, // برای دور زدن مشکلات SSL
    ]);
    curl_multi_add_handle($multiHandle, $ch);
    $urlHandles[$channelUrl] = $ch;
    echo "Added channel for fetching: $channelUrl\n";
}

$running = null;
do {
    curl_multi_exec($multiHandle, $running);
    curl_multi_select($multiHandle);
} while ($running > 0);

// --- Phase 3: Process Results and Extract Proxies ---
$allExtractedProxies = [];
$proxyRegex = '/(?:https?:\/\/t\.me\/proxy\?|tg:\/\/proxy\?)[^"\'\s]+/i';

foreach ($urlHandles as $url => $ch) {
    $htmlContent = curl_multi_getcontent($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    $effectiveUrl = curl_getinfo($ch, CURLINFO_EFFECTIVE_URL);
    echo "Processing channel: $url, HTTP Code: $httpCode, Effective URL: $effectiveUrl, Response Length: " . strlen($htmlContent) . "\n";

    if ($httpCode == 200 && $htmlContent) {
        if (stripos($htmlContent, 'CAPTCHA') !== false || stripos($htmlContent, 'recaptcha') !== false) {
            echo "CAPTCHA detected on $url, skipping\n";
            continue;
        }
        if (preg_match_all($proxyRegex, $htmlContent, $matches)) {
            echo "Found " . count($matches[0]) . " potential proxies in $url\n";
            foreach ($matches[0] as $foundUrl) {
                $parsedUrl = parse_url($foundUrl);
                if (!$parsedUrl || !isset($parsedUrl['query'])) {
                    echo "Invalid proxy URL: $foundUrl\n";
                    continue;
                }

                $decodedQueryString = html_entity_decode($parsedUrl['query'], ENT_QUOTES | ENT_HTML5);
                parse_str($decodedQueryString, $query);

                if (isset($query['server'], $query['port'], $query['secret'])) {
                    $allExtractedProxies[] = [
                        'server' => trim($query['server']),
                        'port' => (int)trim($query['port']),
                        'secret' => trim($query['secret'])
                    ];
                    echo "Extracted proxy: server={$query['server']}, port={$query['port']}, secret={$query['secret']}\n";
                } else {
                    echo "Invalid proxy parameters in: $foundUrl\n";
                }
            }
        } else {
            echo "No proxies found in $url. Response snippet: " . substr($htmlContent, 0, 200) . "...\n";
        }
    } else {
        echo "Failed to fetch $url, HTTP Code: $httpCode, Response Length: " . strlen($htmlContent) . "\n";
    }
    curl_multi_remove_handle($multiHandle, $ch);
}
curl_multi_close($multiHandle);

// --- Phase 4: De-duplicate, Check Proxy Status, and Update History ---
echo "Fetch complete. Found " . count($allExtractedProxies) . " potential proxies. De-duplicating and checking status...\n";

function checkProxyStatus(string $server, int $port, int $timeout): array {
    $startTime = microtime(true);
    $socket = @fsockopen("tcp://$server", $port, $errno, $errstr, $timeout);

    if ($socket) {
        $latency = round((microtime(true) - $startTime) * 1000);
        fclose($socket);
        echo "Proxy $server:$port is Online (Latency: {$latency}ms)\n";
        return ['status' => 'Online', 'latency' => $latency];
    }
    echo "Proxy $server:$port is Offline (Error: $errstr, Code: $errno)\n";
    return ['status' => 'Offline', 'latency' => null];
}

$uniqueProxies = [];
$offlineProxies = [];
foreach ($allExtractedProxies as $proxy) {
    $tgUrl = "tg://proxy?server={$proxy['server']}&port={$proxy['port']}&secret={$proxy['secret']}";
    if (!isset($uniqueProxies[$tgUrl]) && !isset($offlineProxies[$tgUrl])) {
        $statusResult = checkProxyStatus($proxy['server'], $proxy['port'], $proxyCheckTimeout);

        // History Logic
        $history = $indexedOldProxies[$tgUrl]['history'] ?? [];
        $newStatusBit = ($statusResult['status'] === 'Online') ? 1 : 0;
        $history[] = $newStatusBit;
        if (count($history) > $historyLength) {
            $history = array_slice($history, -$historyLength);
        }

        $proxyData = array_merge($proxy, $statusResult, ['tg_url' => $tgUrl, 'history' => $history]);
        if ($statusResult['status'] === 'Online') {
            $uniqueProxies[$tgUrl] = $proxyData;
        } else {
            $offlineProxies[$tgUrl] = $proxyData;
        }
        echo " - Checked {$proxy['server']}:{$proxy['port']} -> {$statusResult['status']}" . ($statusResult['latency'] ? " ({$statusResult['latency']}ms)" : "") . " | History: " . count($history) . "/$historyLength\n";
    }
}

$proxiesWithStatus = array_values($uniqueProxies);
$proxyCount = count($proxiesWithStatus);
$offlineProxyCount = count($offlineProxies);
echo "\nFinished checks. Total unique proxies found: $proxyCount (Online), $offlineProxyCount (Offline)\n";

// --- Phase 5: Sort Proxies (Best First) ---
usort($proxiesWithStatus, function ($a, $b) {
    if ($a['status'] === 'Online' && $b['status'] === 'Offline') return -1;
    if ($a['status'] === 'Offline' && $b['status'] === 'Online') return 1;
    if ($a['status'] === 'Online' && $b['status'] === 'Online') {
        return $a['latency'] <=> $b['latency'];
    }
    return 0;
});

// --- Phase 6: Generate Outputs ---
$jsonOutputContent = json_encode($proxiesWithStatus, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);
if (file_put_contents($outputJsonFile, $jsonOutputContent)) {
    echo "Successfully wrote $proxyCount unique proxies to '$outputJsonFile'\n";
} else {
    echo "Failed to write to '$outputJsonFile'\n";
}

// --- Phase 7: Save Offline Proxies ---
$offlineProxyContent = "";
foreach ($offlineProxies as $proxy) {
    $offlineProxyContent .= $proxy['tg_url'] . "\n";
}
if (file_put_contents($outputOfflineFile, $offlineProxyContent)) {
    echo "Successfully wrote $offlineProxyCount offline proxies to '$outputOfflineFile'\n";
} else {
    echo "Failed to write to '$outputOfflineFile'\n";
}

// --- Phase 8: Merge and Generate proxy.txt ---
$existingProxies = [];
if (file_exists($outputProxyFile)) {
    $existingProxies = file($outputProxyFile, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    echo "Read " . count($existingProxies) . " existing proxies from '$outputProxyFile'\n";
} else {
    echo "No existing proxies found in '$outputProxyFile'\n";
}
$proxyTxtContent = "";
$newProxies = array_column($proxiesWithStatus, 'tg_url');
$allProxies = array_unique(array_merge($existingProxies, $newProxies));
if (empty($allProxies)) {
    echo "No online proxies found, creating empty '$outputProxyFile'\n";
    file_put_contents($outputProxyFile, "");
} else {
    foreach ($allProxies as $proxy) {
        $proxyTxtContent .= "$proxy\n";
    }
    if (file_put_contents($outputProxyFile, $proxyTxtContent)) {
        echo "Successfully wrote " . count($allProxies) . " proxies to '$outputProxyFile'\n";
    } else {
        echo "Failed to write to '$outputProxyFile'\n";
    }
}

$consoleOutput = ob_get_clean();
echo $consoleOutput;
echo "--- Script Finished ---\n";

// همیشه با کد خروج 0 خارج شو
exit(0);
?>
