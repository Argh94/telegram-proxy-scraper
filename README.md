# 📊 نتایج استخراج: (آخرین بروزرسانی: 08:21 15-01-1405)

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
| 2 | `s3.fluctuation.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s3.fluctuation.online&port=443&secret=eedd345afe9188a4e5a94dc706e1aa6cef78352e7275) |
| 3 | `66.135.2.114` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=66.135.2.114&port=443&secret=bbdd3ba2140d7a4de7fe4f38d08d4d28) |
| 4 | `46.225.29.180` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.225.29.180&port=443&secret=ee636c6f7564666c6172652e636f6db6) |
| 5 | `laura.proxyprosto.sbs` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=laura.proxyprosto.sbs&port=443&secret=ee79612e7275dcdfd8017f6ee7c1beb0) |
| 6 | `45.82.65.142` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.82.65.142&port=443&secret=a7c17e9a495ef47028c1c57f4c4a9d5e) |
| 7 | `telegrammessenger_proxy.dimasssss.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=telegrammessenger_proxy.dimasssss.space&port=443&secret=ddbe3007e927acd147dde12bee8b1a7c93) |
| 8 | `proxytop.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxytop.space&port=443&secret=7d793037a0760186574b0282f2f435e7) |
| 9 | `45.90.13.34` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.90.13.34&port=443&secret=dda85f2776cc83dbff66b440fb03050cf7) |
| 10 | `hyper.happvpn.cc` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hyper.happvpn.cc&port=8443&secret=ee4852c1c04ab83db8a328c60eaf9a0db268797065722e6861707076706e2e6363) |
| 11 | `tg.vpnspacev.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.vpnspacev.com&port=443&secret=bc184fc14b62b9b1dc5f34edf9476421) |
| 12 | `mix.nuv.su` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mix.nuv.su&port=443&secret=ee470cb2b8b29aeadfbdf8a2f7bee5ca3b62726f777365722e79616e6465782e636f6d) |
| 13 | `laura.proxyprosto.sbs` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=laura.proxyprosto.sbs&port=443&secret=ee79612e7275dcdfd8017f6ee7c1beb0) |
| 14 | `proxy2.21freedom.net` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy2.21freedom.net&port=443&secret=6e7f2b10a1bc3738692d619ba3df3b7f) |
| 15 | `212.233.74.109` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=212.233.74.109&port=443&secret=eedb3fe4bf0ed595882e36d26015268f346d61782e7275) |
| 16 | `45.32.174.107` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.32.174.107&port=443&secret=039fd728a788500de9d5ca40f4c8adf5) |
| 17 | `27289292.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=27289292.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 18 | `213.176.94.29` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=213.176.94.29&port=443&secret=ee79612e727533b76a10ec4f6547a7a2) |
| 19 | `65.109.16.139` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.16.139&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `proxydazhenaparkovke.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxydazhenaparkovke.site&port=443&secret=dde8aa2e8c1ad50570b7d6fe7e0ba3d677) |


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
