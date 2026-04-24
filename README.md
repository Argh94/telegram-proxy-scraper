# 📊 نتایج استخراج: (آخرین بروزرسانی: 01:18 05-02-1405)

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
| 1 | `79.143.93.219` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.143.93.219&port=8443&secret=ee174f8ad75b1f66755d9fef2e7a02bc987777772e676f6f676c652e636f6d) |
| 2 | `proxy.datamtdatafemida.club` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.datamtdatafemida.club&port=443&secret=ee353f27c43bad4054b23f2837b80c87277777772e676f6f676c652e636f6d) |
| 3 | `46.62.219.0` | `4367` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.62.219.0&port=4367&secret=ee104462821249bd7ac519130220c25d096d61696c2e7275) |
| 4 | `24mt04.mtproxygram.pro` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=24mt04.mtproxygram.pro&port=443&secret=eeb9478b1b5090c520be20ced93d0e816a62726f777365722e79616e6465782e636f6d) |
| 5 | `connect.0xl1r.cfd` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=connect.0xl1r.cfd&port=853&secret=eea1f31ce5039ccb8331e906d5ab00a31777622e7275) |
| 6 | `proxy3.mdnk.fun` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy3.mdnk.fun&port=443&secret=eec547ec12995f5e3501903a74c8c38945706574726f766963682e7275) |
| 7 | `proxy1.mdnk.fun` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy1.mdnk.fun&port=443&secret=eec547ec12995f5e3501903a74c8c38945706574726f766963682e7275) |
| 8 | `prxflow.live` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=prxflow.live&port=443&secret=eed68360458af63073bac1394e8c7a48da707278666c6f772e6c697665) |
| 9 | `2.27.12.157` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.27.12.157&port=443&secret=ee6711534ddf55a427699a01cfc60dcb847777772e77702e706c) |
| 10 | `142.54.189.106` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=142.54.189.106&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 11 | `91.107.189.181` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.189.181&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 12 | `80.241.216.110` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=80.241.216.110&port=443&secret=5baea70d27e7a9d26d9f20ab060fb4f3) |
| 13 | `142.54.189.110` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=142.54.189.110&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 14 | `proxy.pushvpn.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.pushvpn.space&port=443&secret=ee27c7f948bc8c223e13ae240911e783ab7777772e636c6f7564666c6172652e636f6d) |
| 15 | `proxy.proxymtproto.net` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.proxymtproto.net&port=443&secret=dd97caa3c6888366f26b12f994f02ecf1a) |
| 16 | `193.124.58.199` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=193.124.58.199&port=443&secret=eebaeff305618d976e05d4e1d113d249036769746875622e636f6d) |
| 17 | `107.150.34.98` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=107.150.34.98&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 18 | `3.hajrozbeh.onl` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3.hajrozbeh.onl&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 19 | `72.56.238.99` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=72.56.238.99&port=443&secret=3788d8531070b4307f77da398eed8732) |
| 20 | `patrickfriend.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=patrickfriend.online&port=443&secret=eedbe259abc93b59d1f078cebde905309f7061747269636b667269656e642e6f6e6c696e65) |


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
