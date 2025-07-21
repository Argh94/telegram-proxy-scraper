import requests
from bs4 import BeautifulSoup
import re
import random
import time
import logging
from datetime import datetime
import pytz
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import unicodedata

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
]

def get_random_user_agent():
    return random.choice(USER_AGENTS)

def clean_line(line):
    line = line.strip().replace('\r', '').replace('\n', '')
    line = ''.join(c for c in line if unicodedata.category(c)[0] != 'C')
    return line

def fetch_proxies_from_text_urls(urls):
    all_links = []
    headers = {'User-Agent': get_random_user_agent()}
    pattern = r'^(tg://proxy|https://t\.me/proxy)\?server=[^&]+&port=\d+(&secret=.+)$'
    
    for url in urls:
        try:
            logging.info(f"Fetching proxies from {url}")
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            lines = response.text.splitlines()
            for line in lines:
                line = clean_line(line)
                if not line:
                    continue
                if re.match(pattern, line):
                    all_links.append(line)
                    logging.info(f"Valid proxy found: {line}")
                else:
                    logging.debug(f"Invalid or skipped proxy: {line} (does not match pattern)")
            logging.info(f"Fetched {len(lines)} lines, {len(all_links)} valid MTProto proxies from {url}")
        except requests.RequestException as e:
            logging.error(f"HTTP error fetching {url}: {e}")
        time.sleep(random.uniform(1, 3))
    return all_links

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
        for i in range(35):  
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(7)  
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
        proxies = [element.get('href') for element in proxy_elements]
        for proxy in proxies:
            logging.info(f"Valid proxy found from Telegram: {proxy}")
        logging.info(f"Fetched {len(proxies)} MTProto proxies from {url}")
    except WebDriverException as e:
        logging.error(f"WebDriver error fetching {url}: {e}")
    except Exception as e:
        logging.error(f"General error fetching {url}: {e}")
    finally:
        try:
            driver.quit()
        except:
            pass
    time.sleep(random.uniform(2, 5))
    return proxies

def save_proxies_to_file(proxy_list, filename='../proxy.txt'):
    try:
        unique_proxies = list(set(proxy_list))
        with open(filename, 'w', encoding='utf-8') as file:
            for proxy in unique_proxies:
                file.write(proxy + '\n')
        logging.info(f"Saved {len(unique_proxies)} unique proxies to {filename}")
        return unique_proxies
    except IOError as e:
        logging.error(f"Error writing to {filename}: {e}")
        return []

def update_readme(proxy_list):
    try:
        utc_now = datetime.now(pytz.UTC)
        iran_tz = pytz.timezone('Asia/Tehran')
        iran_now = utc_now.astimezone(iran_tz)
        update_time_utc = utc_now.strftime('%d %B %Y, %H:%M UTC')
        update_time_iran = iran_now.strftime('%H:%M')
        logging.info(f"Updating README with timestamp: {update_time_utc} (Iran: {update_time_iran})")

        sample_proxies = random.sample(proxy_list, min(20, len(proxy_list))) if proxy_list else []
        table_rows = ""
        for i, proxy in enumerate(sample_proxies, 1):
            match = re.match(r'^(tg://proxy|https://t\.me/proxy)\?server=([^&]+)&port=(\d+)&secret=.+$', proxy)
            if match:
                server, port = match.groups()[1:3]
                table_rows += f"| {i} | {server} | {port} | فعال | `{proxy}` |\n"

        readme_content = f"""# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: {update_time_utc} (به وقت ایران: {update_time_iran})

این پروژه یه اسکریپت پایتون برای جمع‌آوری خودکار پروکسی‌های MTProto تلگرام از منابع متنی و کانال‌های تلگرامه. پروکسی‌ها تو فایل `proxy.txt` ذخیره می‌شن و هر 3 ساعت به‌صورت خودکار به‌روزرسانی می‌شن.

## درباره پروژه

این اسکریپت با استفاده از `requests` برای منابع متنی و `selenium` برای صفحات وب کانال‌های تلگرام (`t.me/s/...`) پروکسی‌های MTProto رو جمع‌آوری می‌کنه. پروکسی‌های تکراری حذف می‌شن و نتیجه تو فایل `proxy.txt` ذخیره می‌شه. فرآیند به‌صورت خودکار با **GitHub Actions** هر 6 ساعت اجرا می‌شه.

## ویژگی‌ها
- جمع‌آوری پروکسی از منابع متنی و کانال‌های تلگرام
- به‌روزرسانی خودکار هر ۳ ساعت
- حذف پروکسی‌های تکراری
- بدون نیاز به API تلگرام
- مناسب برای کاربرانی که به دنبال پروکسی‌های MTProto فعال هستن

## پیش‌نیازها
- پایتون 3.9
- کتابخونه‌های مورد نیاز: `requests`, `beautifulsoup4`, `selenium`, `pytz`
- فایل `requirements.txt` شامل تمام وابستگی‌هاست.

## نحوه استفاده
1. فایل `proxy.txt` رو از [اینجا](proxy.txt) دانلود کنید.
2. لینک‌های پروکسی (با فرمت `tg://proxy?...` یا `https://t.me/proxy?...`) رو تو کلاینت تلگرام خودتون وارد کنید.
3. برای کپی کردن پروکسی‌های زیر، روی لینک تو ستون "لینک پروکسی" لمس طولانی کنید و گزینه "Copy" رو انتخاب کنید، سپس تو تلگرام پیست کنید.
4. برای به‌روزرسانی دستی، به تب **Actions** تو مخزن برید و روی **Run workflow** کلیک کنید.

## منابع پروکسی
- **منابع متنی**:
  - [MahsaNetConfigTopic](https://raw.githubusercontent.com/MahsaNetConfigTopic/proxy/main/proxies.txt)
  - [ALIILAPRO/MTProtoProxy](https://raw.githubusercontent.com/ALIILAPRO/MTProtoProxy/main/proxy-list.txt)
  - [MhdiTaheri/ProxyCollector](https://raw.githubusercontent.com/MhdiTaheri/ProxyCollector/main/proxy.txt)
  - [SoliSpirit/mtproto](https://raw.githubusercontent.com/SoliSpirit/mtproto/master/all_proxies.txt)
- **کانال‌های تلگرام**:
  - iporoto, HiProxy, iproxy, iRoProxy, proxyforopeta, IRN_Proxy, MProxy_ir, ProxyHagh, PyroProxy, ProxyMTProto, MTPro_XYZ, vpns, mtmvpn

## نمونه پروکسی‌ها
جدول زیر 20 پروکسی نمونه از فایل `proxy.txt` رو نشون می‌ده. برای کپی کردن لینک پروکسی، روی متن تو ستون "لینک پروکسی" لمس طولانی کنید و "Copy" رو انتخاب کنید:

| #  | سرور (Server)       | پورت (Port) | وضعیت     | لینک پروکسی                     |
|----|---------------------|-------------|-----------|---------------------------------|
{table_rows}

> **توجه**: این جدول فقط برای نمایش نمونه‌ست. برای دسترسی به همه پروکسی‌های به‌روز، فایل [proxy.txt](proxy.txt) رو دانلود کنید.

## مشارکت
از مشارکت شما استقبال می‌کنیم! اگه ایده‌ای برای بهبود اسکریپت دارید یا می‌خواید منابع جدیدی اضافه کنید:
1. یه **Issue** تو مخزن باز کنید.
2. یا یه **Pull Request** با تغییرات پیشنهادی بفرستید.

## لایسنس
این پروژه تحت [لایسنس MIT](LICENSE) منتشر شده.

## لینک‌های مفید
- 📄 [لیست پروکسی‌ها](proxy.txt)
- 🚀 [وضعیت GitHub Actions](https://github.com/Argh94/telegram-proxy-scraper/actions)
- ⭐ [ما رو ستاره بدید!](https://github.com/Argh94/telegram-proxy-scraper)

## Stargazers در گذر زمان
[![Stargazers over time](https://starchart.cc/Argh94/telegram-proxy-scraper.svg?variant=adaptive)](https://starchart.cc/Argh94/telegram-proxy-scraper)

---

سپاس از استفاده از **Telegram Proxy Scraper**! اگه سؤالی دارید، تو بخش Issues مطرح کنید. 🌟
"""

        with open('../README.md', 'w', encoding='utf-8') as file:
            file.write(readme_content)
        logging.info("Successfully updated README.md in repository root with latest update time and proxy samples")
    except Exception as e:
        logging.error(f"Error updating README.md: {e}")

if __name__ == "__main__":
    text_urls = [
        "https://raw.githubusercontent.com/MahsaNetConfigTopic/proxy/main/proxies.txt",
        "https://raw.githubusercontent.com/ALIILAPRO/MTProtoProxy/main/proxy-list.txt",
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
    
    all_proxies = list(set(text_proxies + telegram_proxies))
    
    all_proxies = save_proxies_to_file(all_proxies)
    
    update_readme(all_proxies)
