# 📊 نتایج استخراج: (آخرین بروزرسانی: 06:22 13-02-1405)

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
| 1 | `178.104.98.160` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.104.98.160&port=443&secret=ee636c6f7564666c6172652e636f6db6) |
| 2 | `89.125.113.10` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.125.113.10&port=443&secret=ee700a15adb4cca8106fe1e0ad0dd35ce879616e6465782e7275) |
| 3 | `proxytg.fit` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxytg.fit&port=443&secret=eec8f164f338f20e2e3c7a0f4e0408a51270726f787974672e666974) |
| 4 | `5hu7-up-4nd-sell-me-mor3-th353-chocol47e5.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5hu7-up-4nd-sell-me-mor3-th353-chocol47e5.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 5 | `172.65.117.172` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.65.117.172&port=22&secret=dd79e344818749bd7ac519130220c25d09) |
| 6 | `62.60.237.40` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.60.237.40&port=443&secret=eee81e60b985ab58eb0d4c219ed761f249616d617a6f6e2e636f6d) |
| 7 | `91.107.166.142` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.166.142&port=8888&secret=ddb10c15b9f659ae2b9f1e646c9c7c1f40) |
| 8 | `89.125.113.11` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.125.113.11&port=443&secret=eebcb694130943ff7dcaf08c93b0564ff179616e6465782e7275) |
| 9 | `6161627.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=6161627.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 10 | `38.244.194.129` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=38.244.194.129&port=443&secret=ee105b4c7698aedbb55f291968ad2439d4647a656e2e7275) |
| 11 | `3.hajrozbeh.onl` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3.hajrozbeh.onl&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 12 | `195.254.165.251` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.251&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 13 | `5hu7-up-4nd-sell-me-mor3-th353-chocol47e5.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5hu7-up-4nd-sell-me-mor3-th353-chocol47e5.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 14 | `proxy.proxymtproto.net` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.proxymtproto.net&port=443&secret=dd97caa3c6888366f26b12f994f02ecf1a) |
| 15 | `188.137.255.14` | `41414` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=188.137.255.14&port=41414&secret=eea1b2c3d4e5f60123456789abcdef012373332e616d617a6f6e6177732e636f6d) |
| 16 | `77.239.125.158` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=77.239.125.158&port=443&secret=ee15465e6f97a4ca60ab5db03332290d6b77622e7275) |
| 17 | `predator-artist.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=predator-artist.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 18 | `132.243.228.115` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.228.115&port=443&secret=ee3caf4d06bf6b23313068e4b3e743f91e79616e6465782e7275) |
| 19 | `92.118.234.215` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=92.118.234.215&port=443&secret=dddb9b51b5ce9a2820ff62d348cb23f1b9) |
| 20 | `proxy.proxymtproto.net` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.proxymtproto.net&port=443&secret=dd97caa3c6888366f26b12f994f02ecf1a) |


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
