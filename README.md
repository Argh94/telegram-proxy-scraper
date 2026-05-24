# 📊 نتایج استخراج: (آخرین بروزرسانی: 19:32 03-03-1405)

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
| 1 | `2.27.41.207` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.27.41.207&port=443&secret=9436fa39ab47ccb34f217ac6d06b4e58) |
| 2 | `mt.rimuruproject.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.rimuruproject.ru&port=443&secret=ee0b32a6d19fd9f1c1f8b3e48c8638a29c79612e7275) |
| 3 | `www.tproxy.ink` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.tproxy.ink&port=443&secret=ee104462821249bd7ac519130220c25d09617669746f2e7275) |
| 4 | `2.26.99.245` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.26.99.245&port=8443&secret=ee17263409876123456712342349876554322e32362e39392e323435) |
| 5 | `194.50.94.65` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.50.94.65&port=443&secret=ee0c534d144bf266c6b7a09c532a2e529f79616e6465782e7275) |
| 7 | `s.proxytg.space` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s.proxytg.space&port=8443&secret=eefefc4f17248e59437bb451447a9170b2732e70726f787974672e7370616365) |
| 8 | `2.27.22.112` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.27.22.112&port=443&secret=ee17ea0a2562ea669ebe7308ee7f9ae63b706574726f766963682e7275) |
| 9 | `72.56.70.7` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=72.56.70.7&port=443&secret=eec11798ab008831b474066c9e1ebf5c99617669746f2e7275) |
| 11 | `132.243.235.194` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.235.194&port=443&secret=eebbef585db7c10242e5b3654910e1d91479616e6465782e7275) |
| 12 | `s.rkn.tg` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s.rkn.tg&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 13 | `www.tproxy.mom` | `8090` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.tproxy.mom&port=8090&secret=ee104462821249bd7ac519130220c25d09617669746f2e7275) |
| 15 | `dreams.nolags.pw` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dreams.nolags.pw&port=443&secret=dd2d558135931b5e0c5da5e7501724b32c) |
| 16 | `tproxy.ink` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tproxy.ink&port=443&secret=ee104462821249bd7ac519130220c25d09617669746f2e7275) |
| 18 | `tproxy.mom` | `8090` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tproxy.mom&port=8090&secret=ee104462821249bd7ac519130220c25d09617669746f2e7275) |
| 19 | `speed.chunkycorp.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=speed.chunkycorp.shop&port=443&secret=ee3a3365be03d6bc13518d65e70a3146c2617669746f2e7275) |
| 20 | `178.104.81.34` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.104.81.34&port=4455&secret=dd104462821249bd7ac519130220c25d09) |


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
