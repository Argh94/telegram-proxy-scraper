# 📊 نتایج استخراج: (آخرین بروزرسانی: 23:00 10-04-1405)

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License" />
  <img src="https://img.shields.io/badge/python-3.9-blue" alt="Python 3.11" />
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
| 3 | `tabibie.del.davazdah.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tabibie.del.davazdah.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 4 | `permiiium.lavazemi2.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=permiiium.lavazemi2.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add7777772e7961686f6f2e636f6d) |
| 5 | `book.malavanann.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=book.malavanann.co.uk&port=2053&secret=ee1603010200010001fc030386e24c3add706c61792e676f6f676c652e636f6d) |
| 6 | `mmd.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mmd.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `3.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3.telbet.lol&port=25565&secret=dd79e7010200010007f0030386e24c3add) |
| 8 | `edge.ehtemal.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=edge.ehtemal.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 10 | `secure.medhata.org` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=secure.medhata.org&port=443&secret=eea19617d5c2e4a7ea104cd317777acd1b7365637572652e6d6564686174612e6f7267) |
| 11 | `87.120.216.254` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.120.216.254&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 13 | `login.veltura.digital` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=login.veltura.digital&port=443&secret=ee381874396c547235c4be1e40cb6132976c6f67696e2e76656c747572612e6469676974616c) |
| 14 | `87.229.56.182` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.229.56.182&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 15 | `d4a7c1f8-3e9b-425d-a1c6-9f8e2b7a4d5c.casa` | `80` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=d4a7c1f8-3e9b-425d-a1c6-9f8e2b7a4d5c.casa&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d) |
| 16 | `blond.basicscotch.co.uk` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=blond.basicscotch.co.uk&port=25565&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 18 | `lux.lavazemi1.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lux.lavazemi1.co.uk&port=2096&secret=ee1603010200010001fc030386e24c3add7777772e7961686f6f2e636f6d) |
| 19 | `brivora.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=brivora.co.uk.&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |


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
