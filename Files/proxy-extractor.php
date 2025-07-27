<?php

$inputJsonFile = 'Files/usernames.json';
$outputJsonFile = 'Files/extracted_proxies.json';
$outputProxyFile = 'proxy.txt'; 
$telegramBaseUrl = 'https://t.me/s/';
$proxyCheckTimeout = 2; 
$historyLength = 24; 

ob_start();
date_default_timezone_set('Asia/Tehran');
echo "--- Telegram Proxy Extractor v4.0 (Simplified Output) ---\n";

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
    }
}

if (!file_exists($inputJsonFile)) die("Error: Input JSON file not found at '$inputJsonFile'\n");
$jsonContent = file_get_contents($inputJsonFile);
if ($jsonContent === false) die("Error: Could not read input JSON file '$inputJsonFile'\n");
$usernames = json_decode($jsonContent, true);
if ($usernames === null) die("Error: Could not decode JSON. Details: " . json_last_error_msg() . "\n");

echo "Read " . count($usernames) . " usernames. Starting parallel fetch...\n";

$multiHandle = curl_multi_init();
$urlHandles = [];
foreach ($usernames as $username) {
    if (!is_string($username) || empty(trim($username))) continue;
    $channelUrl = $telegramBaseUrl . urlencode(trim($username));

    $ch = curl_init($channelUrl);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_TIMEOUT => 30,
        CURLOPT_USERAGENT => 'Mozilla/5.0 (compatible; PHP-Proxy-Extractor/4.0)'
    ]);
    curl_multi_add_handle($multiHandle, $ch);
    $urlHandles[$channelUrl] = $ch;
}

$running = null;
do {
    curl_multi_exec($multiHandle, $running);
    curl_multi_select($multiHandle);
} while ($running > 0);

$allExtractedProxies = [];
$proxyRegex = '/(?:https?:\/\/t\.me\/proxy\?|tg:\/\/proxy\?)[^"\'\s]+/i';

foreach ($urlHandles as $url => $ch) {
    $htmlContent = curl_multi_getcontent($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

    if ($httpCode == 200 && $htmlContent) {
        if (preg_match_all($proxyRegex, $htmlContent, $matches)) {
            foreach ($matches[0] as $foundUrl) {
                $parsedUrl = parse_url($foundUrl);
                if (!$parsedUrl || !isset($parsedUrl['query'])) continue;

                $decodedQueryString = html_entity_decode($parsedUrl['query'], ENT_QUOTES | ENT_HTML5);
                parse_str($decodedQueryString, $query);

                if (isset($query['server'], $query['port'], $query['secret'])) {
                    $allExtractedProxies[] = [
                        'server' => trim($query['server']),
                        'port' => (int)trim($query['port']),
                        'secret' => trim($query['secret'])
                    ];
                }
            }
        }
    }
    curl_multi_remove_handle($multiHandle, $ch);
}
curl_multi_close($multiHandle);

echo "Fetch complete. Found " . count($allExtractedProxies) . " potential proxies. De-duplicating and checking status...\n";

function checkProxyStatus(string $server, int $port, int $timeout): array {
    $startTime = microtime(true);
    $socket = @fsockopen("tcp://$server", $port, $errno, $errstr, $timeout);

    if ($socket) {
        $latency = round((microtime(true) - $startTime) * 1000);
        fclose($socket);
        return ['status' => 'Online', 'latency' => $latency];
    }
    return ['status' => 'Offline', 'latency' => null];
}

$uniqueProxies = [];
foreach ($allExtractedProxies as $proxy) {
    $tgUrl = "tg://proxy?server={$proxy['server']}&port={$proxy['port']}&secret={$proxy['secret']}";
    if (!isset($uniqueProxies[$tgUrl])) {
        $statusResult = checkProxyStatus($proxy['server'], $proxy['port'], $proxyCheckTimeout);

        $history = $indexedOldProxies[$tgUrl]['history'] ?? [];
        $newStatusBit = ($statusResult['status'] === 'Online') ? 1 : 0;
        $history[] = $newStatusBit;
        if (count($history) > $historyLength) {
            $history = array_slice($history, -$historyLength);
        }

        $uniqueProxies[$tgUrl] = array_merge($proxy, $statusResult, ['tg_url' => $tgUrl, 'history' => $history]);
        echo " - Checked {$proxy['server']}:{$proxy['port']} -> {$statusResult['status']}" . ($statusResult['latency'] ? " ({$statusResult['latency']}ms)" : "") . " | History: " . count($history) . "/$historyLength\n";
    }
}

$proxiesWithStatus = array_values($uniqueProxies);
$proxyCount = count($proxiesWithStatus);

usort($proxiesWithStatus, function ($a, $b) {
    if ($a['status'] === 'Online' && $b['status'] === 'Offline') return -1;
    if ($a['status'] === 'Offline' && $b['status'] === 'Online') return 1;
    if ($a['status'] === 'Online' && $b['status'] === 'Online') {
        return $a['latency'] <=> $b['latency'];
    }
    return 0;
});

echo "\nFinished checks. Total unique proxies found: $proxyCount\n";

$jsonOutputContent = json_encode($proxiesWithStatus, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);
if (file_put_contents($outputJsonFile, $jsonOutputContent)) {
    echo "Successfully wrote $proxyCount unique proxies to '$outputJsonFile'\n";
}

$existingProxies = [];
if (file_exists($outputProxyFile)) {
    $existingProxies = file($outputProxyFile, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
}
$proxyTxtContent = "";
$newProxies = array_column($proxiesWithStatus, 'tg_url');
$allProxies = array_unique(array_merge($existingProxies, $newProxies));
foreach ($allProxies as $proxy) {
    $proxyTxtContent .= "$proxy\n";
}
if (file_put_contents($outputProxyFile, $proxyTxtContent)) {
    echo "Successfully wrote " . count($allProxies) . " proxies to '$outputProxyFile'\n";
}

$consoleOutput = ob_get_clean();
echo $consoleOutput;
echo "--- Script Finished ---\n";
?>
