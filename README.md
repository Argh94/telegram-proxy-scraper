# 📊 نتایج استخراج: (آخرین بروزرسانی: 01:09 18-01-1405)

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
| 2 | `164.68.119.250` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=164.68.119.250&port=443&secret=eee232555f829c81c2193b08f59b08ca19636c6f7564666c6172652e636f6d) |
| 3 | `2.27.22.224` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.27.22.224&port=443&secret=ee3f354f86e59e2c166c83031772d92d6379612e7275) |
| 5 | `80.66.65.184` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=80.66.65.184&port=443&secret=ee3f354f86e59e2c166c83031772d92d6379612e7275) |
| 6 | `142.54.189.107` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=142.54.189.107&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 7 | `207.180.253.71` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=207.180.253.71&port=443&secret=eea136023cfd26d54332adf93ccca90960636c6f7564666c6172652e636f6d) |
| 9 | `144.91.71.245` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=144.91.71.245&port=443&secret=ee0b2abbe3b912d1c71c2116af79ce7f03636c6f7564666c6172652e636f6d) |
| 10 | `nano.happvpn.cc` | `4514` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nano.happvpn.cc&port=4514&secret=ee0a638f4a7bd9db9e94449c652ea963066e616e6f2e6861707076706e2e6363) |
| 11 | `164.68.122.140` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=164.68.122.140&port=443&secret=ee87dd4304ba0973ef97a9f14aea404623636c6f7564666c6172652e636f6d) |
| 12 | `caveat.dyslexia.justly.pedlery.talisman.superpinoy.net` | `2450` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=caveat.dyslexia.justly.pedlery.talisman.superpinoy.net&port=2450&secret=8f6c67087a603cb91c94886ba79d4bdd) |
| 13 | `142.54.189.109` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=142.54.189.109&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 14 | `charlie.freetelega.me` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=charlie.freetelega.me&port=8443&secret=eec2eec77016252e334767f27d5b208fb27265672e7275) |
| 16 | `84.201.169.90` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=84.201.169.90&port=443&secret=ee387cc39e6784d06b17cc32354e92bfe66164732e78352e7275) |
| 17 | `3.hajrozbeh.onl` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3.hajrozbeh.onl&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 18 | `rkn.tg` | `1337` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rkn.tg&port=1337&secret=dda2d3fa639a6ddcf8d6d1c5913d001531) |
| 19 | `2.27.22.225` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.27.22.225&port=443&secret=ee3f354f86e59e2c166c83031772d92d6379612e7275) |
| 20 | `212.233.89.91` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=212.233.89.91&port=443&secret=ddf4b54d805ffeff430be106aa80d94f7f) |


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
