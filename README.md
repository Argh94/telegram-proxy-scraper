# 📊 نتایج استخراج: (آخرین بروزرسانی: 01:02 07-01-1405)

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
| 1 | `144.31.202.189` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=144.31.202.189&port=443&secret=ee766b2e727522c79c0d8e5e0d0a1ea3) |
| 2 | `185.214.74.147` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.214.74.147&port=443&secret=ee663a55116e71d57f9655312ae65c2ea4646c2e676f6f676c652e636f6d) |
| 4 | `204.168.176.214` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=204.168.176.214&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `dedicated.love-internet.xyz` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dedicated.love-internet.xyz&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |
| 6 | `195.254.165.252` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.252&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 7 | `107.150.34.102` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=107.150.34.102&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 9 | `tg.towersflowerss.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.towersflowerss.com&port=443&secret=90eba2e23b01f1cb32b4b9e29bbd7f80) |
| 11 | `tg.vpnspacev.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.vpnspacev.com&port=443&secret=bc184fc14b62b9b1dc5f34edf9476421) |
| 12 | `147.125.130.63` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=147.125.130.63&port=2083&secret=ee1603010200010001fc030386e24c3add68656c702e737465616d706f77657265642e636f6d) |
| 13 | `146.103.107.95` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=146.103.107.95&port=8443&secret=dd653799bd79e146d8e7558ebdeaf73dbd) |
| 15 | `mtproto.eu` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtproto.eu&port=443&secret=bd22cd34081c9420e8515a153186e632) |
| 16 | `43.250.53.22` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=43.250.53.22&port=443&secret=4fc30d1222972a04067e805a5134cb57) |
| 18 | `www.qatar-railways.info.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.qatar-railways.info.&port=443&secret=ee79e7010200010007f0030386e24c3add68656c702e737465616d706f77657265642e636f6d) |
| 19 | `64.188.61.194` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=64.188.61.194&port=443&secret=ee4571396297582727452bf660db01b789676f6f676c652e636f6d) |
| 20 | `tg.scroogevpn.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.scroogevpn.com&port=443&secret=59d307276beb8f4d8a0ed547eb6a461a) |


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
