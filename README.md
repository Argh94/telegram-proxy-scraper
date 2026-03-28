# 📊 نتایج استخراج: (آخرین بروزرسانی: 05:38 08-01-1405)

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
| 1 | `mt.ipizdec.lol` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.ipizdec.lol&port=443&secret=de18609544eb7fa267cf94735d320ac5) |
| 2 | `telegram.mtpproxy.ltvpn.org` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=telegram.mtpproxy.ltvpn.org&port=443&secret=9e9458e4b939ce0894bc146049e64b58) |
| 3 | `VIP.alotaxi.info` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=VIP.alotaxi.info&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |
| 4 | `185.174.137.50` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.174.137.50&port=8443&secret=676c4049812b842b7792954bf2a32943) |
| 5 | `185.237.95.231` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.237.95.231&port=443&secret=ee4571396297582727452bf660db01b789676f6f676c652e636f6d) |
| 6 | `146.185.209.244` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=146.185.209.244&port=443&secret=9f3c7a8d2e4b1c6f5a7d8e9b0c2f4a1d) |
| 8 | `go.bolshevps.su` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=go.bolshevps.su&port=443&secret=ee617782cbbfb6dcc27b0e338f570da65f6164732e78352e7275) |
| 10 | `195.254.165.243` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.243&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 11 | `204.168.176.214` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=204.168.176.214&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 12 | `147.125.130.63` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=147.125.130.63&port=2083&secret=ee1603010200010001fc030386e24c3add68656c702e737465616d706f77657265642e636f6d) |
| 13 | `5.78.93.16` | `4415` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.78.93.16&port=4415&secret=dd104462821249bd7ac519130220c25d09) |
| 14 | `hyper.happvpn.cc` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hyper.happvpn.cc&port=8443&secret=ee4852c1c04ab83db8a328c60eaf9a0db268797065722e6861707076706e2e6363) |
| 15 | `147.125.130.19` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=147.125.130.19&port=2083&secret=ee1603010200010001fc030386e24c3add68656c702e737465616d706f77657265642e636f6d) |
| 16 | `peyk.acharbashi.info` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=peyk.acharbashi.info&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |
| 18 | `dedicated.love-internet.xyz` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dedicated.love-internet.xyz&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |
| 19 | `142.54.189.109` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=142.54.189.109&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 20 | `144.31.230.217` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=144.31.230.217&port=443&secret=33d73370103ea05acd9418eb9dca989e) |


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
