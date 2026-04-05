# 📊 نتایج استخراج: (آخرین بروزرسانی: 10:37 16-01-1405)

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
| 2 | `vavan.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vavan.online&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `72.56.250.221` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=72.56.250.221&port=443&secret=eeff0c592463b7a03b31ce7fec93460449706574726f766963682e7275) |
| 5 | `91.149.241.35` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.149.241.35&port=443&secret=eed95a7f7f310f44feab4f9d1a8a703f536769746875622e636f6d) |
| 6 | `45.90.13.34` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.90.13.34&port=443&secret=dda85f2776cc83dbff66b440fb03050cf7) |
| 7 | `dowd.sportsmanship.steeplechaser.thy.urceolate.kapitoshka.info` | `15417` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dowd.sportsmanship.steeplechaser.thy.urceolate.kapitoshka.info&port=15417&secret=d6db8ab62ff9b9f70f6ca15ccb98c222) |
| 8 | `prx.today` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=prx.today&port=443&secret=b3f0c7f6af7dc2dc2e9c80d0d80e8162) |
| 10 | `172.65.117.172` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.65.117.172&port=22&secret=dd79e344818749bd7ac519130220c25d09) |
| 11 | `2.27.23.23` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.27.23.23&port=8443&secret=f5a97ceadd1bbedd918fbd9f1c9387dd) |
| 12 | `proxyobhod.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxyobhod.online&port=443&secret=71c30cc28759e0a10b6de5b471d69751) |
| 13 | `185.237.95.231` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.237.95.231&port=443&secret=ee4571396297582727452bf660db01b789676f6f676c652e636f6d) |
| 15 | `64.188.61.194` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=64.188.61.194&port=443&secret=ee4571396297582727452bf660db01b789676f6f676c652e636f6d) |
| 16 | `jp.767958.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jp.767958.xyz&port=443&secret=ee8eddf64a864c234ef6cdc41dfb1513b4617a7572652e6d6963726f736f66742e636f6d) |
| 19 | `190.2.142.185` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=190.2.142.185&port=8443&secret=63f84be1fa69afb85f70d273f3e4d557) |
| 20 | `146.19.84.206` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=146.19.84.206&port=443&secret=ce2e89216193d0072e19f8a776e37dee) |


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
