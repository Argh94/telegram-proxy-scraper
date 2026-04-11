# 📊 نتایج استخراج: (آخرین بروزرسانی: 05:42 22-01-1405)

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
| 1 | `95.217.25.41` | `35432` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.217.25.41&port=35432&secret=ee104462821249bd7ac519130220c25d096d61782e7275) |
| 3 | `195.254.165.243` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.243&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 5 | `s3.fluctuation.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s3.fluctuation.online&port=443&secret=eedd345afe9188a4e5a94dc706e1aa6cef78352e7275) |
| 6 | `144.31.156.180` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=144.31.156.180&port=443&secret=f229d48c8d5bfd189b8439894bcc6bb7) |
| 7 | `142.54.189.107` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=142.54.189.107&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 9 | `hi.notmescat.net` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hi.notmescat.net&port=7443&secret=ee4b9ba5fcb813d00ef6f7c5a0302f182f68692e6e6f746d65736361742e6e6574) |
| 10 | `195.254.165.247` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.247&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 11 | `2.26.49.102` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.26.49.102&port=443&secret=f6c4563d6f3d67137a1c286b7d92fa0f) |
| 12 | `136.244.109.78` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=136.244.109.78&port=8443&secret=eecf6ad6e4f27809043ee93b578fc71947646c2e676f6f676c652e636f6d) |
| 14 | `149.120.147.240` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=149.120.147.240&port=443&secret=ee6719f637173dc2276468b703e739f00e7777772e62696e672e636f6d) |
| 15 | `185.23.19.86` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.23.19.86&port=443&secret=cd29cc6379a3e9d20205c1386e2aa683) |
| 16 | `handbell.jude.meet.motoring.shake-up.watchpinoyteleserye.com` | `1150` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=handbell.jude.meet.motoring.shake-up.watchpinoyteleserye.com&port=1150&secret=9c3dd2c3b66976461382216193e8e323) |
| 17 | `i.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=i.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 18 | `38.28.140.150` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=38.28.140.150&port=443&secret=ee14c815be04f1c6bddd220f15c86f5e487777772e6170706c652e636f6d) |
| 19 | `peyk.acharbashi.info` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=peyk.acharbashi.info&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |
| 20 | `taxt.techlibrary.ink` | `4501` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=taxt.techlibrary.ink&port=4501&secret=eeaf939bf55aac4eef8c4bee578bdc09f6626973636f7474692e79656b74616e65742e636f6d) |


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
