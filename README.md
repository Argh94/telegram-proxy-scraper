# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 16 July 2025, 20:49 UTC (به وقت ایران: 00:19)

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
| 1 | 91.84.103.27 | 443 | فعال | `tg://proxy?server=91.84.103.27&port=443&secret=7gAA8A8Pd1VV____9QBuLmktLS8tLS8tLS8tLQ==` |
| 2 | 91.99.197.229 | 443 | فعال | `tg://proxy?server=91.99.197.229&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 3 | dns.geohost.ir. | 443 | فعال | `tg://proxy?server=dns.geohost.ir.&port=443&secret=7nlnZpKACGMvBKgv9kq9q-5hcGkua2FyZW5ob3N0Lmly` |
| 4 | 176.65.135.90 | 220 | فعال | `tg://proxy?server=176.65.135.90&port=220&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 5 | 91.99.179.12 | 443 | فعال | `tg://proxy?server=91.99.179.12&port=443&secret=ee151151151151151151151151151151156D656469612E737465616D706F77657265642E636F6D` |
| 6 | 176.65.135.55 | 23 | فعال | `tg://proxy?server=176.65.135.55&port=23&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 7 | 94.130.136.241 | 443 | فعال | `tg://proxy?server=94.130.136.241&port=443&secret=104462821249bd7ac519130220c25d09` |
| 8 | 7887711.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=7887711.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 9 | 95.217.91.25 | 443 | فعال | `https://t.me/proxy?server=95.217.91.25&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 10 | 157.180.83.102 | 85 | فعال | `tg://proxy?server=157.180.83.102&port=85&secret=eeRighJJvXrFGRMCIMJdCQ` |
| 11 | 356700.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=356700.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 12 | atish.bareh.shop.am-an.ciliptipiti.ir | 777 | فعال | `tg://proxy?server=atish.bareh.shop.am-an.ciliptipiti.ir&port=777&secret=7gD_AA_wD_9VVf____VtZWRtZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 13 | 8.217.215.214 | 443 | فعال | `tg://proxy?server=8.217.215.214&port=443&secret=ee2983fcb1a0fe12dd37451da609d13543617a7572652e6d6963726f736f66742e636f6d` |
| 14 | 213.145.71.117 | 70 | فعال | `tg://proxy?server=213.145.71.117&port=70&secret=7gffffffff_f_Adkb3dubG9hZC53aW5kb3dzdXBkYXRlLmNvbQ` |
| 15 | 62.60.179.21 | 443 | فعال | `tg://proxy?server=62.60.179.21&port=443&secret=eedddddddddddddddddddddddddddddddd6170617261742e636f6d` |
| 16 | 62.60.178.146 | 443 | فعال | `tg://proxy?server=62.60.178.146&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)`` |
| 17 | newdomain1.co.uk | 443 | فعال | `tg://proxy?server=newdomain1.co.uk&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 18 | 46.249.110.54 | 443 | فعال | `tg://proxy?server=46.249.110.54&port=443&secret=15115115115115115115115115115115)|` |
| 19 | 185.245.105.176 | 443 | فعال | `tg://proxy?server=185.245.105.176&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 20 | 5.223.44.107 | 6060 | فعال | `tg://proxy?server=5.223.44.107&port=6060&secret=EE79E344446D34D34D3FFFF11EE79E400079656B74616E65742D636F6D414141414141412D4141414135357676763535357635322D` |


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
