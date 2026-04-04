# 📊 نتایج استخراج: (آخرین بروزرسانی: 01:02 16-01-1405)

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
| 2 | `95.179.152.29` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.179.152.29&port=443&secret=3b6989c4974ba7fc9b1d3e00f3eed276) |
| 3 | `72.56.250.221` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=72.56.250.221&port=443&secret=eeff0c592463b7a03b31ce7fec93460449706574726f766963682e7275) |
| 4 | `o6xodum.duckdns.org` | `1488` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=o6xodum.duckdns.org&port=1488&secret=ee494c3d5858be223fcbb9970d8bf05a036d6f746f76736b696b682e7275) |
| 6 | `138.124.254.43` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=138.124.254.43&port=8443&secret=dd2fda9343d377b15c898cbd8b804e3cf5) |
| 7 | `p4.new-ai.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=p4.new-ai.uk&port=443&secret=eea55f874d57980ec9b48ab1098b0ae48b70342e6e65772d61692e756b) |
| 9 | `mt.fl8.vdl.lat` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.fl8.vdl.lat&port=443&secret=dd1a21752bd8823f6d2e7ac3642f2608ac) |
| 10 | `144.31.229.115` | `59105` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=144.31.229.115&port=59105&secret=ee74de2744cd6e7d76dd27f016d5a6ec666164732e78352e7275) |
| 11 | `prxygo.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=prxygo.shop&port=443&secret=48181acd22b3edaebc8a447868a7dfcb) |
| 13 | `proxy.ciaowner.lol` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.ciaowner.lol&port=443&secret=ee1459dda62dc99782f8741f1ab0deb4f2706574726f766963682e7275) |
| 14 | `116.203.0.182` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=116.203.0.182&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `46.225.29.180` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.225.29.180&port=443&secret=ee636c6f7564666c6172652e636f6db6) |
| 16 | `72.56.250.111` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=72.56.250.111&port=443&secret=eeff0c592463b7a03b31ce7fec93460449706574726f766963682e7275) |
| 17 | `172.65.102.115` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.65.102.115&port=22&secret=dd79e344818749bd7ac519130220c25d09) |
| 18 | `195.66.87.243` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.66.87.243&port=443&secret=ee361e6f00fe51e3551cfebfbd6ebe75e27765622e6d61782e7275) |
| 19 | `proxlet.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxlet.site&port=443&secret=8d969eef6ecad3c29a3a629280e686cf) |


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
