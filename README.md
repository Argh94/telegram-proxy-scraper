# 📊 نتایج استخراج: (آخرین بروزرسانی: 07:04 03-03-1405)

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
| 1 | `87.120.108.48` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.120.108.48&port=443&secret=074e7d1d37cc043746fd0c823f20d21a) |
| 3 | `win.sosproxy.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=win.sosproxy.space&port=443&secret=ee477ccce74a28c13a2ef6ec9e01510c3164726976652e676f6f676c652e636f6d) |
| 4 | `78.17.71.42` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=78.17.71.42&port=443&secret=eeec75b855ebcc01c982f3e013af8ed92a7777772e79616e6465782e7275) |
| 5 | `186.246.16.232` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=186.246.16.232&port=443&secret=eec11798ab008831b474066c9e1ebf5c85617669746f2e7275) |
| 6 | `176.125.240.195` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=176.125.240.195&port=443&secret=eeae49fc0cb49514612b72494665fffa167777772e79616e6465782e7275) |
| 7 | `195.254.165.143` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.143&port=4455&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d) |
| 8 | `31.56.229.49` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=31.56.229.49&port=443&secret=ee4e8084b6d0f3a39986ceb5fab26859ee7777772e6d6963726f736f66742e636f6d) |
| 9 | `89.167.103.249` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.167.103.249&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `2.26.255.73` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.26.255.73&port=443&secret=eeab03f51ca82ec9e172a5eba3b169f6cd7777772e77702e706c) |
| 11 | `tproxy.monster` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tproxy.monster&port=2053&secret=ee104462821249bd7ac519130220c25d096d61696c2e7275) |
| 13 | `tproxy.mom` | `8090` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tproxy.mom&port=8090&secret=ee104462821249bd7ac519130220c25d09617669746f2e7275) |
| 14 | `89.35.131.217` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.35.131.217&port=443&secret=ee21406fa1321a733a9fe7edd39ddbe4fe7777772e79616e6465782e7275) |
| 15 | `91.107.189.181` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.189.181&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `proxy.fluxoria.it.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.fluxoria.it.com&port=443&secret=ee307242dd41275c771f40035565d0750a70726f78792e666c75786f7269612e69742e636f6d) |
| 18 | `alpinavpn.hatecens.cc` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=alpinavpn.hatecens.cc&port=7443&secret=eef8dc254a4c2af8afcab54c8a5f9bb4fb616c70696e6176706e2e6861746563656e732e6363) |
| 19 | `FREE.edgeCDN-static.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=FREE.edgeCDN-static.com&port=443&secret=eea1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d66564676563646e2d7374617469632e636f6d) |


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
