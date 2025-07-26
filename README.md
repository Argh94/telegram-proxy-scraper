# 📊 نتایج استخراج: (آخرین بروزرسانی: 01:33 05-05-1404)

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
| 1 | `810.55.198-44.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=810.55.198-44.ir&port=443&secret=7td9tD7jch8Py0Ck_2O1zSdtZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 2 | `62.60.179.72` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.60.179.72&port=8080&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 3 | `193.3.190.6` | `888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=193.3.190.6&port=888&secret=79e344818749bd7ac519130220c25d09) |
| 4 | `14.102.10.141` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=14.102.10.141&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 5 | `www.vsmusic.ir` | `888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.vsmusic.ir&port=888&secret=7gwwYoISy716xRkTAgVSXRVpYS5zdGVhbXBvd2VyZWQuY29t) |
| 6 | `185.117.0.116` | `8882` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.117.0.116&port=8882&secret=eed700433aba3557d5e83d82beb4ab735873332e616d617a6f6e6177732e636f6) |
| 7 | `87.248.132.67` | `200` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.132.67&port=200&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `62.60.179.221` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.60.179.221&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 9 | `212.34.132.116` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=212.34.132.116&port=443&secret=1320PuNyHw_LQKT_Y7XNJw==) |
| 10 | `91.134.57.71` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.134.57.71&port=443&secret=ee915818963f39435ebc8d07feb36afcb76564782e636f6d) |
| 11 | `arvan.irpower-g.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=arvan.irpower-g.ir&port=443&secret=ee07df7df7df7dfffffdfffffffffffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d|[پروکسی](https://t.me/proxy?server=NoVA.irpower-g.ir) |
| 12 | `91.99.150.26` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.99.150.26&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t)**) |
| 13 | `102.link-a2.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=102.link-a2.ir&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 14 | `62.60.178.216` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.60.178.216&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 15 | `45.93.170.26` | `3389` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.93.170.26&port=3389&secret=eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee31302e31302e33342e3336) |
| 16 | `62.60.176.58` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.60.176.58&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ) |
| 17 | `151.244.85.15` | `70` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=151.244.85.15&port=70&secret=7gffffffff) |
| 18 | `91.99.79.124` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.99.79.124&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 19 | `138.199.150.72` | `243` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=138.199.150.72&port=243&secret=79e462821249bd7ac519130220c25d09) |
| 20 | `185.157.213.77` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.157.213.77&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |


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
