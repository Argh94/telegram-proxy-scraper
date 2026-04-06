# 📊 نتایج استخراج: (آخرین بروزرسانی: 13:40 17-01-1405)

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License" />
  <img src="https://img.shields.io/badge/python-3.9-blue" alt="Python 3.9" />
  <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions Welcome" />
  <img src="https://img.shields.io/badge/Proxy%20Scraper-Running-green" alt="Proxy Scraper" />
  <img src="https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/main.yml/badge.svg" alt="Proxy Scraper Workflow" />
  <img src="https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper" alt="GitHub Last Commit" />
  <img src="https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper" alt="GitHub Issues" />
</p>

این پروژه یک اسکریپت پایتون برای جمع‌آوری خودکار پروکسی‌های MTProto تلگرام از منابع متنی و کانال‌های تلگرام است. پروکسی‌ها در فایل `proxy.txt` ذخیره می‌شوند و هر 3 ساعت به‌صورت خودکار به‌روزرسانی می‌شوند.

## ✨ درباره پروژه

این اسکریپت با استفاده از `requests` برای منابع متنی و `selenium` برای کانال‌های تلگرام، پروکسی‌های MTProto را جمع‌آوری می‌کند. پروکسی‌های تکراری حذف شده و نتایج در فایل `proxy.txt` ذخیره می‌شوند. این فرآیند به‌صورت خودکار با **GitHub Actions** هر 3 ساعت اجرا می‌شود.

## 🚀 ویژگی‌ها
- 🌐 جمع‌آوری پروکسی از منابع متنی و کانال‌های تلگرام
- 🔄 به‌روزرسانی خودکار هر 3 ساعت
- 🗑 حذف پروکسی‌های تکراری
- 🔑 بدون نیاز به API تلگرام
- 📱 مناسب برای کاربران در جستجوی پروکسی‌های فعال MTProto

## 📋 پیش‌نیازها
- 🐍 پایتون 3.9
- 📦 کتابخانه‌های مورد نیاز: `requests`, `beautifulsoup4`, `selenium`, `pytz`, `jdatetime`
- نصب وابستگی‌ها با: `pip install -r requirements.txt`

## 🛠 نحوه استفاده
1. فایل `proxy.txt` را از [اینجا](proxy.txt) دانلود کنید.
2. لینک‌های پروکسی (با فرمت `tg://proxy?...` یا `https://t.me/proxy?...`) را در کلاینت تلگرام وارد کنید.
3. در جدول زیر، روی لینک‌های ستون **لینک پروکسی** کلیک کنید تا به تلگرام هدایت شوید یا لینک را کپی کنید.
4. برای به‌روزرسانی دستی، به تب **Actions** در مخزن بروید و روی **Run workflow** کلیک کنید.

## 🌍 منابع پروکسی
- **منابع متنی**:
  - [MahsaNetConfigTopic](https://raw.githubusercontent.com/MahsaNetConfigTopic/proxy/main/proxies.txt)
  - [MhdiTaheri](https://raw.githubusercontent.com/MhdiTaheri/ProxyCollector/main/proxy.txt)
  - [SoliSpirit/mtproto](https://raw.githubusercontent.com/SoliSpirit/mtproto/master/all_proxies.txt)
  - [hookzof/socks5_list](https://raw.githubusercontent.com/hookzof/socks5_list/master/tg/mtproto.json)
- **کانال‌های تلگرام**:
  - iporoto, HiProxy, iproxy, iRoProxy, proxyforopeta, IRN_Proxy, MProxy_ir, ProxyHagh, PyroProxy, ProxyMTProto, MTPro_XYZ, vpns, mtmvpn, asr_proxy, proxyskyy

## 📈 نمونه پروکسی‌ها
جدول زیر نمونه‌ای از 20 پروکسی فعال از فایل `proxy.txt` را نمایش می‌دهد. برای استفاده، روی لینک پروکسی کلیک کنید یا آن را کپی کنید:

| # | سرور (Server) | پورت (Port) | وضعیت | لینک پروکسی |
|---|---------------|-------------|-------|-------------|
| 2 | `proxy-01-moonlumevpn.duckdns.org` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy-01-moonlumevpn.duckdns.org&port=443&secret=ee117d17b72cd2415e00cafacdf68ded627777772e676f6f676c652e636f6d) |
| 3 | `47.76.77.155` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=47.76.77.155&port=8888&secret=dd9035de6b150c249f1b6f7156092757b4) |
| 5 | `64.188.64.189` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=64.188.64.189&port=443&secret=b0834f5c52129b3de4fed01625bb8567) |
| 6 | `176.123.166.255` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=176.123.166.255&port=443&secret=dd7c5d4e1f2a3b9c8d7e6f5a4b3c2d1e0f) |
| 7 | `tg.hellohiro.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.hellohiro.ru&port=8443&secret=dd973e178b06e6b204a3f6d8044dda69c7) |
| 8 | `107.150.34.98` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=107.150.34.98&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 9 | `tg.servervless.ru` | `9443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.servervless.ru&port=9443&secret=0867e1b95cc9aa87049f7d68fa83760d) |
| 10 | `107.150.34.101` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=107.150.34.101&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 11 | `142.54.189.108` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=142.54.189.108&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 12 | `185.174.137.50` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.174.137.50&port=8443&secret=676c4049812b842b7792954bf2a32943) |
| 13 | `tg.safepal.life` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.safepal.life&port=443&secret=094d1e6d9047716b1672fc5560683bfd) |
| 14 | `47.76.185.250` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=47.76.185.250&port=8888&secret=ddbc333021b477f9f51080ec9f6e9f5ef3) |
| 15 | `tgproxy2.appav.net` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tgproxy2.appav.net&port=443&secret=8bf3a57e01e2d2c226113d338840793d) |
| 16 | `dowd.sportsmanship.steeplechaser.thy.urceolate.kapitoshka.info` | `15417` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dowd.sportsmanship.steeplechaser.thy.urceolate.kapitoshka.info&port=15417&secret=d6db8ab62ff9b9f70f6ca15ccb98c222) |
| 17 | `test.alotaxi.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=test.alotaxi.info&port=8443&secret=ee25773d1e79da8a2f549d1c38da5aae41626f6f6b696e672e636f6d) |
| 18 | `142.54.189.110` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=142.54.189.110&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 19 | `195.254.165.243` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.243&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 20 | `49.12.116.16` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=49.12.116.16&port=443&secret=dd104462821249bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.

## 🤝 مشارکت
از ایده‌ها و مشارکت شما استقبال می‌کنیم! برای بهبود پروژه:
1. یک **Issue** در مخزن باز کنید.
2. یا یک **Pull Request** با تغییرات پیشنهادی ارسال کنید.

## 📜 لایسنس
این پروژه تحت [لایسنس MIT](https://github.com/Argh94/telegram-proxy-scraper/blob/main/Files/LISENSE) منتشر شده است.

## 🔗 لینک‌های مفید
- 📄 [لیست پروکسی‌ها](proxy.txt)
- 🚀 [وضعیت GitHub Actions](https://github.com/Argh94/telegram-proxy-scraper/actions)
- ⭐ [ما را ستاره دهید!](https://github.com/Argh94/telegram-proxy-scraper)

## 📊 Stargazers در گذر زمان
<p align="center">
  <img src="https://starchart.cc/Argh94/telegram-proxy-scraper.svg?variant=adaptive" alt="Stargazers over time" />
</p>

---

🌟 **سپاس از استفاده از Telegram Proxy Scraper!** اگر سؤالی دارید، در بخش Issues مطرح کنید.
