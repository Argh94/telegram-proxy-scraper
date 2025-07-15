# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 15 July 2025, 12:57 UTC (به وقت ایران: 16:27)

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
| 1 | 93.88.205.26 | 888 | فعال | `tg://proxy?server=93.88.205.26&port=888&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 2 | 62.60.178.95 | 9741 | فعال | `tg://proxy?server=62.60.178.95&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d**` |
| 3 | 62.60.176.242 | 443 | فعال | `tg://proxy?server=62.60.176.242&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)`` |
| 4 | 91.99.235.68 | 888 | فعال | `tg://proxy?server=91.99.235.68&port=888&secret=ee79e344818749bd7ac519130220c25d0969612e737465616d706f77657265642e636f6d` |
| 5 | 62.60.179.150 | 343 | فعال | `tg://proxy?server=62.60.179.150&port=343&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d` |
| 6 | arvan.irpower-g.ir | 443 | فعال | `tg://proxy?server=arvan.irpower-g.ir&port=443&secret=7gffffffff___f___Adkb3dubG9hZC53aW5kb3dzdXBkYXRlLmNvbQ` |
| 7 | 79.172.228.4 | 443 | فعال | `tg://proxy?server=79.172.228.4&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 8 | proxybooth.work.gd | 80 | فعال | `tg://proxy?server=proxybooth.work.gd&port=80&secret=7ja01nJUt2Ql1emlrQCwAbZzdGVhbXBvd2VyZWQuY29t` |
| 9 | 91.99.15.77 | 888 | فعال | `tg://proxy?server=91.99.15.77&port=888&secret=7gwwYoISy716xRkTAgVSXRVpYS5zdGVhbXBvd2VyZWQuY29t` |
| 10 | 62.60.179.109 | 443 | فعال | `tg://proxy?server=62.60.179.109&port=443&secret=7hAQEP8PSAZT____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 11 | 49.13.145.62 | 443 | فعال | `tg://proxy?server=49.13.145.62&port=443&secret=3QAAAAAAAAAAAAAAAAAAAAA=` |
| 12 | 88.link-a3.ir | 443 | فعال | `tg://proxy?server=88.link-a3.ir&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 13 | jak-paris.homborg-hamborg.dodos-codam.jojo19.ir | 443 | فعال | `https://t.me/proxy?server=jak-paris.homborg-hamborg.dodos-codam.jojo19.ir&port=443&secret=7gD_AA___wD_9VVf______VtZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 14 | 138.197.126.247 | 8443 | فعال | `tg://proxy?server=138.197.126.247&port=8443&secret=7hURURURURURURURURURURVtZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 15 | 91.99.179.31 | 70 | فعال | `tg://proxy?server=91.99.179.31&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d` |
| 16 | cai7kkj46fbf.dop1000.com | 443 | فعال | `tg://proxy?server=cai7kkj46fbf.dop1000.com&port=443&secret=ee21ef372ec7034a96b00807b1ed45d42d636c7562686f7573652e7075626e75622e636f6d` |
| 17 | 147.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=147.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 18 | xfuonvsf0102.dop321.com | 443 | فعال | `tg://proxy?server=xfuonvsf0102.dop321.com&port=443&secret=ee93a42038d95440949ea6d80ba3bb9daf3467656e6465726a7573746963652e6f7267` |
| 19 | 140.233.187.111 | 443 | فعال | `tg://proxy?server=140.233.187.111&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 20 | Team.hafthashtgswreqetdgsrwrpi-esoiiisolfnwfsksjvwu-urishklfduiwoehv.info. | 6773 | فعال | `https://t.me/proxy?server=Team.hafthashtgswreqetdgsrwrpi-esoiiisolfnwfsksjvwu-urishklfduiwoehv.info.&port=6773&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA` |


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
