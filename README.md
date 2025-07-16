# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 16 July 2025, 20:32 UTC (به وقت ایران: 00:02)

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
| 1 | 172.99.188.74 | 443 | فعال | `tg://proxy?server=172.99.188.74&port=443&secret=ee1603010200010001fc030386e24c3add64726f70626f782e636f6d` |
| 2 | 46.62.144.121 | 70 | فعال | `tg://proxy?server=46.62.144.121&port=70&secret=7gAA8A8Pd1VV____9QBuLmktLXd-Z28tLS0=` |
| 3 | 87.248.132.70 | 155 | فعال | `tg://proxy?server=87.248.132.70&port=155&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0=` |
| 4 | 91.99.105.128 | 8888 | فعال | `tg://proxy?server=91.99.105.128&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29` |
| 5 | 49.13.145.67 | 443 | فعال | `tg://proxy?server=49.13.145.67&port=443&secret=3QAAAAAAAAAAAAAAAAAAAAA=` |
| 6 | 195.57.9.lll-lll.ir | 443 | فعال | `tg://proxy?server=195.57.9.lll-lll.ir&port=443&secret=eeXifpB2GBv9shh2kvi5lA==` |
| 7 | 91.99.171.213 | 8888 | فعال | `tg://proxy?server=91.99.171.213&port=8888&secret=7gAA8A8Pd1VV` |
| 8 | 91.99.171.213 | 8888 | فعال | `tg://proxy?server=91.99.171.213&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 9 | 103.161.34.233 | 85 | فعال | `tg://proxy?server=103.161.34.233&port=85&secret=ee0000f00f0f775555fffffff5006e2e69646F776E6C6F61642E77696E646F77737570646174652E636F6D` |
| 10 | yozar.abarwitch.info | 443 | فعال | `tg://proxy?server=yozar.abarwitch.info&port=443&secret=FgMBAgABAAH8AwOG4kw63Q==` |
| 11 | 104.21.21.77 | 443 | فعال | `tg://proxy?server=104.21.21.77&port=443&secret=3QAAAAAAAAAAAAAAAAAAAAA**` |
| 12 | 78.47.82.66 | 443 | فعال | `tg://proxy?server=78.47.82.66&port=443&secret=DDBighLLvXrFGRMCBVJdFQ==` |
| 13 | 79.172.228.29 | 70 | فعال | `tg://proxy?server=79.172.228.29&port=70&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 14 | 87.229.100.234 | 7777 | فعال | `tg://proxy?server=87.229.100.234&port=7777&secret=eeRighJJvXrFGRMCIMJdCQ` |
| 15 | 91.99.85.639l.ir | 110 | فعال | `tg://proxy?server=91.99.85.639l.ir&port=110&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0=` |
| 16 | 91.99.172.214 | 8888 | فعال | `tg://proxy?server=91.99.172.214&port=8888&secret=7gAA8A8Pd1VV` |
| 17 | 140.233.187.210 | 443 | فعال | `tg://proxy?server=140.233.187.210&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d` |
| 18 | 87.248.132.29 | 70 | فعال | `tg://proxy?server=87.248.132.29&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636FtH` |
| 19 | iran.needhost.ir. | 443 | فعال | `tg://proxy?server=iran.needhost.ir.&port=443&secret=7veb2r8DoV-UM_4TNesqGclpcmFuLm5lZWRob3N0Lmly` |
| 20 | Q3.opt-meli.info | 443 | فعال | `https://t.me/proxy?server=Q3.opt-meli.info&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |


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
