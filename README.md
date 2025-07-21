# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 21 July 2025, 01:50 UTC (به وقت ایران: 05:20)

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
| 1 | plus.time-meli.info | 443 | فعال | `https://t.me/proxy?server=plus.time-meli.info&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 2 | 138.201.138.104 | 9110 | فعال | `tg://proxy?server=138.201.138.104&port=9110&secret=DDBighLLvXrFGRMCBVJdFQRueWVrdGFuZXQuY29t` |
| 3 | iran-vatan.magalaiash.info | 443 | فعال | `tg://proxy?server=iran-vatan.magalaiash.info&port=443&secret=7hYDAQIAAQAB_AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 4 | reverse.kambiz.dirbaz.flexfy.ir | 443 | فعال | `tg://proxy?server=reverse.kambiz.dirbaz.flexfy.ir&port=443&secret=ddd81a1e1c8d876b687d273cce8ed6c16e` |
| 5 | 5.link-a3.ir | 443 | فعال | `tg://proxy?server=5.link-a3.ir&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 6 | 46.62.143.95 | 155 | فعال | `tg://proxy?server=46.62.143.95&port=155&secret=ee07df7df7df7dffdffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d` |
| 7 | 178.20.43.19 | 443 | فعال | `https://t.me/proxy?server=178.20.43.19&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 8 | 157.180.31.92 | 443 | فعال | `tg://proxy?server=157.180.31.92&port=443&secret=1603010200010001fc030386e24c3add` |
| 9 | Komatso-Japan.www.google.com.ganool-com.info | 300 | فعال | `https://t.me/proxy?server=Komatso-Japan.www.google.com.ganool-com.info&port=300&secret=eeRigzNJvXrFGRMCIMJdEARueWVrdGFuZXQuY29tZmFyYTrhdi5jb212YZ6ubmFqXeEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA` |
| 10 | 5.35.70.114 | 443 | فعال | `tg://proxy?server=5.35.70.114&port=443&secret=ee07df7df7df7dfffffdfffffffffffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d)|[پروکسی](https://t.me/proxy?server=91.84.107.88` |
| 11 | 62.60.179.92 | 443 | فعال | `tg://proxy?server=62.60.179.92&port=443&secret=7hAQEP8PSAZT____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 12 | 62.60.177.121 | 343 | فعال | `tg://proxy?server=62.60.177.121&port=343&secret=FgMBAgABAAfwAwOG4kw63Q` |
| 13 | ryzen-gold.shesh-station.ir | 443 | فعال | `tg://proxy?server=ryzen-gold.shesh-station.ir&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d` |
| 14 | 45.129.199.5 | 443 | فعال | `tg://proxy?server=45.129.199.5&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 15 | 5.35.70.114 | 443 | فعال | `tg://proxy?server=5.35.70.114&port=443&secret=ee07df7df7df7dfffffdfffffffffffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d` |
| 16 | 14.102.10.34 | 888 | فعال | `tg://proxy?server=14.102.10.34&port=888&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 17 | 159.69.83.188 | 8080 | فعال | `tg://proxy?server=159.69.83.188&port=8080&secret=7gggggggggggggg______-4tdy5nby0=)__` |
| 18 | 91.99.195.241 | 69 | فعال | `tg://proxy?server=91.99.195.241&port=69&secret=7pVZ3VtL_Wuy49KeR-ZTRlB3d3cuc3BlZWR0ZXN0Lm5ldA==` |
| 19 | jak-paris.homborg-hamborg.dodos-codam.jojo19.ir | 443 | فعال | `tg://proxy?server=jak-paris.homborg-hamborg.dodos-codam.jojo19.ir&port=443&secret=7gD_AA___wD_9VVf______VtZWRpYS5zdGVhbXBvd2VyZWQuY29t)__` |
| 20 | wunixasdwx.proo2.milxbywkaiwnx.xyz | 350 | فعال | `tg://proxy?server=wunixasdwx.proo2.milxbywkaiwnx.xyz&port=350&secret=ddd1cf87d4e4c33d46652605ef24d6bcef` |


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
