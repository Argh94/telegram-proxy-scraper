# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 14 July 2025, 02:20 UTC (به وقت ایران: 05:50)

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
| 1 | 62.60.177.150 | 9741 | فعال | `tg://proxy?server=62.60.177.150&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 2 | hight-opt.irpower-a.ir | 443 | فعال | `tg://proxy?server=hight-opt.irpower-a.ir&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 3 | 185.10.19.214 | 85 | فعال | `tg://proxy?server=185.10.19.214&port=85&secret=eec3c91d2178694563acb01e6f24757b757a756c612e6972` |
| 4 | 164.90.150.61 | 8443 | فعال | `tg://proxy?server=164.90.150.61&port=8443&secret=ee151151151151151151151151151151157777772e6170706c652e636f6d` |
| 5 | 138.199.150.72 | 243 | فعال | `tg://proxy?server=138.199.150.72&port=243&secret=eeRighJJvXrFGRMCIMJdCQ` |
| 6 | 157.180.93.115 | 443 | فعال | `tg://proxy?server=157.180.93.115&port=443&secret=ec742282124f04d318551341ead76457` |
| 7 | 204.76.203.15 | 443 | فعال | `tg://proxy?server=204.76.203.15&port=443&secret=15115115115115115115115115115115` |
| 8 | 45.79.149.31 | 443 | فعال | `tg://proxy?server=45.79.149.31&port=443&secret=ee0000f00f0f775555fffffff6006e2e697777772e77696b6970656469612e6f7267` |
| 9 | 140.233.187.82 | 4030 | فعال | `tg://proxy?server=140.233.187.82&port=4030&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 10 | vip.abanol1.info | 70 | فعال | `tg://proxy?server=vip.abanol1.info&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d` |
| 11 | 109.172.87.223 | 443 | فعال | `tg://proxy?server=109.172.87.223&port=443&secret=7td9tD7jch8Py0Ck_2O1zSdtZWRpYS5zdGVhb` |
| 12 | 62.60.177.42 | 343 | فعال | `tg://proxy?server=62.60.177.42&port=343&secret=FgMBAgABAAfwAwOG4kw63QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.` |
| 13 | 1.2.3.4-5-6-7-8-9.ir | 155 | فعال | `tg://proxy?server=1.2.3.4-5-6-7-8-9.ir&port=155&secret=7ggggggggggggggggggggggtLXd-Z28tLS0=` |
| 14 | 62.60.176.188 | 443 | فعال | `tg://proxy?server=62.60.176.188&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D)‌|‌[همراه](https://t.me/proxy?server=62.60.176.197` |
| 15 | 213.176.94.18 | 443 | فعال | `tg://proxy?server=213.176.94.18&port=443&secret=ee151151151151151151151151151151156D656469612E737465616D706F77657265642E636F6D` |
| 16 | 5.255.111.230 | 443 | فعال | `tg://proxy?server=5.255.111.230&port=443&secret=7u0h9W68_BTpDShqHaz086xzMy5hbWF6b25hd3MuY29t` |
| 17 | 37.27.204.149 | 8080 | فعال | `tg://proxy?server=37.27.204.149&port=8080&secret=7k0eee___00000____222-4tLXd3dy5zeG8tPQ==)__` |
| 18 | 62.60.177.195 | 9741 | فعال | `tg://proxy?server=62.60.177.195&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6dhjkkjtredxgjk` |
| 19 | 140.233.187.128 | 8080 | فعال | `tg://proxy?server=140.233.187.128&port=8080&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d` |
| 20 | 87.248.132.199 | 200 | فعال | `tg://proxy?server=87.248.132.199&port=200&secret=eeNEgYdJvXrFGRMCIMJdCQ` |


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
