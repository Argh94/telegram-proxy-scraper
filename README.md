# 📊 نتایج استخراج: (آخرین بروزرسانی: 14:36 08-02-1405)

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
| 1 | `own.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=own.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 2 | `win.sosproxy.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=win.sosproxy.space&port=443&secret=ee477ccce74a28c13a2ef6ec9e01510c3164726976652e676f6f676c652e636f6d) |
| 3 | `paitakht.arasto.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=paitakht.arasto.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 4 | `zoomit.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zoomit.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 5 | `108.165.233.137` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=108.165.233.137&port=443&secret=24bd7c651c0cdef3195110f94d4c92ce) |
| 6 | `116.203.134.165` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=116.203.134.165&port=443&secret=ee636c6f7564666c6172652e636f6db6) |
| 7 | `195.254.165.250` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.250&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 8 | `167.86.100.17` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.86.100.17&port=443&secret=eee26c8002852c6d9c74ec17c8532d2dfb636c6f7564666c6172652e636f6d) |
| 9 | `144.91.71.245` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=144.91.71.245&port=443&secret=eeb14be3ca837c27602a22a04e46fd076b636c6f7564666c6172652e636f6d) |
| 10 | `46.225.29.180` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.225.29.180&port=443&secret=ee636c6f7564666c6172652e636f6db6) |
| 11 | `168.222.254.175` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=168.222.254.175&port=443&secret=ec4fb4c5dd112ac95a0aaa51e1bd2745) |
| 12 | `46.225.29.180` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.225.29.180&port=443&secret=ee636c6f7564666c6172652e636f6db6) |
| 13 | `tg.caxero.ru` | `6767` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.caxero.ru&port=6767&secret=fffc0efade691faeaccb0ee0cdbf1773) |
| 14 | `195.254.165.251` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.251&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 15 | `concord.servervless.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=concord.servervless.ru&port=443&secret=ee25cbb92cbe5ef91a21da4e802e60675f6164732e78352e7275) |
| 16 | `142.54.189.106` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=142.54.189.106&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 17 | `80.241.216.110` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=80.241.216.110&port=443&secret=eef689b7cd929fdff0e8e8e897fc79ec8f706574726f766963682e7275) |
| 18 | `tproxyru.live.` | `8980` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tproxyru.live.&port=8980&secret=ee104462821249bd7ac519130220c25d09617669746f2e7275) |
| 20 | `65.109.16.139` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.16.139&port=443&secret=dd104462821249bd7ac519130220c25d09) |


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
