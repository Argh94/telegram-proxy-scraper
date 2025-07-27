import requests
from bs4 import BeautifulSoup
import re
import random
import time
import logging
from datetime import datetime
import pytz
import jdatetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import unicodedata
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
]
HISTORY_LENGTH = 24  

def get_random_user_agent():
    return random.choice(USER_AGENTS)

def clean_line(line):
    line = line.strip().replace('\r', '').replace('\n', '')
    line = ''.join(c for c in line if unicodedata.category(c)[0] != 'C')
    return line

def check_proxy_status(server, port, timeout=3):
    """Check if a proxy server is online by attempting a connection."""
    start_time = time.time()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((server, int(port)))
        sock.close()
        if result == 0:
            latency = round((time.time() - start_time) * 1000)  # به میلی‌ثانیه
            logging.info(f"Proxy {server}:{port} is online ({latency}ms)")
            return {'status': 'Online', 'latency': latency}
        else:
            logging.warning(f"Proxy {server}:{port} is offline or unreachable")
            return {'status': 'Offline', 'latency': None}
    except (socket.timeout, socket.gaierror, ConnectionRefusedError, socket.error) as e:
        logging.error(f"Error checking proxy {server}:{port}: {e}")
        return {'status': 'Offline', 'latency': None}

def load_existing_proxies_history(filename='Files/extracted_proxies.json'):
    """خواندن تاریخچه پروکسی‌ها از فایل JSON"""
    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return {proxy['tg_url']: proxy for proxy in data}
        except Exception as e:
            logging.error(f"Error reading {filename}: {e}")
    return {}

def fetch_proxies_from_text_urls(urls):
    all_proxies = []
    headers = {'User-Agent': get_random_user_agent()}
    pattern = r'^(tg://proxy|https://t\.me/proxy)\?server=[^&]+&port=\d+(&secret=.+)$'
    
    for url in urls:
        try:
            logging.info(f"Fetching proxies from {url}")
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            lines = response.text.splitlines()
            proxy_checks = []
            
            for line in lines:
                line = clean_line(line)
                if not line:
                    continue
                if re.match(pattern, line):
                    match = re.match(r'^(?:tg://proxy|https://t\.me/proxy)\?server=([^&]+)&port=(\d+)&secret=([0-9a-fA-F]+.*)$', line)
                    if match:
                        server, port, secret = match.groups()
                        proxy_checks.append({
                            'tg_url': line,
                            'server': server,
                            'port': int(port),
                            'secret': secret
                        })
                    else:
                        logging.debug(f"Invalid or skipped proxy: {line} (does not match pattern)")
                else:
                    logging.debug(f"Invalid or skipped proxy: {line} (does not match pattern)")
            
            with ThreadPoolExecutor(max_workers=30) as executor:
                future_to_proxy = {executor.submit(check_proxy_status, proxy['server'], proxy['port']): proxy for proxy in proxy_checks}
                for future in as_completed(future_to_proxy):
                    proxy = future_to_proxy[future]
                    try:
                        status_result = future.result()
                        proxy['status'] = status_result['status']
                        proxy['latency'] = status_result['latency']
                        if status_result['status'] == 'Online':
                            all_proxies.append(proxy)
                    except Exception as e:
                        logging.error(f"Error checking proxy {proxy['tg_url']}: {e}")
                        proxy['status'] = 'Offline'
                        proxy['latency'] = None
            
            logging.info(f"Fetched {len(lines)} lines, {len(all_proxies)} valid and online MTProto proxies from {url}")
        except requests.RequestException as e:
            logging.error(f"HTTP error fetching {url}: {e}")
        time.sleep(random.uniform(0.5, 1.0))
    return all_proxies

def fetch_proxies_from_telegram_channel(url):
    proxies = []
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f'user-agent={get_random_user_agent()}')
    
    try:
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        logging.info(f"Opened {url}")
        
        last_height = driver.execute_script("return document.body.scrollHeight")
        for i in range(5):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = driver.execute_script("return document.body.scrollHeight")
            logging.info(f"Scrolled {url}, attempt {i+1}, new height: {new_height}")
            if new_height == last_height:
                logging.info(f"No more content to load for {url}")
                break
            last_height = new_height
        
        page_source = driver.page_source
        if "CAPTCHA" in page_source or "recaptcha" in page_source.lower():
            logging.warning(f"CAPTCHA detected on {url}")
        
        soup = BeautifulSoup(page_source, 'html.parser')
        pattern = r'^(tg://proxy|https://t\.me/proxy)\?server=[^&]+&port=\d+(&secret=.+)$'
        proxy_elements = soup.find_all('a', href=re.compile(pattern))
        
        proxy_checks = []
        for element in proxy_elements:
            proxy_url = element.get('href')
            match = re.match(r'^(?:tg://proxy|https://t\.me/proxy)\?server=([^&]+)&port=(\d+)&secret=([0-9a-fA-F]+.*)$', proxy_url)
            if match:
                server, port, secret = match.groups()
                proxy_checks.append({
                    'tg_url': proxy_url,
                    'server': server,
                    'port': int(port),
                    'secret': secret
                })
        
        with ThreadPoolExecutor(max_workers=30) as executor:
            future_to_proxy = {executor.submit(check_proxy_status, proxy['server'], proxy['port']): proxy for proxy in proxy_checks}
            for future in as_completed(future_to_proxy):
                proxy = future_to_proxy[future]
                try:
                    status_result = future.result()
                    proxy['status'] = status_result['status']
                    proxy['latency'] = status_result['latency']
                    if status_result['status'] == 'Online':
                        proxies.append(proxy)
                except Exception as e:
                    logging.error(f"Error checking proxy {proxy['tg_url']}: {e}")
                    proxy['status'] = 'Offline'
                    proxy['latency'] = None
        
        logging.info(f"Fetched {len(proxies)} valid and online MTProto proxies from {url}")
    except WebDriverException as e:
        logging.error(f"WebDriver error fetching {url}: {e}")
    except Exception as e:
        logging.error(f"General error fetching {url}: {e}")
    finally:
        try:
            driver.quit()
        except:
            pass
    time.sleep(random.uniform(0.5, 1.0))
    return proxies

def save_proxies_to_file(proxy_list, filename='../proxy.txt'):
    try:
        existing_proxies_history = load_existing_proxies_history()
        
        for proxy in proxy_list:
            history = existing_proxies_history.get(proxy['tg_url'], {}).get('history', [])
            new_status_bit = 1 if proxy['status'] == 'Online' else 0
            history.append(new_status_bit)
            if len(history) > HISTORY_LENGTH:
                history = history[-HISTORY_LENGTH:]
            proxy['history'] = history
    
        with open('Files/extracted_proxies.json', 'w', encoding='utf-8') as file:
            json.dump(proxy_list, file, ensure_ascii=False, indent=4)
        logging.info(f"Saved {len(proxy_list)} proxies with history to Files/extracted_proxies.json")
        
        existing_proxies = []
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                existing_proxies = [line.strip() for line in file if line.strip()]
        
        unique_proxies = list(set(existing_proxies + [proxy['tg_url'] for proxy in proxy_list if proxy['status'] == 'Online']))

        with open(filename, 'w', encoding='utf-8') as file:
            for proxy in unique_proxies:
                file.write(proxy + '\n')
        logging.info(f"Saved {len(unique_proxies)} unique online proxies to {filename}")
        return proxy_list
    except IOError as e:
        logging.error(f"Error writing to {filename}: {e}")
        return []

def update_readme(proxy_list):
    try:
        utc_now = datetime.now(pytz.UTC)
        iran_tz = pytz.timezone('Asia/Tehran')
        iran_now = utc_now.astimezone(iran_tz)
        
        jalali_date = jdatetime.datetime.fromgregorian(datetime=iran_now)
        update_time_iran = jalali_date.strftime('%H:%M %d-%m-%Y')
        logging.info(f"Updating README with Iranian timestamp: {update_time_iran}")

        sample_proxies = random.sample(proxy_list, min(20, len(proxy_list))) if proxy_list else []
        table_rows = ""
        valid_proxies = 0
        for i, proxy in enumerate(sample_proxies, 1):
            proxy_url = proxy['tg_url'].replace('tg://proxy', 'https://t.me/proxy')
            status = proxy['status']
            latency = f"{proxy['latency']}ms" if proxy['latency'] else '-'
            match = re.match(r'^(?:tg://proxy|https://t\.me/proxy)\?server=([^&]+)&port=(\d+)&secret=([0-9a-fA-F]+.*)$', proxy['tg_url'])
            if match:
                server, port, secret = match.groups()
                display_proxy = f"https://t.me/proxy?server={server}&port={port}&secret={secret}"
                table_rows += f"| {i} | `{server}` | `{port}` | {status} ({latency}) | [لینک پروکسی]({display_proxy}) |\n"
                valid_proxies += 1
                logging.info(f"Valid proxy added to table: {proxy_url} ({status}, {latency})")
            else:
                logging.warning(f"Invalid proxy format, skipped: {proxy['tg_url']}")
        
        logging.info(f"Added {valid_proxies} valid proxies to the table (out of {len(sample_proxies)} sampled)")

        readme_content = f"""# 📊 نتایج استخراج: (آخرین بروزرسانی: {update_time_iran})

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License" />
  <img src="https://img.shields.io/badge/python-3.9-blue" alt="Python 3.9" />
  <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions Welcome" />
  <img src="https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg" alt="Proxy Scraper Workflow" />
  <img src="https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper" alt="GitHub Last Commit" />
  <img src="https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper" alt="GitHub Issues" />
</p>

این پروژه یک اسکریپت پایتون برای جمع‌آوری خودکار پروکسی‌های MTProto تلگرام از منابع متنی و کانال‌های تلگرام است. پروکسی‌ها در فایل `proxy.txt` ذخیره می‌شوند و هر 3 ساعت به‌صورت خودکار به‌روزرسانی می‌شوند.

## ✨ درباره پروژه

این اسکریپت با استفاده از `requests` برای منابع متنی و `selenium` برای کانال‌های تلگرام، پروکسی‌های MTProto را جمع‌آوری می‌کند. فقط پروکسی‌های آنلاین ذخیره شده و پروکسی‌های تکراری حذف می‌شوند. این فرآیند به‌صورت خودکار با **GitHub Actions** هر 3 ساعت اجرا می‌شود.

## 🚀 ویژگی‌ها
- 🌐 جمع‌آوری پروکسی از منابع متنی و کانال‌های تلگرام
- ✅ بررسی وضعیت پروکسی‌ها (آنلاین/آفلاین)
- 🔄 به‌روزرسانی خودکار هر 3 ساعت
- 🗑 حذف پروکسی‌های تکراری
- 🔑 بدون نیاز به API تلگرام
- 📱 مناسب برای کاربران در جستجوی پروکسی‌های فعال MTProto

## 📋 پیش‌نیازها
- 🐍 پایتون 3.9
- 📦 کتابخانه‌های مورد نیاز: `requests`, `beautifulsoup4`, `selenium`, `pytz`, `jdatetime`
- نصب وابستگی‌ها با: `pip install -r requirements.txt`

## 🛠 نحوه استفاده
1. فایل `proxy.txt` را از [اینجا](proxy.txt) دانلود کنید.
2. لینک‌های پروکسی (با فرمت `tg://proxy?...` یا `https://t.me/proxy?...`) را در کلاینت تلگرام وارد کنید.
3. در جدول زیر، روی لینک‌های ستون **لینک پروکسی** کلیک کنید تا به تلگرام هدایت شوید یا لینک را کپی کنید.
4. برای به‌روزرسانی دستی، به تب **Actions** در مخزن بروید و روی **Run workflow** کلیک کنید.

## 🌍 منابع پروکسی
- **منابع متنی**:
  - [MahsaNetConfigTopic](https://raw.githubusercontent.com/MahsaNetConfigTopic/proxy/main/proxies.txt)
  - [MhdiTaheri/ProxyCollector](https://raw.githubusercontent.com/MhdiTaheri/ProxyCollector/main/proxy.txt)
  - [SoliSpirit/mtproto](https://raw.githubusercontent.com/SoliSpirit/mtproto/master/all_proxies.txt)
- **کانال‌های تلگرام**:
  - iporoto, HiProxy, iproxy, iRoProxy, proxyforopeta, IRN_Proxy, MProxy_ir, ProxyHagh, PyroProxy, ProxyMTProto, MTPro_XYZ, vpns, mtmvpn, asr_proxy, proxyskyy

## 📈 نمونه پروکسی‌ها
جدول زیر نمونه‌ای از 20 پروکسی فعال از فایل `proxy.txt` را نمایش می‌دهد. برای استفاده، روی لینک پروکسی کلیک کنید یا آن را کپی کنید:

| # | سرور (Server) | پورت (Port) | وضعیت | لینک پروکسی |
|---|---------------|-------------|-------|-------------|
{table_rows}

> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.

## 🤝 مشارکت
از ایده‌ها و مشارکت شما استقبال می‌کنیم! برای بهبود پروژه:
1. یک **Issue** در مخزن باز کنید.
2. یا یک **Pull Request** با تغییرات پیشنهادی ارسال کنید.

## 📜 لایسنس
این پروژه تحت [لایسنس MIT](https://github.com/Argh94/telegram-proxy-scraper/blob/main/Files/LISENSE) منتشر شده است.

## 🔗 لینک‌های مفید
- 📄 [لیست پروکسی‌ها](proxy.txt)
- 🚀 [وضعیت GitHub Actions](https://github.com/Argh94/telegram-proxy-scraper/actions)
- ⭐ [ما را ستاره دهید!](https://github.com/Argh94/telegram-proxy-scraper)

## 📊 Stargazers در گذر زمان
<p align="center">
  <img src="https://starchart.cc/Argh94/telegram-proxy-scraper.svg?variant=adaptive" alt="Stargazers over time" />
</p>

---

🌟 **سپاس از استفاده از Telegram Proxy Scraper!** اگر سؤالی دارید، در بخش Issues مطرح کنید.
"""

        with open('../README.md', 'w', encoding='utf-8') as file:
            file.write(readme_content)
        logging.info("Successfully updated README.md with new styling and Iranian date format")
    except Exception as e:
        logging.error(f"Error updating README.md: {e}")

if __name__ == "__main__":
    text_urls = [
        "https://raw.githubusercontent.com/MahsaNetConfigTopic/proxy/main/proxies.txt",
        "https://raw.githubusercontent.com/MhdiTaheri/ProxyCollector/main/proxy.txt",
        "https://raw.githubusercontent.com/SoliSpirit/mtproto/master/all_proxies.txt"
    ]
    
    telegram_urls = [
        "https://t.me/s/iporoto",
        "https://t.me/s/HiProxy",
        "https://t.me/s/iproxy",
        "https://t.me/s/iRoProxy",
        "https://t.me/s/proxyforopeta",
        "https://t.me/s/IRN_Proxy",
        "https://t.me/s/MProxy_ir",
        "https://t.me/s/ProxyHagh",
        "https://t.me/s/PyroProxy",
        "https://t.me/s/ProxyMTProto",
        "https://t.me/s/MTPro_XYZ",
        "https://t.me/s/vpns",
        "https://t.me/s/mtmvpn",
        "https://t.me/s/asr_proxy",
        "https://t.me/s/proxyskyy"
    ]
    
    text_proxies = fetch_proxies_from_text_urls(text_urls)
    
    telegram_proxies = []
    for url in telegram_urls:
        proxies = fetch_proxies_from_telegram_channel(url)
        telegram_proxies.extend(proxies)
    
    all_proxies = text_proxies + telegram_proxies
    
    all_proxies = save_proxies_to_file(all_proxies)
    
    update_readme(all_proxies)
