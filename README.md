# 📊 نتایج استخراج: (آخرین بروزرسانی: 19:23 19-02-1405)

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
| 1 | `mtp.yard-tg-bot.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtp.yard-tg-bot.ru&port=443&secret=eef658bb6d89b284874149c13e7d27d9da79616e6465782e7275) |
| 2 | `195.254.165.247` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.247&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 3 | `132.243.235.196` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.235.196&port=443&secret=ee5895bbd18604365e8d18b63af6c3bfbe79616e6465782e7275) |
| 4 | `mtp.webvirt.cloud` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtp.webvirt.cloud&port=443&secret=ee938dd87467bc49301de2e9765cf20f4374656c2e776562766972742e636c6f7564) |
| 5 | `connect.tproxyru.live` | `8980` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=connect.tproxyru.live&port=8980&secret=ee104462821249bd7ac519130220c25d09617669746f2e7275) |
| 6 | `132.243.235.188` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.235.188&port=443&secret=eecff01a06513433100e81c6eadff452e779616e6465782e7275) |
| 8 | `37.27.38.205` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=37.27.38.205&port=443&secret=ee9d659fc2ae43e0b8323c082960233d7b7777772e636c6f7564666c6172652e636f6d) |
| 9 | `proxy.yard-tg-bot.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.yard-tg-bot.ru&port=443&secret=ee1cfe2c07741ef6c9d9dde94a7f14a3db79616e6465782e7275) |
| 11 | `79.137.196.223` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.137.196.223&port=8443&secret=eeeeacd334a255675ccc880cb6b8c9caf07777772e636c6f7564666c6172652e636f6d) |
| 12 | `skill-issue.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=skill-issue.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 13 | `2A.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2A.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 14 | `89.125.113.8` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.125.113.8&port=443&secret=ee5b99cc79c1fe095be478df4111e00b6379616e6465782e7275) |
| 15 | `i-love-boobs.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=i-love-boobs.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 16 | `believe-gravity.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=believe-gravity.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 17 | `172.86.95.195` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.86.95.195&port=443&secret=eeb30612d6f0fac137fa363faee6afe3377262632e7275) |
| 18 | `89.125.113.10` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.125.113.10&port=443&secret=eeb0991382f903caac3568e5f9c7288d3e79616e6465782e7275) |
| 19 | `espress0-macch1ato-p0r-favor3.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=espress0-macch1ato-p0r-favor3.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 20 | `50.7.41.162` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=50.7.41.162&port=443&secret=ee011808bcccfd224644ca7f231846a7d46d61782e7275) |


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
