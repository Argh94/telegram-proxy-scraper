# 📊 نتایج استخراج: (آخرین بروزرسانی: 17:17 18-02-1405)

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
| 1 | `yazdan.htop.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=yazdan.htop.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 2 | `i-love-cu.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=i-love-cu.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 4 | `tgobhod.forum` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tgobhod.forum&port=443&secret=ee1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d74676f62686f642e666f72756d) |
| 5 | `64.188.65.136` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=64.188.65.136&port=443&secret=eec11798ab008831b474066c9e1ebf5c997777772e78352e7275) |
| 6 | `194.50.94.65` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.50.94.65&port=443&secret=ee0c534d144bf266c6b7a09c532a2e529f79616e6465782e7275) |
| 7 | `132.243.235.196` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.235.196&port=443&secret=ee5895bbd18604365e8d18b63af6c3bfbe79616e6465782e7275) |
| 8 | `132.243.235.143` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.235.143&port=443&secret=ee1a043ca04520458fe7fc96309b095f3679616e6465782e7275) |
| 9 | `proxytg.live` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxytg.live&port=443&secret=ee347358dc309fbf96304b28460ef7cd7a70726f787974672e6c697665) |
| 10 | `s5.proxyru.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s5.proxyru.top&port=443&secret=eefe281d2bfa13f991ed6be43138e5e14c79612e7275) |
| 11 | `2A.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2A.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 12 | `77.239.125.158` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=77.239.125.158&port=443&secret=ee15465e6f97a4ca60ab5db03332290d6b77622e7275) |
| 13 | `89.125.113.9` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.125.113.9&port=443&secret=ee270da96d88f34c5719b892a3b1ce156379616e6465782e7275) |
| 14 | `27289292.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=27289292.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 16 | `89.125.113.8` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.125.113.8&port=443&secret=eeb9e6c48a8244eecdb64a7422108aebeb79616e6465782e7275) |
| 17 | `how.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=how.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 18 | `132.243.235.188` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.235.188&port=443&secret=eecff01a06513433100e81c6eadff452e779616e6465782e7275) |
| 19 | `89.125.113.13` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.125.113.13&port=443&secret=ee565b72a7140d98fd8cc18ab30245b23379616e6465782e7275) |
| 20 | `3.hajrozbeh.onl` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3.hajrozbeh.onl&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |


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
