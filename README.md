# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 20 July 2025, 06:30 UTC (به وقت ایران: 10:00)

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
| 1 | Jocker-moker.garden-workeston.borsandowww.tic.ir.eldorado-feng.info. | 443 | فعال | `https://t.me/proxy?server=Jocker-moker.garden-workeston.borsandowww.tic.ir.eldorado-feng.info.&port=443&secret=7HQighJPBNMYVRNB6tdkVw==` |
| 2 | 62.60.177.198 | 443 | فعال | `tg://proxy?server=62.60.177.198&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 3 | 6.df.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.the_internet.brobalair.store | 8888 | فعال | `tg://proxy?server=6.df.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.the_internet.brobalair.store&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 4 | daemi1.fanar.info | 443 | فعال | `tg://proxy?server=daemi1.fanar.info&port=443&secret=FgMBAgABAAH8AwOG4kw63Q==` |
| 5 | mt.vip-server.ir | 1102 | فعال | `tg://proxy?server=mt.vip-server.ir&port=1102&secret=eeb85514a4f3c91ea2b1f0fce5bfbdbfed7376312e646967696b616c612e636f6d` |
| 6 | systemfull.gjesus.info | 443 | فعال | `tg://proxy?server=systemfull.gjesus.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d` |
| 7 | 93.88.205.36 | 85 | فعال | `tg://proxy?server=93.88.205.36&port=85&secret=7gAA8A8Pd1VV__9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 8 | AAAAA.210.63.168-55.ir | 9741 | فعال | `tg://proxy?server=AAAAA.210.63.168-55.ir&port=9741&secret=7u7u8A8Pd1VV____9QReLpZtZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 9 | 62.60.177.69 | 443 | فعال | `tg://proxy?server=62.60.177.69&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)__` |
| 10 | 79.172.228.82 | 70 | فعال | `tg://proxy?server=79.172.228.82&port=70&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D|[پروکسی](https://t.me/proxy?server=79.172.228.201` |
| 11 | 93.88.205.34 | 85 | فعال | `tg://proxy?server=93.88.205.34&port=85&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 12 | iran-vatan.magalaiash.info | 443 | فعال | `tg://proxy?server=iran-vatan.magalaiash.info&port=443&secret=7hYDAQIAAQAB_AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29t)__` |
| 13 | 37.49.224.204 | 8443 | فعال | `tg://proxy?server=37.49.224.204&port=8443&secret=eeb5e95ec1e6e2a27f9ca26fa2afe8abfa737465616D706F77657265642E636F6D` |
| 14 | 157.180.90.85 | 443 | فعال | `tg://proxy?server=157.180.90.85&port=443&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 15 | 138.201.51.101 | 8443 | فعال | `tg://proxy?server=138.201.51.101&port=8443&secret=DDBighLLvXrFGRMCBVJdFQ==` |
| 16 | Man-Iraniam.learn-csharp.ir | 9443 | فعال | `https://t.me/proxy?server=Man-Iraniam.learn-csharp.ir&port=9443&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA` |
| 17 | 140.233.187.210 | 443 | فعال | `tg://proxy?server=140.233.187.210&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d` |
| 18 | 87.229.100.230 | 70 | فعال | `tg://proxy?server=87.229.100.230&port=70&secret=ee07df7df7df7dfffffdfffffffffffc07646869646570726F78792E636C6F756466726F6E742E6E6574` |
| 19 | 62.60.176.235 | 443 | فعال | `tg://proxy?server=62.60.176.235&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)|` |
| 20 | Focos-mokos.berlino-landcvixo.yokohama-1borino.eromatic.info. | 443 | فعال | `https://t.me/proxy?server=Focos-mokos.berlino-landcvixo.yokohama-1borino.eromatic.info.&port=443&secret=iORid5lJ237IiBMGYMQMdw==` |


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
