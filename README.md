# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 18 July 2025, 12:43 UTC (به وقت ایران: 16:13)

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
| 1 | cdn.sitemcinet.co.uk | 443 | فعال | `https://t.me/proxy?server=cdn.sitemcinet.co.uk&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 2 | lan.fanlamona.info | 443 | فعال | `tg://proxy?server=lan.fanlamona.info&port=443&secret=ee151121451151121136221351161119152D2D2D2D2D2D7565622E61707063656E7465722E6D73692D2D2D2D2D2D` |
| 3 | sitemcinet.co.uk | 443 | فعال | `https://t.me/proxy?server=sitemcinet.co.uk&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 4 | newdomain1.co.uk | 443 | فعال | `https://t.me/proxy?server=newdomain1.co.uk&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 5 | 185.117.0.135 | 8882 | فعال | `tg://proxy?server=185.117.0.135&port=8882&secret=eed700433aba3557d5e83d82beb4ab735873332e616d617a6f6e6177732e636f6d` |
| 6 | 87.248.132.53 | 200 | فعال | `tg://proxy?server=87.248.132.53&port=200&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 7 | mas.a27dh1.sbs | 8888 | فعال | `tg://proxy?server=mas.a27dh1.sbs&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 8 | 151.244.85.26 | 70 | فعال | `tg://proxy?server=151.244.85.26&port=70&secret=7gffffffff_f_Adkb3dubG9hZC53aW5kb3dzdXBkYXRlLmNvbQ` |
| 9 | 95.216.22.207 | 443 | فعال | `tg://proxy?server=95.216.22.207&port=443&secret=iORid5lJ237IiBMGYMQMdw` |
| 10 | 62.60.176.139 | 9741 | فعال | `tg://proxy?server=62.60.176.139&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 11 | e7777.zban-mas.info | 8888 | فعال | `tg://proxy?server=e7777.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 12 | 193.3.190.47 | 85 | فعال | `tg://proxy?server=193.3.190.47&port=85&secret=7gAA8A8Pd1VV____9QBuLmljaGF0Z3B0LmNvbQ==` |
| 13 | ae.mohs1736.sbs | 4637 | فعال | `tg://proxy?server=ae.mohs1736.sbs&port=4637&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t)__` |
| 14 | 46.62.154.53 | 55 | فعال | `https://t.me/proxy?server=46.62.154.53&port=55&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 15 | 151.244.42.19 | 85 | فعال | `tg://proxy?server=151.244.42.19&port=85&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 16 | Drop.Cphosting.Shop. | 443 | فعال | `tg://proxy?server=Drop.Cphosting.Shop.&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t)__` |
| 17 | syczleck.itemag.ir | 443 | فعال | `tg://proxy?server=syczleck.itemag.ir&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d)__` |
| 18 | caeca135e871f492.bytezs.ir | 443 | فعال | `tg://proxy?server=caeca135e871f492.bytezs.ir&port=443&secret=7gcgcgcgcgcgcgcgcgcgcgd0cmFuc2xhdGUuZ29v)__` |
| 19 | 62.60.179.150 | 343 | فعال | `tg://proxy?server=62.60.179.150&port=343&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d` |
| 20 | 87.229.100.251 | 443 | فعال | `tg://proxy?server=87.229.100.251&port=443&secret=eeRighJJvXrFGRMCIMJdCQ` |


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
