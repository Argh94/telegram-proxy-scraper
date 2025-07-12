# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 12 July 2025, 02:11 UTC (به وقت ایران: 05:41)

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
| 1 | rightel.irancell.irib.snapp.digikala.cloud.iranian.irib.ahmadp206.namli--binjzk.info | 666 | فعال | `tg://proxy?server=rightel.irancell.irib.snapp.digikala.cloud.iranian.irib.ahmadp206.namli--binjzk.info&port=666&secret=7ggggggggggggggggggggghtZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 2 | 20.218.180.204 | 4443 | فعال | `tg://proxy?server=20.218.180.204&port=4443&secret=b3c1f2bf123b4e5e2fc03c0c4232e2c7` |
| 3 | 134.199.190.138 | 9741 | فعال | `tg://proxy?server=134.199.190.138&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 4 | 157.180.120.251 | 23 | فعال | `tg://proxy?server=157.180.120.251&port=23&secret=1320PuNyHw_LQKT_Y7XNJw==` |
| 5 | 91.99.197.199 | 70 | فعال | `tg://proxy?server=91.99.197.199&port=70&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0=` |
| 6 | 04444.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=04444.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 7 | 46.249.110.51 | 443 | فعال | `https://t.me/proxy?server=46.249.110.51&port=443&secret=ee151151151151151151151151151151156D656469612E737465616D706F77657265642E636F6D` |
| 8 | 167.235.243.48 | 551 | فعال | `tg://proxy?server=167.235.243.48&port=551&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 9 | 62.60.179.139 | 443 | فعال | `tg://proxy?server=62.60.179.139&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)`` |
| 10 | 95.216.22.207 | 443 | فعال | `tg://proxy?server=95.216.22.207&port=443&secret=iORid5lJ237IiBMGYMQMdw` |
| 11 | 91.99.178.38 | 888 | فعال | `tg://proxy?server=91.99.178.38&port=888&secret=7gwwYoISy716xRkTAgVSXRVpYS5zdGVhbXBvd2VyZWQuY29t` |
| 12 | 62.60.177.42 | 343 | فعال | `tg://proxy?server=62.60.177.42&port=343&secret=FgMBAgABAAfwAwOG4kw63Q` |
| 13 | 62.60.176.44 | 443 | فعال | `tg://proxy?server=62.60.176.44&port=443&secret=7qrf MH/OtbDjhkWhT5OSbt3d3cuY2xvdWRmbGFyZS5jb20` |
| 14 | 62.60.178.3 | 8888 | فعال | `tg://proxy?server=62.60.178.3&port=8888&secret=7gAA8A8Pd1VV9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t____` |
| 15 | 62.60.178.146 | 443 | فعال | `tg://proxy?server=62.60.178.146&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)`` |
| 16 | 157.180.112.185 | 443 | فعال | `tg://proxy?server=157.180.112.185&port=443&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 17 | 213.145.71.36 | 443 | فعال | `tg://proxy?server=213.145.71.36&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 18 | 94.130.48.73 | 8443 | فعال | `tg://proxy?server=94.130.48.73&port=8443&secret=DDBighLLvXrFGRMCBVJdFQ==` |
| 19 | Error.parsa-learning.ir. | 333 | فعال | `https://t.me/proxy?server=Error.parsa-learning.ir.&port=333&secret=7hAQEP8PSAZT____9QBuLmlpYS5zdGVhbXBvd2VyZWQuY29t` |
| 20 | home.cphosting.shop | 443 | فعال | `tg://proxy?server=home.cphosting.shop&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |


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
