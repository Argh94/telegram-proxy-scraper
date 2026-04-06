# 📊 نتایج استخراج: (آخرین بروزرسانی: 19:17 17-01-1405)

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
| 1 | `150.241.71.185` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=150.241.71.185&port=8443&secret=ee4d0a2c3e636d0763084f3bed56cfce5f636c6f7564666c6172652e636f6d) |
| 2 | `144.31.157.26` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=144.31.157.26&port=443&secret=ee3f354f86e59e2c166c83031772d92d6379612e7275) |
| 3 | `Fast.love-internet.xyz` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Fast.love-internet.xyz&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |
| 5 | `84.252.100.26` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=84.252.100.26&port=443&secret=ee3f354f86e59e2c166c83031772d92d6379612e7275) |
| 6 | `2.27.21.243` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.27.21.243&port=443&secret=ee3f354f86e59e2c166c83031772d92d6379612e7275) |
| 7 | `tg.vless.cloud` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.vless.cloud&port=25565&secret=eec52989e32ab86d01d07ad0e9ab642846696d616765732e6170706c652e636f6d) |
| 9 | `80.66.65.184` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=80.66.65.184&port=443&secret=ee3f354f86e59e2c166c83031772d92d6379612e7275) |
| 10 | `dowd.sportsmanship.steeplechaser.thy.urceolate.kapitoshka.info` | `15417` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dowd.sportsmanship.steeplechaser.thy.urceolate.kapitoshka.info&port=15417&secret=d6db8ab62ff9b9f70f6ca15ccb98c222) |
| 11 | `3.hajrozbeh.onl` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3.hajrozbeh.onl&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 12 | `171.22.31.13` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=171.22.31.13&port=443&secret=ee3f354f86e59e2c166c83031772d92d6379612e7275) |
| 13 | `2.26.98.220` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.26.98.220&port=443&secret=ee3f354f86e59e2c166c83031772d92d6379612e7275) |
| 15 | `6161627.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=6161627.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 16 | `207.180.253.71` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=207.180.253.71&port=443&secret=eea136023cfd26d54332adf93ccca90960636c6f7564666c6172652e636f6d) |
| 17 | `zoomit.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zoomit.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 18 | `de1.kael.fuckrkn.net` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=de1.kael.fuckrkn.net&port=443&secret=ee1a499af9a7a18282da82e30714402e157777772e6165726f666c6f742e7275) |
| 19 | `proxydazhenaparkovke.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxydazhenaparkovke.site&port=443&secret=dde8aa2e8c1ad50570b7d6fe7e0ba3d677) |
| 20 | `212.80.7.134` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=212.80.7.134&port=443&secret=ee3f354f86e59e2c166c83031772d92d6379612e7275) |


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
