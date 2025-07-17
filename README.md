# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 17 July 2025, 18:36 UTC (به وقت ایران: 22:06)

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
  - [SoliSpirit/mtproto](https://raw.githubusercontent.com/SoliSpirit/mtproto/master/all_proxies.txt)
- **کانال‌های تلگرام**:
  - iporoto, HiProxy, iproxy, iRoProxy, proxyforopeta, IRN_Proxy, MProxy_ir, ProxyHagh, PyroProxy, ProxyMTProto, MTPro_XYZ, vpns, mtmvpn

## نمونه پروکسی‌ها
جدول زیر 20 پروکسی نمونه از فایل `proxy.txt` رو نشون می‌ده. برای کپی کردن لینک پروکسی، روی متن تو ستون "لینک پروکسی" لمس طولانی کنید و "Copy" رو انتخاب کنید:

| #  | سرور (Server)       | پورت (Port) | وضعیت     | لینک پروکسی                     |
|----|---------------------|-------------|-----------|---------------------------------|
| 1 | 157.180.80.209 | 443 | فعال | `tg://proxy?server=157.180.80.209&port=443&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 2 | 352678f9909af538.bytezs.ir | 443 | فعال | `tg://proxy?server=352678f9909af538.bytezs.ir&port=443&secret=7gcgcgcgcgcgcgcgcgcgcgd0cmFuc2xhdGUuZ29v)__` |
| 3 | Allow-more-english-support.kqmusic.ir. | 9741 | فعال | `https://t.me/proxy?server=Allow-more-english-support.kqmusic.ir.&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 4 | 9933.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=9933.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 5 | 87.248.134.12 | 70 | فعال | `tg://proxy?server=87.248.134.12&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D)__` |
| 6 | 91.99.226.187 | 155 | فعال | `https://t.me/proxy?server=91.99.226.187&port=155&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ` |
| 7 | 157.180.46.166 | 8888 | فعال | `tg://proxy?server=157.180.46.166&port=8888&secret=DD1603010200010001fc030386e24c3add` |
| 8 | 163.123.141.136 | 443 | فعال | `tg://proxy?server=163.123.141.136&port=443&secret=ddf900af441604263a084c1aa73af331ac` |
| 9 | cai7kkj46fbf.dop1000.com | 443 | فعال | `tg://proxy?server=cai7kkj46fbf.dop1000.com&port=443&secret=ee21ef372ec7034a96b00807b1ed45d42d636c7562686f7573652e7075626e75622e636f6d` |
| 10 | 91.84.106.140 | 443 | فعال | `tg://proxy?server=91.84.106.140&port=443&secret=d77db43ee3721f0fcb40a4ff63b5cd27` |
| 11 | 46.249.110.244 | 9741 | فعال | `tg://proxy?server=46.249.110.244&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 12 | 151.244.50.41 | 200 | فعال | `tg://proxy?server=151.244.50.41&port=200&secret=79e344818749bd7ac519130220c25d09` |
| 13 | Jocker-moker.garden-workeston.borsandowww.tic.ir.eldorado-feng.info. | 443 | فعال | `https://t.me/proxy?server=Jocker-moker.garden-workeston.borsandowww.tic.ir.eldorado-feng.info.&port=443&secret=7HQighJPBNMYVRNB6tdkVw==` |
| 14 | 45.67.139.20 | 8882 | فعال | `tg://proxy?server=45.67.139.20&port=8882&secret=eed700433aba3557d5e83d82beb4ab735873332e616d617a6f6e6177732e636f6d` |
| 15 | 23.88.70.165 | 443 | فعال | `tg://proxy?server=23.88.70.165&port=443&secret=EERighJJvXrFGRMCIMJdCQ==` |
| 16 | 88.99.248.184 | 443 | فعال | `tg://proxy?server=88.99.248.184&port=443&secret=EERighJJvXrFGRMCIMJdCQ` |
| 17 | 157.90.65.125 | 443 | فعال | `tg://proxy?server=157.90.65.125&port=443&secret=7gffffffff_f_Adkb3dubG9hZC53aW5kb3dzdXBkYXRlLmNvbQ` |
| 18 | 87.248.132.87 | 155 | فعال | `tg://proxy?server=87.248.132.87&port=155&secret=ee0000f00f0f775555fffffff5006e2e69646f776e6c6f61642e77696e646f77737570646174652e636f6d` |
| 19 | 212.34.139.251 | 443 | فعال | `tg://proxy?server=212.34.139.251&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 20 | 91.99.162.41 | 8888 | فعال | `tg://proxy?server=91.99.162.41&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |


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
