# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 17 July 2025, 06:31 UTC (به وقت ایران: 10:01)

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
| 1 | 62.60.179.157 | 343 | فعال | `tg://proxy?server=62.60.179.157&port=343&secret=FgMBAgABAAfwAwOG4kw63Q` |
| 2 | SIGNAL.irpower-b.ir | 443 | فعال | `tg://proxy?server=SIGNAL.irpower-b.ir&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 3 | 37.27.223.70 | 81 | فعال | `tg://proxy?server=37.27.223.70&port=81&secret=eef5aa7dc289c8126ef66ac2e262517f846d656469612e737465616d706f77657265642e636f6d` |
| 4 | 151.244.85.15 | 70 | فعال | `tg://proxy?server=151.244.85.15&port=70&secret=7gffffffff___f_______Adkb3dubG9hZC53aW5kb3dzdXBkYXRlLmNvbQ==` |
| 5 | 14.102.10.129 | 8443 | فعال | `tg://proxy?server=14.102.10.129&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 6 | 87.248.132.34 | 70 | فعال | `tg://proxy?server=87.248.132.34&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 7 | response.cinere.info | 443 | فعال | `tg://proxy?server=response.cinere.info&port=443&secret=7hYDAQIAAQAB_AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 8 | hk-2.mtproto.vip | 54757 | فعال | `tg://proxy?server=hk-2.mtproto.vip&port=54757&secret=ee4b89fcd61d4535451014c168e1e922cb617a7572652e6d6963726f736f66742e636f6d` |
| 9 | 142.132.199.239 | 8443 | فعال | `tg://proxy?server=142.132.199.239&port=8443&secret=DDBighLLvXrFGRMCBVJdFQ==` |
| 10 | dl.bahalbax.ir. | 443 | فعال | `tg://proxy?server=dl.bahalbax.ir.&port=443&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0` |
| 11 | rightel.irancell.irib.snapp.digikala.cloud.iranian.irib.ahmadp206.namli--binjzk.info | 666 | فعال | `tg://proxy?server=rightel.irancell.irib.snapp.digikala.cloud.iranian.irib.ahmadp206.namli--binjzk.info&port=666&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 12 | 94.130.136.241 | 443 | فعال | `tg://proxy?server=94.130.136.241&port=443&secret=EERighJJvXrFGRMCIMJdCQ==` |
| 13 | 91.99.170.203 | 888 | فعال | `tg://proxy?server=91.99.170.203&port=888&secret=ee0c30628212cbbd7ac519130205525d1569612e737465616d706f77657265642e636f6d` |
| 14 | 95.164.119.4 | 155 | فعال | `tg://proxy?server=95.164.119.4&port=155&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 15 | 87.248.132.53 | 200 | فعال | `tg://proxy?server=87.248.132.53&port=200&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 16 | 87.248.132.199 | 200 | فعال | `tg://proxy?server=87.248.132.199&port=200&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 17 | net-meli.bozorgavar-game.ir. | 9741 | فعال | `tg://proxy?server=net-meli.bozorgavar-game.ir.&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 18 | 62.60.176.59 | 443 | فعال | `tg://proxy?server=62.60.176.59&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ` |
| 19 | systemfull.gjesus.info | 443 | فعال | `tg://proxy?server=systemfull.gjesus.info&port=443&secret=7hYDAQIAAQAB_AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29t)__` |
| 20 | 62.60.177.165 | 8443 | فعال | `tg://proxy?server=62.60.177.165&port=8443&secret=FgMBAgABAAfwAwOG4kw63Q` |


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
