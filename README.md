# 📊 نتایج استخراج: (آخرین بروزرسانی: 02:23 04-05-1404)

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
| 1 | `iran-vatan.magalaiash.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=iran-vatan.magalaiash.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 2 | `62.60.179.41` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.60.179.41&port=443&secret=7hAQEP8PSAZT____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 3 | `62.60.176.10` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.60.176.10&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 4 | `77.239.114.253` | `888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=77.239.114.253&port=888&secret=9a158f74da4d63d2cdfb4e09dbafffee) |
| 5 | `new-pio-iran-ck-uk-ir.zx2hgujoiah-xy1xutr021-2tk.com` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=new-pio-iran-ck-uk-ir.zx2hgujoiah-xy1xutr021-2tk.com&port=8443&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0=)__) |
| 6 | `62.60.177.194` | `9741` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.60.177.194&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 7 | `8.220.186.24` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=8.220.186.24&port=443&secret=eefb8c98ae8fb08f1e9633ed19a6e9098f617a7572652e6d6963726f736f66742e636f6d) |
| 8 | `5.35.39.190` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.35.39.190&port=443&secret=eeNEgYdJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 9 | `103.161.34.217` | `65` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=103.161.34.217&port=65&secret=eeNEgYdJvXrFGRMCIMJdCQ**) |
| 10 | `91.99.235.43` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.99.235.43&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 11 | `62.60.176.63` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.60.176.63&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)__) |
| 12 | `95.142.45.42` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.142.45.42&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 13 | `87.248.132.81` | `155` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.132.81&port=155&secret=EERighJJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 14 | `79.172.228.19` | `70` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.172.228.19&port=70&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D) |
| 15 | `473.Ir.ir.ir.ir.ir.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=473.Ir.ir.ir.ir.ir.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 16 | `46.249.110.245` | `9741` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.249.110.245&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D) |
| 17 | `116.202.3.187` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=116.202.3.187&port=443&secret=DDBighLLvXrFGRMCBVJdFQ==) |
| 18 | `27.72.38-83.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=27.72.38-83.ir&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 19 | `62.60.179.157` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.60.179.157&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ) |
| 20 | `37.203.37.15` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=37.203.37.15&port=443&secret=7hAQEP8PSAZT____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |


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
