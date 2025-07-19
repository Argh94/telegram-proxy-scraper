# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 19 July 2025, 12:39 UTC (به وقت ایران: 16:09)

این پروژه یه اسکریپت پایتون برای جمع‌آوری خودکار پروکسی‌های MTProto تلگرام از منابع متنی و کانال‌های تلگرامه. پروکسی‌ها تو فایل `proxy.txt` ذخیره می‌شن و هر 3 ساعت به‌صورت خودکار به‌روزرسانی می‌شن.

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
| 1 | 87.248.132.61 | 200 | فعال | `tg://proxy?server=87.248.132.61&port=200&secret=eeNEgYdJvXrFGRMCIMJdCQ)`` |
| 2 | 62.60.179.150 | 343 | فعال | `tg://proxy?server=62.60.179.150&port=343&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d` |
| 3 | 77.238.109.66 | 8081 | فعال | `tg://proxy?server=77.238.109.66&port=8081&secret=ee40dedd8b89df778347626a92bd9ce4be7777772e636c6f7564666c6172652e636f6d` |
| 4 | 93.88.205.36 | 85 | فعال | `tg://proxy?server=93.88.205.36&port=85&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 5 | 9933.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=9933.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 6 | 93.88.205.29 | 888 | فعال | `tg://proxy?server=93.88.205.29&port=888&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 7 | 87.248.134.172 | 443 | فعال | `https://t.me/proxy?server=87.248.134.172&port=443&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 8 | 150.241.79.45 | 69 | فعال | `tg://proxy?server=150.241.79.45&port=69&secret=7pVZ3VtL_Wuy49KeR-ZTRlB3d3cuc3BlZWR0ZXN0Lm5ldA==` |
| 9 | 90.ir.ir.ir.ir.ir.zban-mas.info | 8888 | فعال | `tg://proxy?server=90.ir.ir.ir.ir.ir.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 10 | ai.qwert-naser5.ir | 852 | فعال | `tg://proxy?server=ai.qwert-naser5.ir&port=852&secret=DDBighLLvXrFGRMCBVJdFQRueWVrdGFuZXQuY29tZmFyYTrhdi5jb212YZ6ubmFqXeEuY29t` |
| 11 | 140.233.187.136 | 9741 | فعال | `tg://proxy?server=140.233.187.136&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 12 | 5.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=5.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 13 | 172.86.66.208.irancell.ir.dijikala.co.uk | 443 | فعال | `tg://proxy?server=172.86.66.208.irancell.ir.dijikala.co.uk&port=443&secret=7hYDAQIAAfADA4biTDrd3E53d3cuZ29vZ2xlLmNvbQ==` |
| 14 | 91.107.137.71 | 27 | فعال | `tg://proxy?server=91.107.137.71&port=27&secret=1320PuNyHw_LQKT_Y7XNJw==` |
| 15 | abestick.abarwitch.info | 443 | فعال | `tg://proxy?server=abestick.abarwitch.info&port=443&secret=1603010200010001fc030386e24c3add` |
| 16 | 159.69.178.54 | 100 | فعال | `https://t.me/proxy?server=159.69.178.54&port=100&secret=EERighJJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA` |
| 17 | e7.a27dh1.sbs | 8888 | فعال | `tg://proxy?server=e7.a27dh1.sbs&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 18 | 62.60.179.139 | 443 | فعال | `tg://proxy?server=62.60.179.139&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)`` |
| 19 | 157.180.46.75 | 8888 | فعال | `tg://proxy?server=157.180.46.75&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 20 | 100.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=100.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |


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
