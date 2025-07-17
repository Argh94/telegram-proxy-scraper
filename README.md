# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 17 July 2025, 15:21 UTC (به وقت ایران: 18:51)

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
  - [SoliSpirit/mtproto](https://raw.githubusercontent.com/SoliSpirit/mtproto/master/all_proxies.txt)
- **کانال‌های تلگرام**:
  - iporoto, HiProxy, iproxy, iRoProxy, proxyforopeta, IRN_Proxy, MProxy_ir, ProxyHagh, PyroProxy, ProxyMTProto, MTPro_XYZ, vpns, mtmvpn

## نمونه پروکسی‌ها
جدول زیر 20 پروکسی نمونه از فایل `proxy.txt` رو نشون می‌ده. برای کپی کردن لینک پروکسی، روی متن تو ستون "لینک پروکسی" لمس طولانی کنید و "Copy" رو انتخاب کنید:

| #  | سرور (Server)       | پورت (Port) | وضعیت     | لینک پروکسی                     |
|----|---------------------|-------------|-----------|---------------------------------|
| 1 | 103.161.35.124 | 443 | فعال | `tg://proxy?server=103.161.35.124&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 2 | 23.88.96.144 | 155 | فعال | `tg://proxy?server=23.88.96.144&port=155&secret=7HQighJPBNMYVRNB6tdkVw` |
| 3 | 1.irpower-a.ir | 443 | فعال | `tg://proxy?server=1.irpower-a.ir&port=443&secret=7gffffffff___f_______Adkb3dubG9hZC53aW5kb3dzdXBkYXRlLmNvbQ==**` |
| 4 | 212.34.141.71 | 443 | فعال | `tg://proxy?server=212.34.141.71&port=443&secret=1320PuNyHw_LQKT_Y7XNJw` |
| 5 | 91.99.192.115 | 70 | فعال | `tg://proxy?server=91.99.192.115&port=70&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0=` |
| 6 | 22.196.92.88 | 2940 | فعال | `tg://proxy?server=22.196.92.88&port=2940&secret=7gwwYoISy716xRkTAgVSXRVpYS5zdGVhbXBvd2VyZWQuY29t` |
| 7 | World-press.Online-shop.speeker-voice.avadox-zhoan.info | 144 | فعال | `tg://proxy?server=World-press.Online-shop.speeker-voice.avadox-zhoan.info&port=144&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 8 | 185.95.159.231 | 9741 | فعال | `tg://proxy?server=185.95.159.231&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 9 | 87.248.132.70 | 155 | فعال | `tg://proxy?server=87.248.132.70&port=155&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0=` |
| 10 | 91.99.172.152 | 8888 | فعال | `tg://proxy?server=91.99.172.152&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 11 | 43.100.108.50 | 443 | فعال | `tg://proxy?server=43.100.108.50&port=443&secret=eee04e6821ae19ca3755852644532a6f61617a7572652e6d6963726f736f66742e636f6d` |
| 12 | 87.248.132.38 | 85 | فعال | `tg://proxy?server=87.248.132.38&port=85&secret=ee0000f00f0f775555fffffff5006e2e69646F776E6C6F61642E77696E646F77737570646174652E636F6D` |
| 13 | iran.zibayi.shop. | 888 | فعال | `tg://proxy?server=iran.zibayi.shop.&port=888&secret=ee0c30628212cbbd7ac519130205525d1569612e737465616d706f77657265642e636f6d` |
| 14 | 95.169.173.9 | 8443 | فعال | `tg://proxy?server=95.169.173.9&port=8443&secret=1320PuNyHw_LQKT_Y7XNJw` |
| 15 | 79.172.228.58 | 70 | فعال | `tg://proxy?server=79.172.228.58&port=70&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 16 | 91.99.105.128 | 8888 | فعال | `tg://proxy?server=91.99.105.128&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 17 | fitidream.fiziotr.info | 443 | فعال | `tg://proxy?server=fitidream.fiziotr.info&port=443&secret=FgMBAgABAAH8AwOG4kw63Q==` |
| 18 | 157.180.46.166 | 8888 | فعال | `tg://proxy?server=157.180.46.166&port=8888&secret=DD1603010200010001fc030386e24c3add` |
| 19 | 77.248.132.188 | 155 | فعال | `tg://proxy?server=77.248.132.188&port=155&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 20 | siteimprove.ir | 443 | فعال | `tg://proxy?server=siteimprove.ir&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |


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
