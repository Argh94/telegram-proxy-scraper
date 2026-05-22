# 📊 نتایج استخراج: (آخرین بروزرسانی: 12:53 01-03-1405)

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
| 1 | `185.224.215.250` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.224.215.250&port=443&secret=eea1b2c3d4e5f60123456789adadad432173332e616d617a6f6e6177732e636f6d) |
| 2 | `204.168.129.90` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=204.168.129.90&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `pepel.help` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pepel.help&port=443&secret=eea890920f5ac6ba5834725e150d06c4aa64726976652e676f6f676c652e636f6d) |
| 4 | `mt.corph.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.corph.ru&port=443&secret=ee2ed7517b077ef414e24b106e0729335d6d742e636f7270682e7275) |
| 5 | `138.124.127.157` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=138.124.127.157&port=443&secret=ee776ed6e05e7099a53f923bdcc99f659e766b2e636f6d) |
| 6 | `espress0-macch1ato-p0r-favor3.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=espress0-macch1ato-p0r-favor3.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 7 | `178.105.141.172` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.105.141.172&port=443&secret=ee8db761231b91c7c07ac0a6e7323ad41b676f6f676c65617069732e636f6d) |
| 8 | `185.182.82.73` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.182.82.73&port=443&secret=ee586cb8c65dc8c78f50bd4e573ae25f4873332e616d617a6f6e6177732e636f6d) |
| 9 | `194.50.94.98` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.50.94.98&port=443&secret=ee75a53853cb3f53976737c82a53d4f13879616e6465782e7275) |
| 10 | `89.125.113.189` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.125.113.189&port=443&secret=ee19835aa301cd9a6ceb68ad8d5ad9e0ac79616e6465782e7275) |
| 11 | `free.proproxies.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=free.proproxies.top&port=443&secret=ee4fb60224ec3ba77691889623ffd44dc8667265652e70726f70726f786965732e746f70) |
| 12 | `mt.shifor.live` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.shifor.live&port=443&secret=eee1de11495a1f99a91c4ee0c863252b586d742e736869666f722e6c697665) |
| 13 | `menf.proxytg.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=menf.proxytg.space&port=443&secret=eed29c1cae809aca8bdbf6ce5c5918141c6d61782e7275) |
| 14 | `hop1.proxytg.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hop1.proxytg.space&port=443&secret=ee7e6c3f99b8b56d5aece5326877a3793a6d61782e7275) |
| 15 | `92.118.234.215` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=92.118.234.215&port=443&secret=dddb9b51b5ce9a2820ff62d348cb23f1b9) |
| 16 | `37.27.38.205` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=37.27.38.205&port=443&secret=ee9d659fc2ae43e0b8323c082960233d7b7777772e636c6f7564666c6172652e636f6d) |
| 17 | `y0u-found-a-way-ou7-of-gorphosts-lockd0wn.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=y0u-found-a-way-ou7-of-gorphosts-lockd0wn.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 18 | `mt.rimuruproject.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.rimuruproject.ru&port=443&secret=ee0b32a6d19fd9f1c1f8b3e48c8638a29c79612e7275) |
| 19 | `artt.proxytg.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=artt.proxytg.space&port=443&secret=ee859265446d8bb72e53291612281d57e26d61782e7275) |
| 20 | `87.120.108.38` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.120.108.38&port=443&secret=f212b4ee21a6f1026aadae4ce0b08f98) |


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
