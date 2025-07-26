# 📊 نتایج استخراج: (آخرین بروزرسانی: 12:51 04-05-1404)

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License" />
  <img src="https://img.shields.io/badge/python-3.9-blue" alt="Python 3.9" />
  <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions Welcome" />
  <img src="https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg" alt="Proxy Scraper Workflow" />
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
  - [MhdiTaheri/ProxyCollector](https://raw.githubusercontent.com/MhdiTaheri/ProxyCollector/main/proxy.txt)
  - [SoliSpirit/mtproto](https://raw.githubusercontent.com/SoliSpirit/mtproto/master/all_proxies.txt)
- **کانال‌های تلگرام**:
  - iporoto, HiProxy, iproxy, iRoProxy, proxyforopeta, IRN_Proxy, MProxy_ir, ProxyHagh, PyroProxy, ProxyMTProto, MTPro_XYZ, vpns, mtmvpn, asr_proxy, proxyskyy

## 📈 نمونه پروکسی‌ها
جدول زیر نمونه‌ای از 20 پروکسی فعال از فایل `proxy.txt` را نمایش می‌دهد. برای استفاده، روی لینک پروکسی کلیک کنید یا آن را کپی کنید:

| # | سرور (Server) | پورت (Port) | وضعیت | لینک پروکسی |
|---|---------------|-------------|-------|-------------|
| 1 | `146.103.100.213` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=146.103.100.213&port=443&secret=eeNEgYdJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 2 | `151.244.42.18` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=151.244.42.18&port=443&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 3 | `daemi-pr.shesh-station.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=daemi-pr.shesh-station.ir&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 4 | `103.161.34.217` | `65` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=103.161.34.217&port=65&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `47.250.149.86` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=47.250.149.86&port=443&secret=ee0d99db994ed1ca453d83df742a2454ac617a7572652e6d6963726f736f66742e636f6d) |
| 6 | `66978828833.meli.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=66978828833.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 7 | `9288387882.meli.meli.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=9288387882.meli.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 8 | `bahbah.khoreshtsabzi.ir` | `8585` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bahbah.khoreshtsabzi.ir&port=8585&secret=dd5d5b15b207cd8974a5ae0585282bc510) |
| 9 | `176.65.131.165` | `85` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=176.65.131.165&port=85&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 10 | `arvan.irpower-g.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=arvan.irpower-g.ir&port=443&secret=7gffffffff___f___Adkb3dubG9hZC53aW5kb3dzdXBkYXRlLmNvbQ) |
| 11 | `65.108.255.94` | `155` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.108.255.94&port=155&secret=7otdyWf9v23L9+j4vrzGtv5OemY0WUxtZGg0T3NCcDUwNUFBMDUwMDEwMjAzMDQwNTA2MDcwODA5Li11cGRhdGUxLmFuZHJvaWQuZ29vZ2xlLnN5bmMuaW1hZ2UudG5hYmlzaWJpemlwLmly) |
| 12 | `IRAN.irpower-g.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=IRAN.irpower-g.ir&port=443&secret=ee07df7df7df7dfffffdfffffffffffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d) |
| 13 | `116.202.4.47` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=116.202.4.47&port=443&secret=0c30628212cbbd7ac519130205525d15) |
| 14 | `159.69.69.234` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=159.69.69.234&port=443&secret=EERighJJvXrFGRMCIMJdCQ==) |
| 15 | `ae.mohs1736.sbs` | `4637` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ae.mohs1736.sbs&port=4637&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 16 | `focos-mokos.berlino-landcvixo.yokohama-1borino.eromatic.ps-yari.ir.` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=focos-mokos.berlino-landcvixo.yokohama-1borino.eromatic.ps-yari.ir.&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ==) |
| 17 | `212.33.198.29` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=212.33.198.29&port=443&secret=7gAAAAAAAAAAAAAAAAAAAAl3d3cuY2xvdWRmbGFyZS5jb20) |
| 18 | `138.201.195.175` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=138.201.195.175&port=443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 19 | `one.homayoon19.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=one.homayoon19.ir&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d) |
| 20 | `dns.parsa-learning.ir.` | `333` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dns.parsa-learning.ir.&port=333&secret=7hAQEP8PSAZT____9QBuLmlpYS5zdGVhbXBvd2VyZWQuY29t)__) |


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
