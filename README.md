# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 19 July 2025, 01:41 UTC (به وقت ایران: 05:11)

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
| 1 | 91.99.178.113 | 70 | فعال | `tg://proxy?server=91.99.178.113&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d` |
| 2 | 213.239.205.42 | 1460 | فعال | `tg://proxy?server=213.239.205.42&port=1460&secret=DDBighLLvXrFGRMCBVJdFQRueWVrdGFuZXQuY29t` |
| 3 | 109.172.87.223 | 443 | فعال | `tg://proxy?server=109.172.87.223&port=443&secret=7td9tD7jch8Py0Ck_2O1zSdtZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 4 | 62.60.177.142 | 443 | فعال | `tg://proxy?server=62.60.177.142&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ` |
| 5 | rightel.irancell.irib.snapp.digikala.cloud.iranian.irib.ahmadp206.namli--binjzk.info | 666 | فعال | `tg://proxy?server=rightel.irancell.irib.snapp.digikala.cloud.iranian.irib.ahmadp206.namli--binjzk.info&port=666&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 6 | Iran.cdnhub.ir. | 443 | فعال | `tg://proxy?server=Iran.cdnhub.ir.&port=443&secret=7nlnZpKACGMvBKgv9kq9q-5waXJvb3ouc2lnbWFtZXNzZW5nZXIuY29t` |
| 7 | 9443.iropt-f.ir | 443 | فعال | `tg://proxy?server=9443.iropt-f.ir&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 8 | 91.99.226.187 | 155 | فعال | `https://t.me/proxy?server=91.99.226.187&port=155&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ` |
| 9 | 9891.Ir.ir.ir.ir.ir.zban-mas.info | 8888 | فعال | `tg://proxy?server=9891.Ir.ir.ir.ir.ir.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t__` |
| 10 | soos-turk.nuremborg-hamborg.dodos-codam.jojo19.ir | 443 | فعال | `tg://proxy?server=soos-turk.nuremborg-hamborg.dodos-codam.jojo19.ir&port=443&secret=7gD_AA___wD_9VVf______VtZWRpYS5zdGVhbXBvd2VyZWQuY29t)__` |
| 11 | 95.216.97.241 | 443 | فعال | `tg://proxy?server=95.216.97.241&port=443&secret=fd0068d5babf83266dadc790a20f6617` |
| 12 | 167.235.65.93 | 8888 | فعال | `tg://proxy?server=167.235.65.93&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 13 | 92782.meli.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=92782.meli.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 14 | 91.99.204.4 | 110 | فعال | `tg://proxy?server=91.99.204.4&port=110&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 15 | Berke.Wikimoon.sale | 443 | فعال | `tg://proxy?server=Berke.Wikimoon.sale&port=443&secret=7jK5IN_7UWQwKOL2uHjU6sFkbXl3ZWIuY2xvdWRmcm9udC5uZXQ](https://t.me/proxy?server=mofidonline.emofid.bourse24.moflidonline.mofiidonline.ir` |
| 16 | 87.248.132.70 | 155 | فعال | `https://t.me/proxy?server=87.248.132.70&port=155&secret=ee0000f00f0f775555fffffff5006e2e69646f776e6c6f61642e77696e646f77737570646174652e636f6d` |
| 17 | 62.60.179.18 | 155 | فعال | `tg://proxy?server=62.60.179.18&port=155&secret=dd1603010200010001fc030386e24c3add|[پروکسی` |
| 18 | 176.65.135.90 | 220 | فعال | `tg://proxy?server=176.65.135.90&port=220&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 19 | 87.248.132.44 | 200 | فعال | `tg://proxy?server=87.248.132.44&port=200&secret=79e344818749bd7ac519130220c25d09` |
| 20 | 79.172.228.13 | 443 | فعال | `tg://proxy?server=79.172.228.13&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |


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
