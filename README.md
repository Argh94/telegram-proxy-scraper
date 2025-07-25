# 📊 نتایج استخراج: (آخرین بروزرسانی: 02:20 04-05-1404)

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
| 1 | `62.60.178.185` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.60.178.185&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)|) |
| 2 | `89.251.10.20` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.251.10.20&port=443&secret=ee151151151151151151151151151151156d656469612e737465616d706f77657265642e636f6d)[پروکسی](https://t.me/proxy?server=89.251.10.20) |
| 3 | `167.235.169.138` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.235.169.138&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 4 | `77.239.114.253` | `888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=77.239.114.253&port=888&secret=9a158f74da4d63d2cdfb4e09dbafffee) |
| 5 | `www.wwweror.space.` | `888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.wwweror.space.&port=888&secret=ee0c30628212cbbd7ac519130205525d1569612e737465616d706f77657265642e636f6d) |
| 6 | `Qavi.189-208-55-72.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Qavi.189-208-55-72.ir&port=443&secret=7td9tD7jch8Py0Ck_2O1zSdtZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 7 | `www.newtcpconnectiodo.store` | `888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.newtcpconnectiodo.store&port=888&secret=ee0c30628212cbbd7ac519130205525d1569612e737465616d706f77657265642e636f6d) |
| 8 | `188.166.49.247` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=188.166.49.247&port=443&secret=d1d069d2fb0fca4d28cd0e53bda39bbb) |
| 9 | `62.60.179.137` | `343` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.60.179.137&port=343&secret=FgMBAgABAAfwAwOG4kw63Q) |
| 10 | `response.cinere.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=response.cinere.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f7765726) |
| 11 | `87.248.132.34` | `70` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.132.34&port=70&secret=eed77db43) |
| 12 | `62.60.178.119` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.60.178.119&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)|) |
| 13 | `141.11.26.24` | `70` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=141.11.26.24&port=70&secret=1320PuNyHw_LQKT_Y7XNJw==) |
| 14 | `212.34.130.249` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=212.34.130.249&port=443&secret=eeNEgYdJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 15 | `193.3.190.6` | `85` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=193.3.190.6&port=85&secret=7gAA8A8Pd1VV____9QBuLmluYW1hdmEuaXI) |
| 16 | `ai.parsa-learning.ir.` | `333` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ai.parsa-learning.ir.&port=333&secret=7hAQEP8PSAZT____9QBuLmlpYS5zdGVhbXBvd2VyZWQuY29t) |
| 17 | `194.164.34.200` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.164.34.200&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 18 | `95.217.91.27` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.217.91.27&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t****) |
| 19 | `116.202.83.133` | `404` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=116.202.83.133&port=404&secret=79e344818749bd7ac519130220c25d09) |
| 20 | `157.180.30.251` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=157.180.30.251&port=443&secret=7HQighJPBNMYVRNB6tdkVw==) |


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
