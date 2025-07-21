# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 21 July 2025, 09:29 UTC (به وقت ایران: 12:59)

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
3. برای کپی کردن پروکسی‌های زیر، روی لینک تو ستون "لینک پروکسی" کلیک کنید یا لمس طولانی کنید و گزینه "Copy" رو انتخاب کنید، سپس تو تلگرام پیست کنید.
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
جدول زیر 20 پروکسی نمونه از فایل `proxy.txt` رو نشون می‌ده. برای کپی کردن لینک پروکسی، روی متن تو ستون "لینک پروکسی" کلیک کنید یا لمس طولانی کنید و "Copy" رو انتخاب کنید:

| #  | سرور (Server)       | پورت (Port) | وضعیت     | لینک پروکسی                     |
|----|---------------------|-------------|-----------|---------------------------------|
| 1 | ناشناخته | ناشناخته | فعال | [پروکسی 1](tg://proxy?server=45.135.192.245&port=85&secret=ee0000f00f0f775555fffffff5006e2e69646F776E6C6F61642E77696E646F77737570646174652E636F6D) |
| 2 | ناشناخته | ناشناخته | فعال | [پروکسی 2](tg://proxy?server=91.99.100.55&port=155&secret=ddec742282124f04d318551341ead76457) |
| 3 | ناشناخته | ناشناخته | فعال | [پروکسی 3](tg://proxy?server=00900.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t**) |
| 4 | ناشناخته | ناشناخته | فعال | [پروکسی 4](tg://proxy?server=91.99.145.87&port=888&secret=7gwwYoISy716xRkTAgVSXRVpYS5zdGVhbXBvd2VyZWQuY29t) |
| 5 | ناشناخته | ناشناخته | فعال | [پروکسی 5](tg://proxy?server=62.60.179.82&port=443&secret=7hAQEP8PSAZT____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 6 | ناشناخته | ناشناخته | فعال | [پروکسی 6](tg://proxy?server=83.147.255.85&port=443&secret=EE1603010200010007f0030386e24c3add646f776e6c6f61642e77696e646f77737570646174652e636f6d) |
| 7 | ناشناخته | ناشناخته | فعال | [پروکسی 7](tg://proxy?server=5.255.114.52&port=443&secret=15115115115115115115115115115115) |
| 8 | ناشناخته | ناشناخته | فعال | [پروکسی 8](tg://proxy?server=91.99.206.83&port=70&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0=)__) |
| 9 | ناشناخته | ناشناخته | فعال | [پروکسی 9](tg://proxy?server=87.248.134.14&port=200&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | ناشناخته | ناشناخته | فعال | [پروکسی 10](https://t.me/proxy?server=57.130.30.202&port=100&secret=EERighJJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 11 | ناشناخته | ناشناخته | فعال | [پروکسی 11](tg://proxy?server=91.99.206.53&port=59065&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E73) |
| 12 | ناشناخته | ناشناخته | فعال | [پروکسی 12](tg://proxy?server=62.60.178.117&port=443&secret=1603010200010001fc030386e24c3add) |
| 13 | ناشناخته | ناشناخته | فعال | [پروکسی 13](tg://proxy?server=109.104.154.226&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t**) |
| 14 | ناشناخته | ناشناخته | فعال | [پروکسی 14](tg://proxy?server=89.111.22.103&port=443&secret=7hAQEP8PSAZT____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 15 | ناشناخته | ناشناخته | فعال | [پروکسی 15](tg://proxy?server=87.248.132.44&port=200&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 16 | ناشناخته | ناشناخته | فعال | [پروکسی 16](tg://proxy?server=150.241.79.45&port=69&secret=7pVZ3VtL_Wuy49KeR-ZTRlB3d3cuc3BlZWR0ZXN0Lm5ldA==) |
| 17 | ناشناخته | ناشناخته | فعال | [پروکسی 17](tg://proxy?server=46.245.64.60&port=443&secret=36d4db00f0ae7d7c6e3d7b29dfe04134) |
| 18 | ناشناخته | ناشناخته | فعال | [پروکسی 18](tg://proxy?server=91.107.164.77&port=27&secret=1320PuNyHw_LQKT_Y7XNJw==) |
| 19 | ناشناخته | ناشناخته | فعال | [پروکسی 19](tg://proxy?server=62.60.176.141&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d) |
| 20 | ناشناخته | ناشناخته | فعال | [پروکسی 20](tg://proxy?server=91.99.169.201&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29) |


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
