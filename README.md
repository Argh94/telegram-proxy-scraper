# 📊 نتایج استخراج: (آخرین بروزرسانی: 01:59 04-05-1404)

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
| 1 | `chernobill.technote.ir` | `443` | ✅ فعال | [https://t.me/proxy?server=chernobill.technote.ir&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d](https://t.me/proxy?server=chernobill.technote.ir&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 2 | `AAAAA.210.63.168-55.ir` | `9741` | ✅ فعال | [https://t.me/proxy?server=AAAAA.210.63.168-55.ir&port=9741&secret=7u7u8A8Pd1VV____9QReLpZtZWRpYS5zdGVhbXBvd2VyZWQuY29t](https://t.me/proxy?server=AAAAA.210.63.168-55.ir&port=9741&secret=7u7u8A8Pd1VV____9QReLpZtZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 3 | `62.60.178.33` | `443` | ✅ فعال | [https://t.me/proxy?server=62.60.178.33&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)`](https://t.me/proxy?server=62.60.178.33&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)`) |
| 4 | `193.3.190.47` | `85` | ✅ فعال | [https://t.me/proxy?server=193.3.190.47&port=85&secret=7gAA8A8Pd1VV____9QBuLmljaGF0Z3B0LmNvbQ](https://t.me/proxy?server=193.3.190.47&port=85&secret=7gAA8A8Pd1VV____9QBuLmljaGF0Z3B0LmNvbQ) |
| 5 | `51.159.157.218` | `7743` | ✅ فعال | [https://t.me/proxy?server=51.159.157.218&port=7743&secret=eedbe97246f57a3e90ccc1c3f25b8e15ef7777772e736974652e636f6d](https://t.me/proxy?server=51.159.157.218&port=7743&secret=eedbe97246f57a3e90ccc1c3f25b8e15ef7777772e736974652e636f6d) |
| 6 | `87.229.100.252` | `443` | ✅ فعال | [https://t.me/proxy?server=87.229.100.252&port=443&secret=eeRighJJvXrFGRMCIMJdCQ](https://t.me/proxy?server=87.229.100.252&port=443&secret=eeRighJJvXrFGRMCIMJdCQ) |
| 7 | `91.99.172.220` | `443` | ✅ فعال | [https://t.me/proxy?server=91.99.172.220&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t](https://t.me/proxy?server=91.99.172.220&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 8 | `151.244.85.38` | `443` | ✅ فعال | [https://t.me/proxy?server=151.244.85.38&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D](https://t.me/proxy?server=151.244.85.38&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 9 | `leveldaemi.fiziotr.info` | `443` | ✅ فعال | [https://t.me/proxy?server=leveldaemi.fiziotr.info&port=443&secret=7hYDAQIAAQAB_AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29t](https://t.me/proxy?server=leveldaemi.fiziotr.info&port=443&secret=7hYDAQIAAQAB_AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 10 | `91.99.178.38` | `888` | ✅ فعال | [https://t.me/proxy?server=91.99.178.38&port=888&secret=7gwwYoISy716xRkTAgVSXRVpYS5zdGVhbXBvd2VyZWQuY29t](https://t.me/proxy?server=91.99.178.38&port=888&secret=7gwwYoISy716xRkTAgVSXRVpYS5zdGVhbXBvd2VyZWQuY29t) |
| 11 | `203.25.108.13` | `85` | ✅ فعال | [https://t.me/proxy?server=203.25.108.13&port=85&secret=ee0000f00f0f775555fffffff5006e2e69646F776E6C6F61642E77696E646F77737570646174652E636F6D](https://t.me/proxy?server=203.25.108.13&port=85&secret=ee0000f00f0f775555fffffff5006e2e69646F776E6C6F61642E77696E646F77737570646174652E636F6D) |
| 12 | `151.244.50.63` | `200` | ✅ فعال | [https://t.me/proxy?server=151.244.50.63&port=200&secret=eeNEgYdJvXrFGRMCIMJdCQ](https://t.me/proxy?server=151.244.50.63&port=200&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `62.60.176.30` | `443` | ✅ فعال | [https://t.me/proxy?server=62.60.176.30&port=443&secret=7hAQEP8PSAZT____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t](https://t.me/proxy?server=62.60.176.30&port=443&secret=7hAQEP8PSAZT____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 14 | `ae.mohs1736.sbs` | `4637` | ✅ فعال | [https://t.me/proxy?server=ae.mohs1736.sbs&port=4637&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t)__](https://t.me/proxy?server=ae.mohs1736.sbs&port=4637&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t)__) |
| 15 | `CP1.shahrnetfarangsarashatelcenter.co.uk` | `443` | ✅ فعال | [https://t.me/proxy?server=CP1.shahrnetfarangsarashatelcenter.co.uk&port=443&secret=ee07df7df7df7dfffffdfffffffffffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d****](https://t.me/proxy?server=CP1.shahrnetfarangsarashatelcenter.co.uk&port=443&secret=ee07df7df7df7dfffffdfffffffffffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d****) |
| 16 | `62.60.177.143` | `8443` | ✅ فعال | [https://t.me/proxy?server=62.60.177.143&port=8443&secret=FgMBAgABAAfwAwOG4kw63Q](https://t.me/proxy?server=62.60.177.143&port=8443&secret=FgMBAgABAAfwAwOG4kw63Q) |
| 17 | `Startup-active.custome-tobano.avadox-zhoan.info` | `65` | ✅ فعال | [https://t.me/proxy?server=Startup-active.custome-tobano.avadox-zhoan.info&port=65&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t)**](https://t.me/proxy?server=Startup-active.custome-tobano.avadox-zhoan.info&port=65&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t)**) |
| 18 | `213.239.207.79` | `155` | ✅ فعال | [https://t.me/proxy?server=213.239.207.79&port=155&secret=1320PuNyHw_LQKT_Y7XNJw==](https://t.me/proxy?server=213.239.207.79&port=155&secret=1320PuNyHw_LQKT_Y7XNJw==) |
| 19 | `185.121.233.89` | `443` | ✅ فعال | [https://t.me/proxy?server=185.121.233.89&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D](https://t.me/proxy?server=185.121.233.89&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 20 | `87.248.134.9` | `4443` | ✅ فعال | [https://t.me/proxy?server=87.248.134.9&port=4443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D](https://t.me/proxy?server=87.248.134.9&port=4443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |


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
