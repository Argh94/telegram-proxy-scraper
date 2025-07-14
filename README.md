# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 14 July 2025, 12:56 UTC (به وقت ایران: 16:26)

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
| 1 | 109.104.154.81 | 443 | فعال | `tg://proxy?server=109.104.154.81&port=443&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D**` |
| 2 | HAMRAH-AVAL.new-visioncity.ir. | 9741 | فعال | `tg://proxy?server=HAMRAH-AVAL.new-visioncity.ir.&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D)__` |
| 3 | 152.42.131.200 | 443 | فعال | `tg://proxy?server=152.42.131.200&port=443&secret=15115115115115115115115115115115` |
| 4 | 157.180.93.115 | 443 | فعال | `tg://proxy?server=157.180.93.115&port=443&secret=iORid5lJ237IiBMGYMQMdw==` |
| 5 | 147.182.130.96 | 155 | فعال | `tg://proxy?server=147.182.130.96&port=155&secret=7hURURURURURURURURURURVtZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 6 | 7477839.ir.ir.ir.ir.ir.zban-mas.info | 8888 | فعال | `tg://proxy?server=7477839.ir.ir.ir.ir.ir.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 7 | 157.180.67.240 | 443 | فعال | `tg://proxy?server=157.180.67.240&port=443&secret=7HQighJPBNMYVRNB6tdkVw==` |
| 8 | 37.27.89.14 | 81 | فعال | `tg://proxy?server=37.27.89.14&port=81&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 9 | cdn.sitemcinet.co.uk | 443 | فعال | `tg://proxy?server=cdn.sitemcinet.co.uk&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t)__` |
| 10 | 91.99.67.183 | 443 | فعال | `tg://proxy?server=91.99.67.183&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 11 | 193.3.190.50 | 85 | فعال | `tg://proxy?server=193.3.190.50&port=85&secret=ee0000f00f0f775555fffffff5006e2e69636861746770742e636f6d` |
| 12 | new-pio-iran-ck-uk-ir.zx2hgujoiah-xy1xutr021-2tk.com | 8443 | فعال | `tg://proxy?server=new-pio-iran-ck-uk-ir.zx2hgujoiah-xy1xutr021-2tk.com&port=8443&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0=` |
| 13 | 87.248.132.199 | 200 | فعال | `tg://proxy?server=87.248.132.199&port=200&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0=` |
| 14 | 135.181.10.214 | 443 | فعال | `https://t.me/proxy?server=135.181.10.214&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 15 | 140.233.187.210 | 443 | فعال | `tg://proxy?server=140.233.187.210&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d` |
| 16 | 93.88.205.35 | 85 | فعال | `tg://proxy?server=93.88.205.35&port=85&secret=7gAA8A8Pd1VV__9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 17 | 62.60.178.90 | 9741 | فعال | `tg://proxy?server=62.60.178.90&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d****` |
| 18 | 95.217.246.199 | 8888 | فعال | `https://t.me/proxy?server=95.217.246.199&port=8888&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA` |
| 19 | 87.248.134.204 | 443 | فعال | `tg://proxy?server=87.248.134.204&port=443&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 20 | 91.99.170.217 | 8888 | فعال | `tg://proxy?server=91.99.170.217&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |


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
