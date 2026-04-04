# 📊 نتایج استخراج: (آخرین بروزرسانی: 13:09 15-01-1405)

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
| 2 | `146.185.243.42` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=146.185.243.42&port=443&secret=137b5ff6e2d9e9efd467c2da4d1bff2b) |
| 3 | `001.tg.magproxy.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=001.tg.magproxy.com&port=443&secret=dd755e2a560dcbc2b22746d6e02555bc43) |
| 4 | `213.176.94.29` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=213.176.94.29&port=443&secret=ee79612e727533b76a10ec4f6547a7a2) |
| 5 | `2A.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2A.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 6 | `mt.vpn-one.net` | `5223` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.vpn-one.net&port=5223&secret=7ae73ddfd70b8e549aae657b4da1bf03) |
| 7 | `95.216.28.120` | `6800` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.216.28.120&port=6800&secret=4dcebaabeb692bdc9ad03486b090da76) |
| 8 | `27289292.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=27289292.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 9 | `takhtekhab.rylvin.bar` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=takhtekhab.rylvin.bar&port=443&secret=5839ef5285c1a55062cc35f9197003cb) |
| 10 | `proxium.rest` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxium.rest&port=443&secret=a665a45920422f9d417e4867efdc4fb8) |
| 11 | `s3.fluctuation.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s3.fluctuation.online&port=443&secret=eedd345afe9188a4e5a94dc706e1aa6cef78352e7275) |
| 12 | `telegrammessenger_proxy.dimasssss.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=telegrammessenger_proxy.dimasssss.space&port=443&secret=ddbe3007e927acd147dde12bee8b1a7c93) |
| 13 | `80.249.131.53` | `3232` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=80.249.131.53&port=3232&secret=dd3e0848dc48c09f0a8731af8c088fc5f5) |
| 14 | `laura.proxyprosto.sbs` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=laura.proxyprosto.sbs&port=443&secret=ee79612e7275dcdfd8017f6ee7c1beb0) |
| 15 | `laura.proxyprosto.sbs` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=laura.proxyprosto.sbs&port=443&secret=ee79612e7275dcdfd8017f6ee7c1beb0) |
| 16 | `tg.just-cloud.org` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.just-cloud.org&port=443&secret=10728fb49a2145f8b91abfb451283adf) |
| 17 | `84.201.173.20` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=84.201.173.20&port=443&secret=9b31714333fcb181199fc46f9cb8068d) |
| 18 | `zoomit.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zoomit.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 19 | `46.225.29.180` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.225.29.180&port=443&secret=ee636c6f7564666c6172652e636f6db6) |


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
