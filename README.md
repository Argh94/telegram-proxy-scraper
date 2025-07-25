# 📊 نتایج استخراج: (آخرین بروزرسانی: 01:39 04-05-1404)

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
| 1 | `00800.meli.zban-mas.info` | `8888` | ✅ فعال | [tg://proxy?server=00800.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t**](tg://proxy?server=00800.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t**) |
| 2 | `87.248.132.44` | `200` | ✅ فعال | [tg://proxy?server=87.248.132.44&port=200&secret=79e344818749bd7ac519130220c25d09](tg://proxy?server=87.248.132.44&port=200&secret=79e344818749bd7ac519130220c25d09) |
| 3 | `89.110.84.76` | `443` | ✅ فعال | [tg://proxy?server=89.110.84.76&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t](tg://proxy?server=89.110.84.76&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 4 | `193.3.190.47` | `85` | ✅ فعال | [tg://proxy?server=193.3.190.47&port=85&secret=7gAA8A8Pd1VV____9QBuLmljaGF0Z3B0LmNvbQ==](tg://proxy?server=193.3.190.47&port=85&secret=7gAA8A8Pd1VV____9QBuLmljaGF0Z3B0LmNvbQ==) |
| 5 | `994.meli.meli.zban-mas.info` | `8888` | ✅ فعال | [tg://proxy?server=994.meli.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t](tg://proxy?server=994.meli.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 6 | `91.99.172.220` | `443` | ✅ فعال | [tg://proxy?server=91.99.172.220&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t](tg://proxy?server=91.99.172.220&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 7 | `sitemcinet.co.uk` | `443` | ✅ فعال | [tg://proxy?server=sitemcinet.co.uk&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t)__](tg://proxy?server=sitemcinet.co.uk&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t)__) |
| 8 | `88.119.165.95` | `155` | ✅ فعال | [tg://proxy?server=88.119.165.95&port=155&secret=7s7477TTTTTTETTTTTTTtrYtRi5rby0](tg://proxy?server=88.119.165.95&port=155&secret=7s7477TTTTTTETTTTTTTtrYtRi5rby0) |
| 9 | `home.cphosting.shop` | `443` | ✅ فعال | [tg://proxy?server=home.cphosting.shop&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t](tg://proxy?server=home.cphosting.shop&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 10 | `62.60.179.156` | `443` | ✅ فعال | [tg://proxy?server=62.60.179.156&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)`](tg://proxy?server=62.60.179.156&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)`) |
| 11 | `89.251.10.22` | `443` | ✅ فعال | [tg://proxy?server=89.251.10.22&port=443&secret=ee151151151151151151151151151151156d656469612e737465616d706f77657265642e636f6d](tg://proxy?server=89.251.10.22&port=443&secret=ee151151151151151151151151151151156d656469612e737465616d706f77657265642e636f6d) |
| 12 | `146.103.105.105` | `70` | ✅ فعال | [tg://proxy?server=146.103.105.105&port=70&secret=1320PuNyHw_LQKT_Y7XNJw==](tg://proxy?server=146.103.105.105&port=70&secret=1320PuNyHw_LQKT_Y7XNJw==) |
| 13 | `91.99.179.31` | `70` | ✅ فعال | [tg://proxy?server=91.99.179.31&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d](tg://proxy?server=91.99.179.31&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d) |
| 14 | `vip.bomberoo.co.uk` | `155` | ✅ فعال | [https://t.me/proxy?server=vip.bomberoo.co.uk&port=155&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ](https://t.me/proxy?server=vip.bomberoo.co.uk&port=155&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ) |
| 15 | `94.130.218.244` | `443` | ✅ فعال | [tg://proxy?server=94.130.218.244&port=443&secret=EERighJJvXrFGRMCIMJdCQ](tg://proxy?server=94.130.218.244&port=443&secret=EERighJJvXrFGRMCIMJdCQ) |
| 16 | `fpf027.meli.zban-mas.info` | `8888` | ✅ فعال | [tg://proxy?server=fpf027.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t](tg://proxy?server=fpf027.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 17 | `151.244.85.77` | `343` | ✅ فعال | [tg://proxy?server=151.244.85.77&port=343&secret=7td9tD7jch8Py0Ck/2O1zSdtZWRpYS5zdGVhbXBvd2VyZWQuY29t](tg://proxy?server=151.244.85.77&port=343&secret=7td9tD7jch8Py0Ck/2O1zSdtZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 18 | `193.3.190.60` | `85` | ✅ فعال | [tg://proxy?server=193.3.190.60&port=85&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636](tg://proxy?server=193.3.190.60&port=85&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636) |
| 19 | `62.60.178.2` | `8888` | ✅ فعال | [tg://proxy?server=62.60.178.2&port=8888&secret=7gAA8A8Pd1VV9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t____](tg://proxy?server=62.60.178.2&port=8888&secret=7gAA8A8Pd1VV9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t____) |
| 20 | `14.102.10.51` | `888` | ✅ فعال | [tg://proxy?server=14.102.10.51&port=888&secret=FgMBAgABAAH8AwOG4kw63Q](tg://proxy?server=14.102.10.51&port=888&secret=FgMBAgABAAH8AwOG4kw63Q) |


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
