# 📊 نتایج استخراج: (آخرین بروزرسانی: 04:47 05-09-1405)

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License" />
  <img src="https://img.shields.io/badge/python-3.9-blue" alt="Python 3.11" />
  <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions Welcome" />
  <img src="https://img.shields.io/badge/Proxy%20Scraper-Running-green" alt="Proxy Scraper" />
  <img src="https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/main.yml/badge.svg" alt="Proxy Scraper Workflow" />
  <img src="https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper" alt="GitHub Last Commit" />
  <img src="https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper" alt="GitHub Issues" />
</p>

این پروژه یک اسکریپت پایتون برای جمع‌آوری خودکار پروکسی‌های MTProto تلگرام از منابع متنی و کانال‌های تلگرام است. پروکسی‌ها در فایل `proxy.txt` ذخیره می‌شوند و هر 3 ساعت به‌صورت خودکار به‌روزرسانی می‌شوند.

## ✨ درباره پروژه

این اسکریپت با استفاده از `requests` برای منابع متنی و کانال‌های تلگرام، پروکسی‌های MTProto را جمع‌آوری می‌کند. پروکسی‌های تکراری حذف شده و نتایج در فایل `proxy.txt` ذخیره می‌شوند. این فرآیند به‌صورت خودکار با **GitHub Actions** هر 3 ساعت اجرا می‌شود.

## 🚀 ویژگی‌ها
- 🌐 جمع‌آوری پروکسی از منابع متنی و کانال‌های تلگرام
- 🔄 به‌روزرسانی خودکار هر 3 ساعت
- 🗑 حذف پروکسی‌های تکراری
- 🔑 بدون نیاز به API تلگرام
- 📱 مناسب برای کاربران در جستجوی پروکسی‌های فعال MTProto

## 📋 پیش‌نیازها
- 🐍 پایتون 3.9
- 📦 کتابخانه‌های مورد نیاز: `requests`, `beautifulsoup4`, `pytz`, `jdatetime`
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
| 1 | `79.137.196.223` | `4443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.137.196.223&port=4443&secret=eeee4026e99e99216664b0cb156da676d7707777772e636c6f7564666c6172652e636f6d) |
| 2 | `se.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=se.anotelinopalk.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 3 | `dune.velvetwindow.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dune.velvetwindow.cc&port=443&secret=eed09fb30e9ba945e3eb272875413c8c9464756e652e76656c76657477696e646f772e6363) |
| 4 | `wbs.regmail.org` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=wbs.regmail.org&port=443&secret=ee5610dcb9c93a1c5dd38d965b0462ad2c7762732e7265676d61696c2e6f7267) |
| 5 | `russia.knox-proxy.world` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=russia.knox-proxy.world&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |
| 6 | `irogallery.golgoli1.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=irogallery.golgoli1.co.uk&port=2096&secret=79e344818749bd7ac519130220c25d09) |
| 7 | `valley.paperteapot.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=valley.paperteapot.com&port=443&secret=eed09fb30e9ba945e3eb272875413c8c9476616c6c65792e7061706572746561706f742e636f6d) |
| 8 | `speed.runserver.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=speed.runserver.co.uk&port=8443&secret=79e344818749bd7ac519130220c25d09) |
| 9 | `5.252.118.6` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.252.118.6&port=443&secret=dd794794f1fbbeb7e3cbb6d6c309b799a4) |
| 10 | `name.namenewok.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=name.namenewok.info&port=8443&secret=79e344818749bd7ac519130220c25d09) |
| 11 | `11.new1.ramkal12.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=11.new1.ramkal12.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 12 | `85.133.200.13` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=85.133.200.13&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 15 | `ram7.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ram7.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `support.infinityhalo.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=support.infinityhalo.co.uk&port=8443&secret=79e344818749bd7ac519130220c25d09) |
| 17 | `91.107.170.11` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.170.11&port=8443&secret=79e344818749bd7ac519130220c25d09) |
| 18 | `yek.ionox.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=yek.ionox.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 19 | `dele89.quillmarsh.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dele89.quillmarsh.xyz&port=8443&secret=ee704c9352bad79b00f1e067772277715664726976652e676f6f676c652e636f6d) |
| 20 | `borujerd-tehran-esfahan.miandoabs.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=borujerd-tehran-esfahan.miandoabs.info&port=8443&secret=1603010200010001fc030386e24c3add) |


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
