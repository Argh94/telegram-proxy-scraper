# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 16 July 2025, 20:13 UTC (به وقت ایران: 23:43)

این پروژه یه اسکریپت پایتون برای جمع‌آوری خودکار پروکسی‌های MTProto تلگرام از منابع متنی و کانال‌های تلگرامه. پروکسی‌ها تو فایل `proxy.txt` ذخیره می‌شن و هر 6 ساعت به‌صورت خودکار به‌روزرسانی می‌شن.

## درباره پروژه

این اسکریپت با استفاده از `requests` برای منابع متنی و `selenium` برای صفحات وب کانال‌های تلگرام (`t.me/s/...`) پروکسی‌های MTProto رو جمع‌آوری می‌کنه. پروکسی‌های تکراری حذف می‌شن و نتیجه تو فایل `proxy.txt` ذخیره می‌شه. فرآیند به‌صورت خودکار با **GitHub Actions** هر 6 ساعت اجرا می‌شه.

## ویژگی‌ها
- جمع‌آوری پروکسی از منابع متنی و کانال‌های تلگرام
- به‌روزرسانی خودکار هر 6 ساعت
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
- **کانال‌های تلگرام**:
  - iporoto, HiProxy, iproxy, iRoProxy, proxyforopeta, IRN_Proxy, MProxy_ir, ProxyHagh, PyroProxy, ProxyMTProto, MTPro_XYZ, vpns, mtmvpn

## نمونه پروکسی‌ها
جدول زیر 20 پروکسی نمونه از فایل `proxy.txt` رو نشون می‌ده. برای کپی کردن لینک پروکسی، روی متن تو ستون "لینک پروکسی" لمس طولانی کنید و "Copy" رو انتخاب کنید:

| #  | سرور (Server)       | پورت (Port) | وضعیت     | لینک پروکسی                     |
|----|---------------------|-------------|-----------|---------------------------------|
| 1 | 8.220.185.235 | 443 | فعال | `tg://proxy?server=8.220.185.235&port=443&secret=eee8725affe357534b2ff1e6a1727b47ee617a7572652e6d6963726f736f66742e636f6d` |
| 2 | 116.203.81.58 | 8888 | فعال | `tg://proxy?server=116.203.81.58&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 3 | 95.169.173.8 | 8443 | فعال | `tg://proxy?server=95.169.173.8&port=8443&secret=1320PuNyHw_LQKT_Y7XNJw` |
| 4 | 65.109.193.216 | 443 | فعال | `tg://proxy?server=65.109.193.216&port=443&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 5 | 62.60.179.213 | 9741 | فعال | `tg://proxy?server=62.60.179.213&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 6 | 4455.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=4455.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 7 | meli.zban-df.info | 8888 | فعال | `tg://proxy?server=meli.zban-df.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 8 | 213.176.94.18 | 443 | فعال | `tg://proxy?server=213.176.94.18&port=443&secret=ee151151151151151151151151151151156D656469612E737465616D706F77657265642E636F6D` |
| 9 | 185.157.212.84 | 443 | فعال | `tg://proxy?server=185.157.212.84&port=443&secret=7rXpXsHm4qJ_nKJvoq_oq_ptZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 10 | 5.255.97.150 | 443 | فعال | `tg://proxy?server=5.255.97.150&port=443&secret=15115115115115115115115115115115` |
| 11 | 79.172.228.15 | 85 | فعال | `tg://proxy?server=79.172.228.15&port=85&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 12 | 47.243.58.241 | 443 | فعال | `tg://proxy?server=47.243.58.241&port=443&secret=ee869510fa3cc873a13e0e74321eab0c75617a7572652e6d6963726f736f66742e636f6d` |
| 13 | 79.172.228.22 | 70 | فعال | `tg://proxy?server=79.172.228.22&port=70&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 14 | 62.60.179.129 | 8080 | فعال | `tg://proxy?server=62.60.179.129&port=8080&secret=7nnjRIGHSb16xRkTAiDCXQltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 15 | 65.108.12.153 | 65 | فعال | `tg://proxy?server=65.108.12.153&port=65&secret=1320PuNyHw_LQKT_Y7XNJw==` |
| 16 | 117.55.203.133 | 56068 | فعال | `tg://proxy?server=117.55.203.133&port=56068&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d` |
| 17 | 62.60.177.22 | 443 | فعال | `tg://proxy?server=62.60.177.22&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D)__` |
| 18 | 87.248.132.18 | 85 | فعال | `tg://proxy?server=87.248.132.18&port=85&secret=ee0000f00f0f775555fffffff5006e2e69646F776E6C6F61642E77696E646F77737570646174652E636F6D` |
| 19 | 94.130.221.24 | 404 | فعال | `tg://proxy?server=94.130.221.24&port=404&secret=eeNEgYdJvXrFGRMCIMJdCQ==` |
| 20 | 2.meli.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=2.meli.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |


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
