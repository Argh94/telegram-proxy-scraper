# 📊 نتایج استخراج: (آخرین بروزرسانی: 23:16 24-02-1405)

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
| 1 | `mtp.love-pussy.online` | `8980` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtp.love-pussy.online&port=8980&secret=eeb6506e69d11db32d81c215a14850a194617669746f2e7275) |
| 2 | `132.243.235.194` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.235.194&port=443&secret=eebbef585db7c10242e5b3654910e1d91479616e6465782e7275) |
| 3 | `mtp.fsoc-app.online` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtp.fsoc-app.online&port=853&secret=ee1d49946a9bd11022149e2c68f1d75f6774656c2e66736f632d6170702e6f6e6c696e65) |
| 4 | `87.120.108.48` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.120.108.48&port=443&secret=074e7d1d37cc043746fd0c823f20d21a) |
| 5 | `194.50.94.98` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.50.94.98&port=443&secret=ee75a53853cb3f53976737c82a53d4f13879616e6465782e7275) |
| 6 | `50.7.41.162` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=50.7.41.162&port=443&secret=ee011808bcccfd224644ca7f231846a7d46d61782e7275) |
| 7 | `s.arixo.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s.arixo.shop&port=443&secret=eec11798ab008831b474066c9e1ebf5c997777772e617669746f2e7275) |
| 8 | `s1.proxytg.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s1.proxytg.space&port=443&secret=ee481fc4aa7c63d939142d4dbf07e1aac464726976652e676f6f676c652e636f6d) |
| 9 | `89.125.113.155` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.125.113.155&port=443&secret=ee67af7b545eb72c3c47fc2ccb74aa41c979616e6465782e7275) |
| 10 | `87.120.108.48` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.120.108.48&port=443&secret=074e7d1d37cc043746fd0c823f20d21a) |
| 11 | `195.254.165.143` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.143&port=4455&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d) |
| 12 | `195.254.165.253` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.253&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 14 | `mt.corph.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.corph.ru&port=443&secret=ee2ed7517b077ef414e24b106e0729335d6d742e636f7270682e7275) |
| 15 | `89.125.48.232` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.125.48.232&port=443&secret=ee72f3ca54320d22b0c5d8daf53168962d706574726f766963682e7275) |
| 16 | `fit.proxytg.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fit.proxytg.space&port=443&secret=ee0ea320b5c19fb4f014bb1514baeb49da64726976652e676f6f676c652e636f6d) |
| 17 | `predator-artist.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=predator-artist.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 18 | `132.243.235.190` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.235.190&port=443&secret=ee157938a8c2f93afd4880d5bc6a1c8da279616e6465782e7275) |
| 19 | `132.243.235.196` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.235.196&port=443&secret=ee5895bbd18604365e8d18b63af6c3bfbe79616e6465782e7275) |
| 20 | `proxy.fluxoria.it.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.fluxoria.it.com&port=443&secret=ee307242dd41275c771f40035565d0750a70726f78792e666c75786f7269612e69742e636f6d) |


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
