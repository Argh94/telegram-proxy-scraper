# 📊 نتایج استخراج: (آخرین بروزرسانی: 16:28 22-01-1405)

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
| 1 | `164.68.111.163` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=164.68.111.163&port=443&secret=ee9fc1d5793a3a7470f6b5aba24abd476a636c6f7564666c6172652e636f6d) |
| 3 | `89.117.63.176` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.117.63.176&port=443&secret=ee4e3346cfb87699c595c051b55e3705d2636c6f7564666c6172652e636f6d) |
| 4 | `95.217.25.41` | `35432` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.217.25.41&port=35432&secret=ee104462821249bd7ac519130220c25d096d61782e7275) |
| 5 | `46.225.29.180` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.225.29.180&port=443&secret=ee636c6f7564666c6172652e636f6db6) |
| 6 | `168.222.254.50` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=168.222.254.50&port=443&secret=86a518fe71e9bbb70db48ea77b74ec79) |
| 7 | `62.171.135.77` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.171.135.77&port=443&secret=eeca4579380da2228bf1e70bc43b666d8c636c6f7564666c6172652e636f6d) |
| 8 | `172.65.102.115` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.65.102.115&port=22&secret=dd79e344818749bd7ac519130220c25d09) |
| 9 | `195.254.165.252` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.252&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 10 | `72.56.247.5` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=72.56.247.5&port=443&secret=eece30a4906087f0a9605f804e11a1e0336d61782e7275) |
| 11 | `2A.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2A.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 12 | `31.130.151.16` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=31.130.151.16&port=443&secret=4931e9e6000537266a0de4dbb81f81fa) |
| 13 | `144.91.118.127` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=144.91.118.127&port=443&secret=eed3d0797e6033939e7fae7f095c307991636c6f7564666c6172652e636f6d) |
| 14 | `31.220.74.142` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=31.220.74.142&port=443&secret=ee95ff4820a4a489822c5fc56bd686fbb6636c6f7564666c6172652e636f6d) |
| 15 | `47.243.7.197` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=47.243.7.197&port=443&secret=eee5e4bf3ea829b0530f705f8e9776c0e9617a7572652e6d6963726f736f66742e636f6d) |
| 16 | `62.84.126.12` | `3443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.84.126.12&port=3443&secret=679f7f50045349a76724af59906a1013) |
| 17 | `45.63.43.130` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.63.43.130&port=443&secret=2f218706df4cf2dd2d026e9871308289) |
| 18 | `five.proxyprosto.sbs` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=five.proxyprosto.sbs&port=443&secret=ee5ebd2af5512770fc537a14dc2f40818877622e7275) |
| 19 | `146.185.211.189` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=146.185.211.189&port=443&secret=ee3a0641397a47d10417ee57f90fa646726d61782e7275) |
| 20 | `45.116.79.246` | `20001` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.116.79.246&port=20001&secret=eea5942ff95e1bc79f3598114dfc767d19617a7572652e6d6963726f736f66742e636f6d) |


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
