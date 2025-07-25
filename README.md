# 📊 نتایج استخراج: (آخرین بروزرسانی: 01:29 04-05-1404)

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
| 1 | `62.60.178.117` | `443` | ✅ فعال | [**کپی لینک**](tg://proxy?server=62.60.178.117&port=443&secret=1603010200010001fc030386e24c3add) |
| 2 | `5.35.46.105` | `443` | ✅ فعال | [**کپی لینک**](https://t.me/proxy?server=5.35.46.105&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 3 | `phyzyk.nokande.info` | `443` | ✅ فعال | [**کپی لینک**](tg://proxy?server=phyzyk.nokande.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 4 | `62.60.176.132` | `443` | ✅ فعال | [**کپی لینک**](tg://proxy?server=62.60.176.132&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 5 | `151.244.42.2` | `85` | ✅ فعال | [**کپی لینک**](tg://proxy?server=151.244.42.2&port=85&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 6 | `error.parsa-learning.ir.` | `333` | ✅ فعال | [**کپی لینک**](https://t.me/proxy?server=error.parsa-learning.ir.&port=333&secret=7hAQEP8PSAZT____9QBuLmlpYS5zdGVhbXBvd2VyZWQuY29t) |
| 7 | `4.meli.zban-mas.info` | `8888` | ✅ فعال | [**کپی لینک**](tg://proxy?server=4.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV////9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 8 | `response.cinere.info` | `443` | ✅ فعال | [**کپی لینک**](tg://proxy?server=response.cinere.info&port=443&secret=7hYDAQIAAQAB_AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 9 | `5.Ir.ir.ir.ir.ir.zban-mas.info` | `8888` | ✅ فعال | [**کپی لینک**](tg://proxy?server=5.Ir.ir.ir.ir.ir.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 10 | `kheybar.co.uk` | `443` | ✅ فعال | [**کپی لینک**](tg://proxy?server=kheybar.co.uk&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 11 | `pes2021-update2025.magalaiash.info` | `443` | ✅ فعال | [**کپی لینک**](https://t.me/proxy?server=pes2021-update2025.magalaiash.info&port=443&secret=7hYDAQIAAQAB_AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 12 | `212.34.132.116` | `443` | ✅ فعال | [**کپی لینک**](tg://proxy?server=212.34.132.116&port=443&secret=1320PuNyHw_LQKT_Y7XNJw==) |
| 13 | `91.84.106.230` | `443` | ✅ فعال | [**کپی لینک**](tg://proxy?server=91.84.106.230&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 14 | `212.34.141.71` | `443` | ✅ فعال | [**کپی لینک**](tg://proxy?server=212.34.141.71&port=443&secret=1320PuNyHw_LQKT_Y7XNJw) |
| 15 | `47.250.45.121` | `443` | ✅ فعال | [**کپی لینک**](tg://proxy?server=47.250.45.121&port=443&secret=eeb2c426a5aaa97f69f6e386d64f8c789a617a7572652e6d6963726f736f66742e636f6d) |
| 16 | `93.88.205.35` | `85` | ✅ فعال | [**کپی لینک**](tg://proxy?server=93.88.205.35&port=85&secret=7gAA8A8Pd1VV__9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 17 | `14.102.10.50` | `888` | ✅ فعال | [**کپی لینک**](tg://proxy?server=14.102.10.50&port=888&secret=FgMBAgABAAH8AwOG4kw63Q) |
| 18 | `A62.206-197-43.ir` | `777` | ✅ فعال | [**کپی لینک**](tg://proxy?server=A62.206-197-43.ir&port=777&secret=7td9tD7jch8PzUCk_2PVzSdtZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 19 | `8-elite.ultrasam.info` | `443` | ✅ فعال | [**کپی لینک**](https://t.me/proxy?server=8-elite.ultrasam.info&port=443&secret=7hYDAQIAAQAB_AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 20 | `79.172.228.46` | `70` | ✅ فعال | [**کپی لینک**](tg://proxy?server=79.172.228.46&port=70&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D) |


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
