# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 15 July 2025, 18:40 UTC (به وقت ایران: 22:10)

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
| 1 | 93.88.205.5 | 888 | فعال | `tg://proxy?server=93.88.205.5&port=888&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 2 | 91.99.170.217 | 8888 | فعال | `tg://proxy?server=91.99.170.217&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 3 | xadip.bambo.oooooooooo.ir | 443 | فعال | `tg://proxy?server=xadip.bambo.oooooooooo.ir&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 4 | 151.244.85.32 | 70 | فعال | `tg://proxy?server=151.244.85.32&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6` |
| 5 | 78.46.245.210 | 443 | فعال | `tg://proxy?server=78.46.245.210&port=443&secret=0c30628212cbbd7ac519130205525d15` |
| 6 | 91.99.185.220 | 888 | فعال | `tg://proxy?server=91.99.185.220&port=888&secret=ee0c30628212cbbd7ac519130205525d1569612e737465616d706f77657265642e636f6d` |
| 7 | chernobill.technote.ir | 443 | فعال | `tg://proxy?server=chernobill.technote.ir&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d` |
| 8 | 194.26.141.97 | 443 | فعال | `tg://proxy?server=194.26.141.97&port=443&secret=EE100404ff0f48064fffffff9001b8696d696d656469612e737465616d706f77657265642e636f6d` |
| 9 | 150.241.79.45 | 69 | فعال | `tg://proxy?server=150.241.79.45&port=69&secret=7pVZ3VtL_Wuy49KeR-ZTRlB3d3cuc3BlZWR0ZXN0Lm5ldA==` |
| 10 | 37.27.252.251 | 100 | فعال | `tg://proxy?server=37.27.252.251&port=100&secret=7gQB8C8Pd1VF____9QJuPnktLXcuZ28tLS0=` |
| 11 | 51.159.165.172 | 7549 | فعال | `tg://proxy?server=51.159.165.172&port=7549&secret=eeff9890eed0a3c6fbfafeb2608a4aedb37777772e736974652e636f6d` |
| 12 | 45.86.230.177 | 56777 | فعال | `tg://proxy?server=45.86.230.177&port=56777&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 13 | Yoast.harcibasheokeye.ir | 918 | فعال | `tg://proxy?server=Yoast.harcibasheokeye.ir&port=918&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t)__` |
| 14 | 62.60.178.195 | 443 | فعال | `tg://proxy?server=62.60.178.195&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ` |
| 15 | 103.161.34.13 | 65 | فعال | `tg://proxy?server=103.161.34.13&port=65&secret=eeNEgYdJvXrFGRMCIMJdCQ**` |
| 16 | 62.60.178.55 | 443 | فعال | `tg://proxy?server=62.60.178.55&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)__` |
| 17 | 157.180.92.108 | 8888 | فعال | `tg://proxy?server=157.180.92.108&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 18 | 193.233.253.118 | 55824 | فعال | `tg://proxy?server=193.233.253.118&port=55824&secret=ee00000000000000000000000000000000737465616D706F77657265642E636F6d)__` |
| 19 | 176.65.135.58 | 220 | فعال | `tg://proxy?server=176.65.135.58&port=220&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 20 | 193.3.190.47 | 85 | فعال | `tg://proxy?server=193.3.190.47&port=85&secret=7gAA8A8Pd1VV____9QBuLmljaGF0Z3B0LmNvbQ==` |


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
