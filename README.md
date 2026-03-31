# 📊 نتایج استخراج: (آخرین بروزرسانی: 16:49 11-01-1405)

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
| 1 | `116.203.134.165` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=116.203.134.165&port=443&secret=ee636c6f7564666c6172652e636f6db6) |
| 2 | `107.150.34.99` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=107.150.34.99&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 3 | `185.174.137.50` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.174.137.50&port=8443&secret=676c4049812b842b7792954bf2a32943) |
| 5 | `107.150.34.98` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=107.150.34.98&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 6 | `free.tgsecurity.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=free.tgsecurity.online&port=443&secret=dd7c5d4e1f2a3b9c8d7e6f5a4b3c2d1e0f) |
| 7 | `Fast.love-internet.xyz` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Fast.love-internet.xyz&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |
| 8 | `31.130.151.16` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=31.130.151.16&port=443&secret=4931e9e6000537266a0de4dbb81f81fa) |
| 9 | `178.104.98.160` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.104.98.160&port=443&secret=ee636c6f7564666c6172652e636f6db6) |
| 10 | `de-03.satoshidiary.org` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=de-03.satoshidiary.org&port=8443&secret=ee6d33147f1bbc63e9b39efe483516ab85617669746f2e7374) |
| 11 | `142.132.232.226` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=142.132.232.226&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 12 | `dedicated.love-internet.xyz` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dedicated.love-internet.xyz&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |
| 13 | `linkera.948141.xyz` | `1337` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=linkera.948141.xyz&port=1337&secret=dd26b68f6bd3fe200284f654574260f09b) |
| 14 | `proxium.rest` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxium.rest&port=443&secret=a665a45920422f9d417e4867efdc4fb8) |
| 16 | `rkn.tg` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rkn.tg&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 17 | `proxytop.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxytop.space&port=443&secret=7d793037a0760186574b0282f2f435e7) |
| 19 | `44.223.90.89` | `80` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=44.223.90.89&port=80&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `go.bolshevps.su` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=go.bolshevps.su&port=443&secret=ee617782cbbfb6dcc27b0e338f570da65f6164732e78352e7275) |


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
