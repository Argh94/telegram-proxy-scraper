# 📊 نتایج استخراج: (آخرین بروزرسانی: 22:14 16-01-1405)

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
| 2 | `app.free-telegram.link` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=app.free-telegram.link&port=443&secret=ddfb47a1320fa86adfa6e63b425154ce1b) |
| 3 | `185.174.137.50` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.174.137.50&port=8443&secret=676c4049812b842b7792954bf2a32943) |
| 4 | `77.42.43.220` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=77.42.43.220&port=443&secret=ee442d1fb2156a1473f94bb181aba9b92a636c6f7564666c6172652e636f6d) |
| 5 | `173.212.229.99` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=173.212.229.99&port=443&secret=eefea85401978c4b18d790fe3aaed5764c636c6f7564666c6172652e636f6d) |
| 6 | `167.233.12.183` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.233.12.183&port=443&secret=ddc333a2a17e2be71f9cf1887f3b22dc7d) |
| 7 | `soft.telegramharvester.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=soft.telegramharvester.ru&port=443&secret=ee05ca1fb5eadbac1e7e8c725695b48f0079612e7275) |
| 9 | `107.175.189.200` | `8447` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=107.175.189.200&port=8447&secret=554b3dd4c9d6fbbe2101c12765bb4229) |
| 10 | `27289292.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=27289292.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 11 | `138.124.254.125` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=138.124.254.125&port=443&secret=ee470cb2b8b29aeadfbdf8a2f7bee5ca3b62726f777365722e79616e6465782e636f6d) |
| 12 | `37.27.42.53` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=37.27.42.53&port=443&secret=ee400beecda94bbb22a7759357fd921c00636c6f7564666c6172652e636f6d) |
| 14 | `146.103.116.221` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=146.103.116.221&port=443&secret=3c9306bf0ab91b79fd23d57a521b79af) |
| 15 | `212.111.84.201` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=212.111.84.201&port=443&secret=dd79870f7f2a69beb5c0206d8697c40ed9) |
| 16 | `go.bolshevps.su` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=go.bolshevps.su&port=443&secret=ee617782cbbfb6dcc27b0e338f570da65f6164732e78352e7275) |
| 17 | `how.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=how.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 19 | `jp.767958.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jp.767958.xyz&port=443&secret=ee8eddf64a864c234ef6cdc41dfb1513b4617a7572652e6d6963726f736f66742e636f6d) |
| 20 | `own.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=own.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |


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
