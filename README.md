# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 18 July 2025, 09:09 UTC (به وقت ایران: 12:39)

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
| 1 | 212.34.134.99 | 443 | فعال | `https://t.me/proxy?server=212.34.134.99&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 2 | 37.27.202.36 | 81 | فعال | `tg://proxy?server=37.27.202.36&port=81&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0=` |
| 3 | 151.244.42.4 | 85 | فعال | `tg://proxy?server=151.244.42.4&port=85&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 4 | 91.99.228.230 | 59065 | فعال | `https://t.me/proxy?server=91.99.228.230&port=59065&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 5 | 62.60.179.139 | 443 | فعال | `tg://proxy?server=62.60.179.139&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)`` |
| 6 | 46.62.146.34 | 200 | فعال | `tg://proxy?server=46.62.146.34&port=200&secret=eeb2afad908ddd149ac788045d721ae7d4736e6170702e6972` |
| 7 | ryzen-gold.shesh-station.ir | 443 | فعال | `tg://proxy?server=ryzen-gold.shesh-station.ir&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d` |
| 8 | 62.60.177.35 | 443 | فعال | `tg://proxy?server=62.60.177.35&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ` |
| 9 | 62.60.177.195 | 9741 | فعال | `tg://proxy?server=62.60.177.195&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 10 | 8.meli.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=8.meli.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 11 | 157.180.127.223 | 8888 | فعال | `tg://proxy?server=157.180.127.223&port=8888&secret=1603010200010001fc030386e24c3add` |
| 12 | 78.46.234.177 | 443 | فعال | `tg://proxy?server=78.46.234.177&port=443&secret=DDBighLLvXrFGRMCBVJdFQ==` |
| 13 | 94.130.221.24 | 404 | فعال | `tg://proxy?server=94.130.221.24&port=404&secret=eeNEgYdJvXrFGRMCIMJdCQ==` |
| 14 | syczleck.itemag.ir | 443 | فعال | `tg://proxy?server=syczleck.itemag.ir&port=443&secret=7hYDAQIAAQAB_AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 15 | rightel.irancell.irib.snapp.digikala.cloud.iranian.irib.ahmadp206.namli--binjzk.info | 666 | فعال | `tg://proxy?server=rightel.irancell.irib.snapp.digikala.cloud.iranian.irib.ahmadp206.namli--binjzk.info&port=666&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 16 | 95.217.225.85 | 65 | فعال | `tg://proxy?server=95.217.225.85&port=65&secret=1320PuNyHw_LQKT_Y7XNJw` |
| 17 | rightel.irancell.irib.snapp.digikala.cloud.iranian.irib.ahmadp206.namakdarya.info | 777 | فعال | `tg://proxy?server=rightel.irancell.irib.snapp.digikala.cloud.iranian.irib.ahmadp206.namakdarya.info&port=777&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 18 | mtproto.vaheed.net | 2028 | فعال | `tg://proxy?server=mtproto.vaheed.net&port=2028&secret=dd2028b5afa0e6d701acec3cd9bb8a902b` |
| 19 | Mortal-Vovok.nuremborg-hamborg.dodos-codam.mehrvilla.info | 443 | فعال | `tg://proxy?server=Mortal-Vovok.nuremborg-hamborg.dodos-codam.mehrvilla.info&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 20 | leveldaemi.fiziotr.info | 443 | فعال | `tg://proxy?server=leveldaemi.fiziotr.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d` |


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
