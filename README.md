# 📊 نتایج استخراج: (آخرین بروزرسانی: 09:25 26-02-1405)

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
| 1 | `espress0-macch1ato-p0r-favor3.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=espress0-macch1ato-p0r-favor3.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 2 | `144.31.221.15` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=144.31.221.15&port=443&secret=b2d53412432435cd7d8e90b4d0821d60) |
| 4 | `195.254.165.253` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.253&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 5 | `tproxyru.live.` | `8980` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tproxyru.live.&port=8980&secret=ee104462821249bd7ac519130220c25d09617669746f2e7275) |
| 6 | `2.27.22.112` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.27.22.112&port=443&secret=ee17ea0a2562ea669ebe7308ee7f9ae63b706574726f766963682e7275) |
| 7 | `germany.tgproxysokol.pro` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=germany.tgproxysokol.pro&port=8443&secret=ee4215d16e455242e9b5ffb6349df285d06164732e78352e7275) |
| 8 | `lovevesper.zoryx.tech` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lovevesper.zoryx.tech&port=853&secret=ee2a43151ca1c75d56a2f8f63c87bfaae374726176656c6c696e652e7275) |
| 9 | `mt.rimuruproject.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.rimuruproject.ru&port=443&secret=ee0b32a6d19fd9f1c1f8b3e48c8638a29c79612e7275) |
| 10 | `vfast.proxytg.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vfast.proxytg.space&port=443&secret=ee4b3ce8c172e8a23ff5f953069ef6c38a64726976652e676f6f676c652e636f6d) |
| 11 | `proxy.fluxoria.it.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.fluxoria.it.com&port=443&secret=ee307242dd41275c771f40035565d0750a70726f78792e666c75786f7269612e69742e636f6d) |
| 12 | `connect.tproxyru.live` | `8980` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=connect.tproxyru.live&port=8980&secret=ee104462821249bd7ac519130220c25d09617669746f2e7275) |
| 13 | `mtp.love-pussy.online` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtp.love-pussy.online&port=853&secret=eeb6506e69d11db32d81c215a14850a1947777772e666173746c792e636f6d) |
| 14 | `proxy.fluxoria.it.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.fluxoria.it.com&port=443&secret=ee307242dd41275c771f40035565d0750a70726f78792e666c75786f7269612e69742e636f6d) |
| 16 | `87.120.108.38` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.120.108.38&port=443&secret=f212b4ee21a6f1026aadae4ce0b08f98) |
| 17 | `hello.proxytg.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hello.proxytg.space&port=443&secret=ee57b7509fe484325abedc85f18804843768656c6c6f2e70726f787974672e7370616365) |
| 18 | `195.254.165.247` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.247&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 19 | `50.7.41.162` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=50.7.41.162&port=443&secret=ee011808bcccfd224644ca7f231846a7d46d61782e7275) |
| 20 | `f1.kurduk.store` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=f1.kurduk.store&port=443&secret=ee1e34c689f1f76dff1f2ae4aefb4c6848706574726f766963682e7275) |


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
