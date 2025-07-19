# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 19 July 2025, 18:28 UTC (به وقت ایران: 21:58)

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
| 1 | 14.102.10.38 | 888 | فعال | `tg://proxy?server=14.102.10.38&port=888&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 2 | 159.253.2.4 | 300 | فعال | `tg://proxy?server=159.253.2.4&port=300&secret=EE0C30628212cbbd7ac519130205525d1569612e737465616d706f77657265642e636f6DD` |
| 3 | NoVA.irpower-g.ir | 443 | فعال | `tg://proxy?server=NoVA.irpower-g.ir&port=443&secret=ee07df7df7df7dfffffdfffffffffffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d` |
| 4 | 176.65.136.180 | 443 | فعال | `tg://proxy?server=176.65.136.180&port=443&secret=ee151151151151151151151151151151156d656469612e737465616d706f77657265642e636f6d` |
| 5 | 87.248.134.172 | 443 | فعال | `https://t.me/proxy?server=87.248.134.172&port=443&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 6 | 87.248.132.39 | 85 | فعال | `tg://proxy?server=87.248.132.39&port=85&secret=ee0000f00f0f775555fffffff5006e2e69646F776E6C6F61642E77696E646F77737570646174652E636F6D` |
| 7 | 195.200.18.147 | 443 | فعال | `tg://proxy?server=195.200.18.147&port=443&secret=ee07df7df7df7dfffffdfffffffffffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d` |
| 8 | load.link-a4.ir | 443 | فعال | `tg://proxy?server=load.link-a4.ir&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 9 | 87.248.132.56 | 200 | فعال | `tg://proxy?server=87.248.132.56&port=200&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 10 | Berke.Wikimoon.sale | 443 | فعال | `tg://proxy?server=Berke.Wikimoon.sale&port=443&secret=7jK5IN_7UWQwKOL2uHjU6sFkbXl3ZWIuY2xvdWRmcm9udC5uZXQ` |
| 11 | 91.99.236.24 | 4637 | فعال | `https://t.me/proxy?server=91.99.236.24&port=4637&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 12 | 109.107.167.113 | 443 | فعال | `tg://proxy?server=109.107.167.113&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWR1aS5jb20` |
| 13 | 176.65.128.51 | 155 | فعال | `tg://proxy?server=176.65.128.51&port=155&secret=ee07df7df7df7dffdffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d` |
| 14 | 91.99.172.214 | 8888 | فعال | `tg://proxy?server=91.99.172.214&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29` |
| 15 | 193.109.120.106 | 443 | فعال | `tg://proxy?server=193.109.120.106&port=443&secret=ee100404ff0f48064fffffff9001b8696d696d656469612e737465616d706f77657265642e636f6d` |
| 16 | 9494.Ir.ir.ir.ir.ir.zban-mas.info | 8888 | فعال | `tg://proxy?server=9494.Ir.ir.ir.ir.ir.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t____` |
| 17 | 193.3.190.51 | 85 | فعال | `tg://proxy?server=193.3.190.51&port=85&secret=7gAA8A8Pd1VV____9QBuLmljaGF0Z3B0LmNvbQ` |
| 18 | 151.244.85.158 | 70 | فعال | `tg://proxy?server=151.244.85.158&port=70&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 19 | 4.df.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.the_internet.brobalair.store | 8888 | فعال | `tg://proxy?server=4.df.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.the_internet.brobalair.store&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 20 | 151.244.42.8 | 443 | فعال | `tg://proxy?server=151.244.42.8&port=443&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |


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
