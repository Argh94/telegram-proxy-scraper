# 📊 نتایج استخراج: (آخرین بروزرسانی: 12:00 03-03-1405)

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
| 2 | `91.107.189.181` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.189.181&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `in.mythical.house` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=in.mythical.house&port=443&secret=eeecc03a8eabe3443a254a09bcd5681d75696e2e6d7974686963616c2e686f757365) |
| 4 | `87.120.108.38` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.120.108.38&port=443&secret=f212b4ee21a6f1026aadae4ce0b08f98) |
| 5 | `2.26.99.245` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.26.99.245&port=8443&secret=ee17263409876123456712342349876554322e32362e39392e323435) |
| 7 | `178.105.141.172` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.105.141.172&port=443&secret=ee8db761231b91c7c07ac0a6e7323ad41b676f6f676c65617069732e636f6d) |
| 8 | `91.84.127.166` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.84.127.166&port=443&secret=eee1c9c22f43146f765430cbd63d40cdc37777772e79616e6465782e7275) |
| 9 | `premium1.fsproxy.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=premium1.fsproxy.site&port=443&secret=eed29605852bf2e034c63c6f866062600f696e2e6d7974686963616c2e686f757365) |
| 10 | `2.27.22.112` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.27.22.112&port=443&secret=ee17ea0a2562ea669ebe7308ee7f9ae63b706574726f766963682e7275) |
| 11 | `89.125.113.189` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.125.113.189&port=443&secret=ee19835aa301cd9a6ceb68ad8d5ad9e0ac79616e6465782e7275) |
| 12 | `mtp.yard-tg-bot.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtp.yard-tg-bot.ru&port=443&secret=eef658bb6d89b284874149c13e7d27d9da79616e6465782e7275) |
| 13 | `194.50.94.98` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.50.94.98&port=443&secret=ee75a53853cb3f53976737c82a53d4f13879616e6465782e7275) |
| 14 | `www.tproxy.ink` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.tproxy.ink&port=443&secret=ee104462821249bd7ac519130220c25d09617669746f2e7275) |
| 16 | `91.107.189.181` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.189.181&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `185.224.215.250` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.224.215.250&port=443&secret=eea1b2c3d4e5f60123456789adadad432173332e616d617a6f6e6177732e636f6d) |
| 18 | `178.105.168.17` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.105.168.17&port=443&secret=eeb67e98429f3ba8896ff33ab9ff9d18a1676f6f676c65617069732e636f6d) |
| 19 | `37.27.38.205` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=37.27.38.205&port=443&secret=ee9d659fc2ae43e0b8323c082960233d7b7777772e636c6f7564666c6172652e636f6d) |
| 20 | `185.147.127.50` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.147.127.50&port=443&secret=eec11798ab008831b474066c9e1ebf5c81617669746f2e7275) |


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
