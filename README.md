# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 18 July 2025, 09:04 UTC (به وقت ایران: 12:34)

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
| 1 | 163.123.141.136 | 443 | فعال | `tg://proxy?server=163.123.141.136&port=443&secret=7vkAr0QWBCY6CEwapzrzMaxnb29nbGUuY29t` |
| 2 | 46.62.151.238 | 443 | فعال | `tg://proxy?server=46.62.151.238&port=443&secret=7gD_AA_wD_9VVf____VtZWRpYS5zdGVhbXBvd2VyZWQuY29t)__` |
| 3 | 151.244.85.32 | 70 | فعال | `tg://proxy?server=151.244.85.32&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6` |
| 4 | 5.255.125.203 | 443 | فعال | `tg://proxy?server=5.255.125.203&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d` |
| 5 | aval.fsaremi.info | 443 | فعال | `tg://proxy?server=aval.fsaremi.info&port=443&secret=7hYDAQIAAQAB_AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 6 | 93.88.205.5 | 888 | فعال | `tg://proxy?server=93.88.205.5&port=888&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 7 | 212.34.134.99 | 443 | فعال | `https://t.me/proxy?server=212.34.134.99&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 8 | yozar.abarwitch.info | 443 | فعال | `tg://proxy?server=yozar.abarwitch.info&port=443&secret=FgMBAgABAAH8AwOG4kw63Q==` |
| 9 | 78.47.82.66 | 443 | فعال | `tg://proxy?server=78.47.82.66&port=443&secret=DDBighLLvXrFGRMCBVJdFQ` |
| 10 | 157.180.92.108 | 8888 | فعال | `tg://proxy?server=157.180.92.108&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 11 | 194.164.34.200 | 443 | فعال | `https://t.me/proxy?server=194.164.34.200&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 12 | 176.65.135.72 | 443 | فعال | `tg://proxy?server=176.65.135.72&port=443&secret=7gAA8A8Pd1VV____9QBuLmlkb3dubG9hZC53aW5kb3dzdXBkYXRlLmNvbQ)|` |
| 13 | 138.201.195.175 | 443 | فعال | `tg://proxy?server=138.201.195.175&port=443&secret=104462821249bd7ac519130220c25d09` |
| 14 | 62.60.176.38 | 443 | فعال | `tg://proxy?server=62.60.176.38&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)__` |
| 15 | 212.34.135.78 | 443 | فعال | `tg://proxy?server=212.34.135.78&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 16 | 117.55.203.133 | 56068 | فعال | `tg://proxy?server=117.55.203.133&port=56068&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d` |
| 17 | 95.169.173.13 | 85 | فعال | `tg://proxy?server=95.169.173.13&port=85&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 18 | 87.248.134.203 | 443 | فعال | `tg://proxy?server=87.248.134.203&port=443&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D)__` |
| 19 | morgh.2p2p.ir | 8080 | فعال | `tg://proxy?server=morgh.2p2p.ir&port=8080&secret=7maIHm4ebR_2ZmZmYW1mrq5ob3N0aXJhbi5jbG91ZA==` |
| 20 | 91.99.201.44 | 443 | فعال | `tg://proxy?server=91.99.201.44&port=443&secret=eec862057ba49a7ecdf0ad4eb44cd5bb11646f776e6c6f61642e77696e646f77737570646174652e636f6d)__` |


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
