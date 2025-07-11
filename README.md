# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Poriya58p/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Poriya58p/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Poriya58p/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 11 July 2025, 00:48 UTC (به وقت ایران: 04:18)

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
2. لینک‌های پروکسی (با فرمت `tg://proxy?...`) رو تو کلاینت تلگرام خودتون وارد کنید.
3. برای کپی کردن پروکسی‌های زیر، روی لینک تو ستون "لینک پروکسی" لمس طولانی کنید و گزینه "Copy" رو انتخاب کنید، سپس تو تلگرام پیست کنید.
4. برای به‌روزرسانی دستی، به تب **Actions** تو مخزن برید و روی **Run workflow** کلیک کنید.

## منابع پروکسی
- **منابع متنی**:
  - [MahsaNetConfigTopic](https://raw.githubusercontent.com/MahsaNetConfigTopic/proxy/main/proxies.txt)
  - [ALIILAPRO/MTProtoProxy](https://raw.githubusercontent.com/ALIILAPRO/MTProtoProxy/main/proxy-list.txt)
- **کانال‌های تلگرام**:
  - iporoto, HiProxy, iproxy, iRoProxy, proxyforopeta, IRN_Proxy, MProxy_ir, ProxyHagh, PyroProxy, ProxyMTProto, MTPro_XYZ, vpns, mtmvpn

## نمونه پروکسی‌ها
جدول زیر 20 پروکسی نمونه از فایل `proxy.txt` رو نشون می‌ده. برای کپی کردن لینک پروکسی، روی متن تو ستون "لینک پروکسی" لمس طولانی کنید و "Copy" رو انتخاب کنید:

| #  | سرور (Server)       | پورت (Port) | وضعیت     | لینک پروکسی                     |
|----|---------------------|-------------|-----------|---------------------------------|
| 1 | 89.110.123.163 | 90 | فعال | `tg://proxy?server=89.110.123.163&port=90&secret=7gPPmInDT3mcMnl8Tl-dbchtZWRpYS5zdGVhbXBvd2VyZWQuY29tLg==` |
| 2 | 151.244.42.21 | 443 | فعال | `tg://proxy?server=151.244.42.21&port=443&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 3 | 104.248.26.196 | 443 | فعال | `tg://proxy?server=104.248.26.196&port=443&secret=eec80ff604fa45408f1d152624d3bffcf276616e2e6e616a76612e636f6d**` |
| 4 | 45.135.192.244 | 85 | فعال | `tg://proxy?server=45.135.192.244&port=85&secret=ee0000f00f0f775555fffffff5006e2e69646F776E6C6F61642E77696E646F77737570646174652E636F6D` |
| 5 | 77.238.253.117 | 443 | فعال | `tg://proxy?server=77.238.253.117&port=443&secret=7gffffffff_f_Adkb3dubG9hZC53aW5kb3dzdXBkYXRlLmNvbQ` |
| 6 | 128.140.67.68 | 53246 | فعال | `tg://proxy?server=128.140.67.68&port=53246&secret=1320PuNyHw_LQKT_Y7XNJw==` |
| 7 | 584.ir.ir.ir.ir.ir.zban-mas.info | 8888 | فعال | `tg://proxy?server=584.ir.ir.ir.ir.ir.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 8 | sadra.mygrade.ir | 443 | فعال | `tg://proxy?server=sadra.mygrade.ir&port=443&secret=7hYDAQIAAQAB_AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 9 | 62.60.177.143 | 8443 | فعال | `tg://proxy?server=62.60.177.143&port=8443&secret=FgMBAgABAAfwAwOG4kw63Q` |
| 10 | 151.244.85.15 | 70 | فعال | `tg://proxy?server=151.244.85.15&port=70&secret=7gffffffff_f_Adkb3dubG9hZC53aW5kb3dzdXBkYXRlLmNvbQ` |
| 11 | 178.130.42.116 | 443 | فعال | `tg://proxy?server=178.130.42.116&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 12 | irangodrati.co.uk. | 443 | فعال | `tg://proxy?server=irangodrati.co.uk.&port=443&secret=7s8J5YYVhvOdr-WqHy_58gVtZWRpYS5zdGVhbXBvd2VyZWQuY29t﻿` |
| 13 | hk-2.mtproto.vip | 54757 | فعال | `tg://proxy?server=hk-2.mtproto.vip&port=54757&secret=ee4b89fcd61d4535451014c168e1e922cb617a7572652e6d6963726f736f66742e636f6d` |
| 14 | 62.60.179.139 | 443 | فعال | `tg://proxy?server=62.60.179.139&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ` |
| 15 | cdn.sitemcinet.co.uk | 443 | فعال | `tg://proxy?server=cdn.sitemcinet.co.uk&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t)__` |
| 16 | Startup-active.custome-tobano.avadox-zhoan.info | 65 | فعال | `tg://proxy?server=Startup-active.custome-tobano.avadox-zhoan.info&port=65&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 17 | reverse.kambiz.dirbaz.flexfy.ir | 443 | فعال | `tg://proxy?server=reverse.kambiz.dirbaz.flexfy.ir&port=443&secret=ddd81a1e1c8d876b687d273cce8ed6c16e` |
| 18 | 91.99.206.83 | 70 | فعال | `tg://proxy?server=91.99.206.83&port=70&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0=` |
| 19 | 213.239.205.42 | 1460 | فعال | `tg://proxy?server=213.239.205.42&port=1460&secret=DDBighLLvXrFGRMCBVJdFQRueWVrdGFuZXQuY29t` |
| 20 | 31.58.134.131 | 443 | فعال | `tg://proxy?server=31.58.134.131&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |


> **توجه**: این جدول فقط برای نمایش نمونه‌ست. برای دسترسی به همه پروکسی‌های به‌روز، فایل [proxy.txt](proxy.txt) رو دانلود کنید.

## مشارکت
از مشارکت شما استقبال می‌کنیم! اگه ایده‌ای برای بهبود اسکریپت دارید یا می‌خواید منابع جدیدی اضافه کنید:
1. یه **Issue** تو مخزن باز کنید.
2. یا یه **Pull Request** با تغییرات پیشنهادی بفرستید.

## لایسنس
این پروژه تحت [لایسنس MIT](LICENSE) منتشر شده.

## لینک‌های مفید
- 📄 [لیست پروکسی‌ها](proxy.txt)
- 🚀 [وضعیت GitHub Actions](https://github.com/Poriya58p/telegram-proxy-scraper/actions)
- ⭐ [ما رو ستاره بدید!](https://github.com/Poriya58p/telegram-proxy-scraper)

## Stargazers در گذر زمان
[![Stargazers over time](https://starchart.cc/Poriya58p/telegram-proxy-scraper.svg?variant=adaptive)](https://starchart.cc/Poriya58p/telegram-proxy-scraper)

---

سپاس از استفاده از **Telegram Proxy Scraper**! اگه سؤالی دارید، تو بخش Issues مطرح کنید. 🌟
