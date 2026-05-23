# 📊 نتایج استخراج: (آخرین بروزرسانی: 17:02 02-03-1405)

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
| 1 | `another.life.mambabot.net` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=another.life.mambabot.net&port=4515&secret=eec485b564c0178c338d8bf4f3f17539c4613234382e652e616b616d61692e6e6574) |
| 2 | `94.125.102.217` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=94.125.102.217&port=443&secret=ee244217408227effcd6234e992d9bd9827777772e77702e706c) |
| 3 | `87.120.108.48` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.120.108.48&port=443&secret=074e7d1d37cc043746fd0c823f20d21a) |
| 5 | `89.167.104.111` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.167.104.111&port=443&secret=b3f0c7f6af7dc2dc2e9c80d0d80e8162) |
| 6 | `alpinavpn.hatecens.cc` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=alpinavpn.hatecens.cc&port=7443&secret=eef8dc254a4c2af8afcab54c8a5f9bb4fb616c70696e6176706e2e6861746563656e732e6363) |
| 7 | `178.104.244.158` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.104.244.158&port=8080&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `138.124.127.154` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=138.124.127.154&port=443&secret=ee0c480abc71136dd1c5dadf918e32cea7766b2e636f6d) |
| 10 | `i-love-hse.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=i-love-hse.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 11 | `premium1.fsproxy.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=premium1.fsproxy.site&port=443&secret=eed29605852bf2e034c63c6f866062600f696e2e6d7974686963616c2e686f757365) |
| 12 | `2.27.41.207` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.27.41.207&port=443&secret=9436fa39ab47ccb34f217ac6d06b4e58) |
| 13 | `144.31.54.207` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=144.31.54.207&port=443&secret=eec5081bcd191b76e90ee894d248e44c42706574726f766963682e7275) |
| 14 | `owner-explain.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=owner-explain.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 15 | `95.217.235.33` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.217.235.33&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `proxy.yard-tg-bot.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.yard-tg-bot.ru&port=443&secret=ee1cfe2c07741ef6c9d9dde94a7f14a3db79616e6465782e7275) |
| 17 | `win.sosproxy.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=win.sosproxy.space&port=443&secret=ee477ccce74a28c13a2ef6ec9e01510c3164726976652e676f6f676c652e636f6d) |
| 18 | `hop2.proxytg.space` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hop2.proxytg.space&port=8443&secret=eeaaa47352535a38478c5c9954a708f4ff6e686c2e636f6d) |
| 19 | `77.42.79.76` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=77.42.79.76&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `138.124.127.157` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=138.124.127.157&port=443&secret=ee776ed6e05e7099a53f923bdcc99f659e766b2e636f6d) |


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
