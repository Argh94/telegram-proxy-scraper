# 📊 نتایج استخراج: (آخرین بروزرسانی: 16:50 18-01-1405)

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
| 2 | `107.150.34.101` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=107.150.34.101&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 3 | `45.63.37.198` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.63.37.198&port=443&secret=34f66fe0a25afe45d9310e4b2641bc5f) |
| 4 | `2A.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2A.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 5 | `94.130.190.170` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=94.130.190.170&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `82.152.162.9` | `10002` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=82.152.162.9&port=10002&secret=ee548593a9c0688f4f7d9d57377897d964636c6f7564666c6172652e636f6d) |
| 7 | `proxytop.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxytop.space&port=443&secret=7d793037a0760186574b0282f2f435e7) |
| 8 | `149.120.147.188` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=149.120.147.188&port=443&secret=ee6719f637173dc2276468b703e739f00e7777772e62696e672e636f6d) |
| 9 | `149.28.196.187` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=149.28.196.187&port=443&secret=9d1b239f1211789f80f3ad715e575129) |
| 10 | `107.150.34.100` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=107.150.34.100&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 11 | `s3.neo-trading.org` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s3.neo-trading.org&port=443&secret=eec3fefd89a25d37ca3af1a602c7bfd8de79612e7275) |
| 12 | `82.152.162.14` | `10002` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=82.152.162.14&port=10002&secret=ee548593a9c0688f4f7d9d57377897d964636c6f7564666c6172652e636f6d) |
| 13 | `142.54.189.106` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=142.54.189.106&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 15 | `px.spektr.win` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=px.spektr.win&port=443&secret=ee370baecb228874e0fe5b4a32a9a95ed0646c2e676f6f676c652e636f6d) |
| 16 | `172.65.117.172` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.65.117.172&port=22&secret=dd79e344818749bd7ac519130220c25d09) |
| 17 | `185.84.156.90` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.84.156.90&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e6d61782e7275) |
| 18 | `psql.s1nqq.fun` | `5432` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=psql.s1nqq.fun&port=5432&secret=0e5360aecceecd4c27f7acd6aa79a7d5) |
| 19 | `107.150.34.99` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=107.150.34.99&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 20 | `45.32.91.56` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.32.91.56&port=443&secret=b6b84f3587029551fc8e0ff081e7903f) |


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
