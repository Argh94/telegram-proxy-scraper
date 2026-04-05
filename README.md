# 📊 نتایج استخراج: (آخرین بروزرسانی: 06:00 16-01-1405)

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
| 1 | `mtproto.proproxies.pro` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtproto.proproxies.pro&port=8443&secret=ee8e60f2fe61cf363f9ed0d0695b59c6d86d7470726f746f2e70726f70726f786965732e70726f) |
| 2 | `burned.concordantly.onlay.unicolourous.wholesale.superpinoy.net` | `2500` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=burned.concordantly.onlay.unicolourous.wholesale.superpinoy.net&port=2500&secret=fd35d27eb736c8d1527e44aa67d57649) |
| 3 | `95.179.184.84` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.179.184.84&port=443&secret=7bf15239c97a187712d3c8ff662fa113) |
| 4 | `195.66.87.243` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.66.87.243&port=443&secret=ee361e6f00fe51e3551cfebfbd6ebe75e27765622e6d61782e7275) |
| 5 | `144.31.230.217` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=144.31.230.217&port=443&secret=33d73370103ea05acd9418eb9dca989e) |
| 6 | `mt.fl8.vdl.lat` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.fl8.vdl.lat&port=443&secret=dd1a21752bd8823f6d2e7ac3642f2608ac) |
| 7 | `178.104.72.162` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.104.72.162&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `155.138.202.81` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=155.138.202.81&port=443&secret=9e4862383f46562395c4c546479acd33) |
| 9 | `soft.telegramharvester.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=soft.telegramharvester.ru&port=443&secret=ee05ca1fb5eadbac1e7e8c725695b48f0079612e7275) |
| 10 | `77.90.63.2` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=77.90.63.2&port=443&secret=ee8dd986e1d1ea297bdb58db4b5e369af57777772e676f6f676c652e636f6d) |
| 11 | `prxygo.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=prxygo.shop&port=443&secret=48181acd22b3edaebc8a447868a7dfcb) |
| 12 | `p5.new-ai.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=p5.new-ai.uk&port=443&secret=ee27b68bda6b4b99915f73a423b17f768470352e6e65772d61692e756b) |
| 13 | `95.85.231.6` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.85.231.6&port=8443&secret=46b107169c2e3968abc49eba40928782) |
| 14 | `172.65.102.115` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.65.102.115&port=22&secret=dd79e344818749bd7ac519130220c25d09) |
| 15 | `193.222.99.7` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=193.222.99.7&port=8888&secret=ddbb560aad55358c4fe10ae84cb8110348) |
| 16 | `proxium.rest` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxium.rest&port=443&secret=a665a45920422f9d417e4867efdc4fb8) |
| 17 | `209.250.238.192` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=209.250.238.192&port=443&secret=6c87b1eac5d66e8df9d561965b85d2f7) |
| 18 | `proxyobhod.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxyobhod.online&port=443&secret=71c30cc28759e0a10b6de5b471d69751) |
| 19 | `108.61.179.245` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=108.61.179.245&port=443&secret=e8fc2977f2a2ac84d99e895d0a96884f) |
| 20 | `144.31.135.73` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=144.31.135.73&port=443&secret=abb29dcec88e73610721bcf68c00b796) |


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
