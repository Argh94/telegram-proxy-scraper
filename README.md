# 📊 نتایج استخراج: (آخرین بروزرسانی: 06:08 27-01-1405)

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
| 1 | `frhb90498flex.ikexpress.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=frhb90498flex.ikexpress.com&port=443&secret=ee5df55ec73ac44c90b83e29641e28fd26676f6f676c652e636f6d) |
| 2 | `195.254.165.247` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.247&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 3 | `195.254.165.250` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.250&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 4 | `195.254.165.243` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.243&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 5 | `3.hajrozbeh.onl` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3.hajrozbeh.onl&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 6 | `178.104.202.42` | `9321` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.104.202.42&port=9321&secret=ee104462821249bd7ac519130220c25d096d61696c2e7275) |
| 8 | `prxtg.enterlancevpn.com` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=prxtg.enterlancevpn.com&port=8443&secret=ee79612e7275c8d582e6565ef8a46786) |
| 9 | `31.220.72.60` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=31.220.72.60&port=443&secret=ee399a6e8dbe6399816eba10c0fa78609d636c6f7564666c6172652e636f6d) |
| 10 | `116.203.0.182` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=116.203.0.182&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 12 | `knoll0422-c522b2fb.proxytg.ink` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=knoll0422-c522b2fb.proxytg.ink&port=443&secret=28ed0c814a97362df6fed7339922e795) |
| 13 | `nano.happvpn.cc` | `4514` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nano.happvpn.cc&port=4514&secret=ee0a638f4a7bd9db9e94449c652ea963066e616e6f2e6861707076706e2e6363) |
| 14 | `95.85.251.66` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.85.251.66&port=443&secret=ee8e52a74eebc889c2691b756d1b0a9ae139352e38352e3235312e36362e6e69702e696f) |
| 15 | `2.27.4.58` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.27.4.58&port=443&secret=ee9d343635a76a38133c6d01e1c81f50cf706574726f766963682e7275) |
| 16 | `195.254.165.253` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.253&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 17 | `88.198.56.230` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=88.198.56.230&port=8080&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `31.220.72.224` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=31.220.72.224&port=443&secret=eea53322ad1baa135a8fcc2d5d6bff6e3a636c6f7564666c6172652e636f6d) |
| 19 | `hyper.happvpn.cc` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hyper.happvpn.cc&port=8443&secret=ee4852c1c04ab83db8a328c60eaf9a0db268797065722e6861707076706e2e6363) |
| 20 | `rkn.tg` | `1337` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rkn.tg&port=1337&secret=dda2d3fa639a6ddcf8d6d1c5913d001531) |


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
