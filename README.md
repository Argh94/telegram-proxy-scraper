# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 20 July 2025, 09:21 UTC (به وقت ایران: 12:51)

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
| 1 | 62.60.179.160 | 343 | فعال | `tg://proxy?server=62.60.179.160&port=343&secret=FgMBAgABAAfwAwOG4kw63Q` |
| 2 | jak-paris.homborg-hamborg.dodos-codam.jojo19.ir | 443 | فعال | `https://t.me/proxy?server=jak-paris.homborg-hamborg.dodos-codam.jojo19.ir&port=443&secret=7gD_AA___wD_9VVf______VtZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 3 | 14.102.10.39 | 888 | فعال | `tg://proxy?server=14.102.10.39&port=888&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 4 | 157.180.65.126 | 551 | فعال | `tg://proxy?server=157.180.65.126&port=551&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 5 | bib.bib.game.zx2hgujoiah-xy1xutr045-2tk.ir | 8443 | فعال | `tg://proxy?server=bib.bib.game.zx2hgujoiah-xy1xutr045-2tk.ir&port=8443&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0=` |
| 6 | 204.76.203.36 | 443 | فعال | `tg://proxy?server=204.76.203.36&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 7 | 109.104.154.207 | 443 | فعال | `tg://proxy?server=109.104.154.207&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t**` |
| 8 | 47.87.64.133 | 443 | فعال | `tg://proxy?server=47.87.64.133&port=443&secret=ee43e9a1e06d788f87e0b468e3f643448c617a7572652e6d6963726f736f66742e636f6d` |
| 9 | 4.link-a3.ir | 443 | فعال | `tg://proxy?server=4.link-a3.ir&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 10 | 140.233.187.98 | 443 | فعال | `tg://proxy?server=140.233.187.98&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d` |
| 11 | lan.fanlamona.info | 443 | فعال | `tg://proxy?server=lan.fanlamona.info&port=443&secret=ee151121451151121136221351161119152D2D2D2D2D2D7565622E61707063656E7465722E6D73692D2D2D2D2D2D` |
| 12 | www.hihim.sbs | 888 | فعال | `tg://proxy?server=www.hihim.sbs&port=888&secret=ee0c30628212cbbd7ac519130205525d1569612e737465616d706f77657265642e636f6d****` |
| 13 | 5.meli.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=5.meli.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t)__` |
| 14 | 185.95.159.251 | 9741 | فعال | `tg://proxy?server=185.95.159.251&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 15 | 157.180.43.253 | 8888 | فعال | `tg://proxy?server=157.180.43.253&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 16 | 213.239.207.75 | 155 | فعال | `tg://proxy?server=213.239.207.75&port=155&secret=1320PuNyHw_LQKT_Y7XNJw==` |
| 17 | 103.161.34.217 | 65 | فعال | `tg://proxy?server=103.161.34.217&port=65&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 18 | 91.99.125.231 | 48 | فعال | `tg://proxy?server=91.99.125.231&port=48&secret=7gAA8A8Pd1VV____9QBtLmlfbWVkaWEuc3RlYW0tcG93ZXJlZF8)__` |
| 19 | 81.12.96.203 | 1000 | فعال | `tg://proxy?server=81.12.96.203&port=1000&secret=ee4714faa05f25f39c7f1ddc4438110bd77777772e63626c6f756463646e2e636f6d` |
| 20 | ir.suggested.run. | 8888 | فعال | `https://t.me/proxy?server=ir.suggested.run.&port=8888&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA` |


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
