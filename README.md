# 📊 نتایج استخراج: (آخرین بروزرسانی: 01:41 04-05-1404)

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
  - [ALIILAPRO/MTProtoProxy](https://raw.githubusercontent.com/ALIILAPRO/MTProtoProxy/main/proxy-list.txt)
  - [MhdiTaheri/ProxyCollector](https://raw.githubusercontent.com/MhdiTaheri/ProxyCollector/main/proxy.txt)
  - [SoliSpirit/mtproto](https://raw.githubusercontent.com/SoliSpirit/mtproto/master/all_proxies.txt)
- **کانال‌های تلگرام**:
  - iporoto, HiProxy, iproxy, iRoProxy, proxyforopeta, IRN_Proxy, MProxy_ir, ProxyHagh, PyroProxy, ProxyMTProto, MTPro_XYZ, vpns, mtmvpn, asr_proxy, proxyskyy

## 📈 نمونه پروکسی‌ها
جدول زیر نمونه‌ای از 20 پروکسی فعال از فایل `proxy.txt` را نمایش می‌دهد. برای استفاده، روی لینک پروکسی کلیک کنید یا آن را کپی کنید:

| # | سرور (Server) | پورت (Port) | وضعیت | لینک پروکسی |
|---|---------------|-------------|-------|-------------|
| 1 | `200.meli.zban-mas.info` | `8888` | ✅ فعال | [tg://proxy?server=200.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t](tg://proxy?server=200.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 2 | `185.222.28.153` | `23` | ✅ فعال | [tg://proxy?server=185.222.28.153&port=23&secret=1320PuNyHw_LQKT_Y7XNJw==](tg://proxy?server=185.222.28.153&port=23&secret=1320PuNyHw_LQKT_Y7XNJw==) |
| 3 | `87.229.100.234` | `7777` | ✅ فعال | [tg://proxy?server=87.229.100.234&port=7777&secret=eeRighJJvXrFGRMCIMJdCQ](tg://proxy?server=87.229.100.234&port=7777&secret=eeRighJJvXrFGRMCIMJdCQ) |
| 4 | `95.217.91.27` | `443` | ✅ فعال | [tg://proxy?server=95.217.91.27&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t****](tg://proxy?server=95.217.91.27&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t****) |
| 5 | `91.107.241.252` | `443` | ✅ فعال | [tg://proxy?server=91.107.241.252&port=443&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0](tg://proxy?server=91.107.241.252&port=443&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0) |
| 6 | `62.60.178.185` | `443` | ✅ فعال | [tg://proxy?server=62.60.178.185&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ](tg://proxy?server=62.60.178.185&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ) |
| 7 | `6.meli.zban-mas.info` | `8888` | ✅ فعال | [tg://proxy?server=6.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t)__](tg://proxy?server=6.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t)__) |
| 8 | `109.172.84.78` | `443` | ✅ فعال | [tg://proxy?server=109.172.84.78&port=443&secret=7td9tD7jch8Py0Ck_2O1zSdtZWRpYS5zdGVhbXBvd2VyZWQuY29t](tg://proxy?server=109.172.84.78&port=443&secret=7td9tD7jch8Py0Ck_2O1zSdtZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 9 | `45.67.139.20` | `8882` | ✅ فعال | [tg://proxy?server=45.67.139.20&port=8882&secret=eed700433aba3557d5e83d82beb4ab735873332e616d617a6f6e6177732e636f6d](tg://proxy?server=45.67.139.20&port=8882&secret=eed700433aba3557d5e83d82beb4ab735873332e616d617a6f6e6177732e636f6d) |
| 10 | `206.189.29.108` | `443` | ✅ فعال | [tg://proxy?server=206.189.29.108&port=443&secret=1320PuNyHw_LQKT_Y7XNJw==](tg://proxy?server=206.189.29.108&port=443&secret=1320PuNyHw_LQKT_Y7XNJw==) |
| 11 | `88.99.2.124` | `9841` | ✅ فعال | [tg://proxy?server=88.99.2.124&port=9841&secret=DDBighLLvXrFGRMCBVJdFQRueWVrdGFuZXQuY29t](tg://proxy?server=88.99.2.124&port=9841&secret=DDBighLLvXrFGRMCBVJdFQRueWVrdGFuZXQuY29t) |
| 12 | `irangodrati.co.uk.` | `443` | ✅ فعال | [tg://proxy?server=irangodrati.co.uk.&port=443&secret=7s8J5YYVhvOdr-WqHy_58gVtZWRpYS5zdGVhbXBvd2VyZWQuY29t](tg://proxy?server=irangodrati.co.uk.&port=443&secret=7s8J5YYVhvOdr-WqHy_58gVtZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 13 | `109.107.186.38` | `443` | ✅ فعال | [https://t.me/proxy?server=109.107.186.38&port=443&secret=eeNEgYdJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA](https://t.me/proxy?server=109.107.186.38&port=443&secret=eeNEgYdJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 14 | `91.99.165.90` | `443` | ✅ فعال | [tg://proxy?server=91.99.165.90&port=443&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0](tg://proxy?server=91.99.165.90&port=443&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0) |
| 15 | `85.198.111.90` | `443` | ✅ فعال | [tg://proxy?server=85.198.111.90&port=443&secret=7td9tD7jch8Py0Ck_2O1zSdtZWRpYS5zdGVhbXBvd2VyZWQuY29t](tg://proxy?server=85.198.111.90&port=443&secret=7td9tD7jch8Py0Ck_2O1zSdtZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 16 | `app.biatokonman.co.uk` | `85` | ✅ فعال | [tg://proxy?server=app.biatokonman.co.uk&port=85&secret=7gAA8A8Pd1VV____9QBuLmliaWF0b2tvbm1hbi5jby51aw](tg://proxy?server=app.biatokonman.co.uk&port=85&secret=7gAA8A8Pd1VV____9QBuLmliaWF0b2tvbm1hbi5jby51aw) |
| 17 | `91.84.97.20` | `443` | ✅ فعال | [https://t.me/proxy?server=91.84.97.20&port=443&secret=eeNEgYdJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA](https://t.me/proxy?server=91.84.97.20&port=443&secret=eeNEgYdJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 18 | `91.99.95.43` | `443` | ✅ فعال | [tg://proxy?server=91.99.95.43&port=443&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d)__](tg://proxy?server=91.99.95.43&port=443&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d)__) |
| 19 | `151.244.50.5` | `70` | ✅ فعال | [tg://proxy?server=151.244.50.5&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D](tg://proxy?server=151.244.50.5&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 20 | `151.244.50.63` | `200` | ✅ فعال | [tg://proxy?server=151.244.50.63&port=200&secret=79e344818749bd7ac519130220c25d09](tg://proxy?server=151.244.50.63&port=200&secret=79e344818749bd7ac519130220c25d09) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.

## 🤝 مشارکت
از ایده‌ها و مشارکت شما استقبال می‌کنیم! برای بهبود پروژه:
1. یک **Issue** در مخزن باز کنید.
2. یا یک **Pull Request** با تغییرات پیشنهادی ارسال کنید.

## 📜 لایسنس
این پروژه تحت [لایسنس MIT](LICENSE) منتشر شده است.

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
