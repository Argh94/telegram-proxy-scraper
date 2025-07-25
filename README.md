# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 25 July 2025, 01:45 UTC (به وقت ایران: 05:15)

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
| 1 | 95.217.77.168 | 443 | فعال | `tg://proxy?server=95.217.77.168&port=443&secret=7HQighJPBNMYVRNB6tdkVw` |
| 2 | 94.103.85.176 | 443 | فعال | `https://t.me/proxy?server=94.103.85.176&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 3 | vip2.abanol1.info | 70 | فعال | `tg://proxy?server=vip2.abanol1.info&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d)__` |
| 4 | 140.233.187.90 | 200 | فعال | `tg://proxy?server=140.233.187.90&port=200&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA)`|`` |
| 5 | 157.180.127.223 | 8888 | فعال | `tg://proxy?server=157.180.127.223&port=8888&secret=1603010200010001fc030386e24c3add` |
| 6 | 45.13.226.180 | 8882 | فعال | `tg://proxy?server=45.13.226.180&port=8882&secret=eed700433aba3557d5e83d82beb4ab735873332e616d617a6f6e6177732e636f6d` |
| 7 | 79.172.228.82 | 70 | فعال | `tg://proxy?server=79.172.228.82&port=70&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D|[پروکسی](https://t.me/proxy?server=79.172.228.201` |
| 8 | 47.250.149.86 | 443 | فعال | `tg://proxy?server=47.250.149.86&port=443&secret=ee0d99db994ed1ca453d83df742a2454ac617a7572652e6d6963726f736f66742e636f6d` |
| 9 | 116.202.83.133 | 404 | فعال | `tg://proxy?server=116.202.83.133&port=404&secret=eeNEgYdJvXrFGRMCIMJdCQ==` |
| 10 | 79.172.228.86 | 70 | فعال | `tg://proxy?server=79.172.228.86&port=70&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 11 | 151.244.85.66 | 85 | فعال | `tg://proxy?server=151.244.85.66&port=85&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 12 | abestick.abarwitch.info | 443 | فعال | `tg://proxy?server=abestick.abarwitch.info&port=443&secret=1603010200010001fc030386e24c3add` |
| 13 | 157.180.93.115 | 443 | فعال | `tg://proxy?server=157.180.93.115&port=443&secret=7HQighJPBNMYVRNB6tdkVw` |
| 14 | 151.244.42.20 | 70 | فعال | `tg://proxy?server=151.244.42.20&port=70&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 15 | e7.a27dh1.sbs | 8888 | فعال | `tg://proxy?server=e7.a27dh1.sbs&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 16 | new-pio-iran-ck-uk-ir.zx2hgujoiah-xy1xutr021-2tk.com | 8443 | فعال | `tg://proxy?server=new-pio-iran-ck-uk-ir.zx2hgujoiah-xy1xutr021-2tk.com&port=8443&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0=` |
| 17 | 62.60.179.227 | 9880 | فعال | `tg://proxy?server=62.60.179.227&port=9880&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 18 | 94.130.218.244 | 443 | فعال | `tg://proxy?server=94.130.218.244&port=443&secret=104462821249bd7ac519130220c25d09` |
| 19 | 62.60.179.109 | 443 | فعال | `tg://proxy?server=62.60.179.109&port=443&secret=7hAQEP8PSAZT____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 20 | 65.109.170.104 | 100 | فعال | `tg://proxy?server=65.109.170.104&port=100&secret=c862057ba49a7ecdf0ad4eb44cd5bb11` |


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
