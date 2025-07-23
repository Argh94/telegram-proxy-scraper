# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 23 July 2025, 12:44 UTC (به وقت ایران: 16:14)

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
| 1 | 151.244.85.48 | 443 | فعال | `tg://proxy?server=151.244.85.48&port=443&secret=eed77db43ee3721f0fcb40a4ff6` |
| 2 | 5.255.122.86 | 443 | فعال | `tg://proxy?server=5.255.122.86&port=443&secret=15115115115115115115115115115115` |
| 3 | 91.99.169.51 | 8888 | فعال | `tg://proxy?server=91.99.169.51&port=8888&secret=7gAA8A8Pd1VV` |
| 4 | bib.bib.game.zx2hgujoiah-xy1xutr021-2tk.info | 8443 | فعال | `tg://proxy?server=bib.bib.game.zx2hgujoiah-xy1xutr021-2tk.info&port=8443&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0)__` |
| 5 | dns.bahalbax.ir | 443 | فعال | `tg://proxy?server=dns.bahalbax.ir&port=443&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0` |
| 6 | 62.113.116.140 | 443 | فعال | `https://t.me/proxy?server=62.113.116.140&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 7 | 109.172.87.223 | 443 | فعال | `tg://proxy?server=109.172.87.223&port=443&secret=7td9tD7jch8Py0Ck_2O1zSdtZWRpYS5zdGVhb` |
| 8 | end.iropt-q.ir | 443 | فعال | `tg://proxy?server=end.iropt-q.ir&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 9 | 79.172.228.15 | 85 | فعال | `tg://proxy?server=79.172.228.15&port=85&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 10 | Iran.cdnhub.ir. | 443 | فعال | `tg://proxy?server=Iran.cdnhub.ir.&port=443&secret=7nlnZpKACGMvBKgv9kq9q-5waXJvb3ouc2lnbWFtZXNzZW5nZXIuY29t` |
| 11 | sebro.sheshko.info | 443 | فعال | `tg://proxy?server=sebro.sheshko.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d` |
| 12 | 91.84.107.88 | 443 | فعال | `tg://proxy?server=91.84.107.88&port=443&secret=ee07df7df7df7dfffffdfffffffffffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d` |
| 13 | 188.40.70.227 | 443 | فعال | `tg://proxy?server=188.40.70.227&port=443&secret=EERighJJvXrFGRMCIMJdCQ` |
| 14 | 62.60.158.137 | 69 | فعال | `tg://proxy?server=62.60.158.137&port=69&secret=7pVZ3VtL_Wuy49KeR-ZTRlBtZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 15 | 185.21.14.155 | 443 | فعال | `https://t.me/proxy?server=185.21.14.155&port=443&secret=eeNEgYdJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA` |
| 16 | fasst.sitemcinet.co.uk | 443 | فعال | `tg://proxy?server=fasst.sitemcinet.co.uk&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t)__` |
| 17 | 109.107.178.86 | 443000 | فعال | `tg://proxy?server=109.107.178.86&port=443000&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ` |
| 18 | cd9ffdcd077ba605.bytezs.ir | 443 | فعال | `tg://proxy?server=cd9ffdcd077ba605.bytezs.ir&port=443&secret=7gcgcgcgcgcgcgcgcgcgcgd0cmFuc2xhdGUuZ29v)__` |
| 19 | 91.99.105.128 | 8888 | فعال | `tg://proxy?server=91.99.105.128&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 20 | 91.99.103.222 | 155 | فعال | `tg://proxy?server=91.99.103.222&port=155&secret=ee07df7df7df7dffdffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d` |


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
