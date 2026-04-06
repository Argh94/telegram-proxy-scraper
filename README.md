# 📊 نتایج استخراج: (آخرین بروزرسانی: 08:55 17-01-1405)

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
| 1 | `37.27.42.53` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=37.27.42.53&port=443&secret=ee400beecda94bbb22a7759357fd921c00636c6f7564666c6172652e636f6d) |
| 2 | `haughtily.mucous.obstetrical.overmaster.zoophile.rawisda.com` | `2290` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=haughtily.mucous.obstetrical.overmaster.zoophile.rawisda.com&port=2290&secret=a630d0df19b52481592a18016d266cf9) |
| 5 | `146.103.116.221` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=146.103.116.221&port=443&secret=3c9306bf0ab91b79fd23d57a521b79af) |
| 6 | `45.76.78.122` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.76.78.122&port=443&secret=3aa09f1f95c80c28caf844de0c022067) |
| 7 | `test.alotaxi.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=test.alotaxi.info&port=8443&secret=ee25773d1e79da8a2f549d1c38da5aae41626f6f6b696e672e636f6d) |
| 8 | `94.228.168.30` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=94.228.168.30&port=443&secret=ee8383301585e1f78b055c64165c824cad676f2e73616d706f2e7275) |
| 9 | `proxyobhod.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxyobhod.online&port=443&secret=71c30cc28759e0a10b6de5b471d69751) |
| 10 | `45.139.29.50` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.139.29.50&port=8443&secret=ddf672deb6dcac2f471e8ccffb1eacc82f) |
| 11 | `185.237.95.231` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.237.95.231&port=443&secret=ee4571396297582727452bf660db01b789676f6f676c652e636f6d) |
| 12 | `66.42.95.218` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=66.42.95.218&port=443&secret=477f1ffd983e734ea11647d47872d6d2) |
| 13 | `how.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=how.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 14 | `107.150.34.98` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=107.150.34.98&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 15 | `catholicity.gravely.pudgy.relaxed.scatterer.superpinoy.net` | `2400` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=catholicity.gravely.pudgy.relaxed.scatterer.superpinoy.net&port=2400&secret=c6e97411bd2f36aead173ff1b945c91e) |
| 17 | `2.26.97.0` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.26.97.0&port=8443&secret=f5a96ceadd1bbedd719fbd7f1c9387dd) |
| 18 | `107.150.34.99` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=107.150.34.99&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 20 | `tgproxy2.appav.net` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tgproxy2.appav.net&port=443&secret=8bf3a57e01e2d2c226113d338840793d) |


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
