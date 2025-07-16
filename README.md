# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 16 July 2025, 20:17 UTC (به وقت ایران: 23:47)

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
| 1 | 65.21.177.171 | 100 | فعال | `tg://proxy?server=65.21.177.171&port=100&secret=c862057ba49a7ecdf0ad4eb44cd5bb11` |
| 2 | 185.117.0.110 | 8882 | فعال | `tg://proxy?server=185.117.0.110&port=8882&secret=7tcAQzq6NVfV6D2CvrSrc1hzMy5hbWF6b25hd3MuY29t` |
| 3 | 140.233.187.99 | 443 | فعال | `tg://proxy?server=140.233.187.99&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d` |
| 4 | 62.60.179.84 | 443 | فعال | `tg://proxy?server=62.60.179.84&port=443&secret=7hAQEP8PSAZT____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 5 | 91.99.194.148 | 443 | فعال | `tg://proxy?server=91.99.194.148&port=443&secret=ee151151151151151151151151151151156D656469612E737465616D706F77657265642E636F6D` |
| 6 | 14.102.10.169 | 8443 | فعال | `tg://proxy?server=14.102.10.169&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 7 | 37.27.204.149 | 8080 | فعال | `tg://proxy?server=37.27.204.149&port=8080&secret=7k0eee_00000__222-4tLXd3dy5zeG8tPQ==` |
| 8 | 62.60.176.132 | 443 | فعال | `tg://proxy?server=62.60.176.132&port=443&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 9 | Q3.opt-meli.info | 443 | فعال | `https://t.me/proxy?server=Q3.opt-meli.info&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 10 | 159.69.33.168 | 551 | فعال | `tg://proxy?server=159.69.33.168&port=551&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 11 | 87.248.132.188 | 155 | فعال | `tg://proxy?server=87.248.132.188&port=155&secret=eeNEgYdJvXrFGRMCIMJdCQ**` |
| 12 | 011010101101.noirc0re.online | 443 | فعال | `tg://proxy?server=011010101101.noirc0re.online&port=443&secret=35e1c63ac12a5ca4e2866c6e31a5b886` |
| 13 | 151.244.85.50 | 70 | فعال | `tg://proxy?server=151.244.85.50&port=70&secret=ee00ff000fffff00fff5555ffffffffff56D656469612E737465616D706F77657265642E636F6D` |
| 14 | 116.203.98.204 | 155 | فعال | `tg://proxy?server=116.203.98.204&port=155&secret=ee07df7df7df7dffdffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d` |
| 15 | 87.248.134.41 | 200 | فعال | `tg://proxy?server=87.248.134.41&port=200&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 16 | 85.133.214.37 | 8848 | فعال | `tg://proxy?server=85.133.214.37&port=8848&secret=ee91497bf49c81243ab60717929edb0009616a61782e31343832352e31302e646e732e31332e4c65696c6140333032302e7370656564746573742e6e6574` |
| 17 | my.parsa-learning.ir. | 443 | فعال | `https://t.me/proxy?server=my.parsa-learning.ir.&port=443&secret=7hAQEP8PSAZT____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 18 | 140.233.187.135 | 343 | فعال | `tg://proxy?server=140.233.187.135&port=343&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D)**` |
| 19 | 91.84.106.140 | 443 | فعال | `tg://proxy?server=91.84.106.140&port=443&secret=d77db43ee3721f0fcb40a4ff63b5cd27` |
| 20 | 157.180.94.178 | 8888 | فعال | `tg://proxy?server=157.180.94.178&port=8888&secret=FgMBAgABAAH8AwOG4kw63` |


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
