# 📊 نتایج استخراج: (آخرین بروزرسانی: 14:57 11-04-1405)

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
| 1 | `167.233.179.218` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.233.179.218&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `stars.tg-proxy.fun` | `6443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=stars.tg-proxy.fun&port=6443&secret=a545c35eb2bdfa1a93df5ebe69957120) |
| 3 | `194.77.70.81` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.77.70.81&port=8080&secret=1603010200010001fc030386e24c3add) |
| 4 | `nab.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nab.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `portal.malevich7.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=portal.malevich7.top&port=443&secret=ee11a238b08b4be3863afe578bcbe7a6f9706f7274616c2e6d616c6576696368372e746f70) |
| 7 | `dena-plus-auto.denatara.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dena-plus-auto.denatara.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 10 | `Www.merco-karco.website` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Www.merco-karco.website&port=443&secret=ee1603010200010001fc030386e24c3add626973636F7474692E79656B74616E65742E636F6D) |
| 12 | `blond.basicscotch.co.uk` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=blond.basicscotch.co.uk&port=25565&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 13 | `138.124.33.176` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=138.124.33.176&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 14 | `167.233.179.218` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.233.179.218&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `rain.golgoli2.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rain.golgoli2.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add7777772e7961686f6f2e636f6d) |
| 16 | `borj-pooshak-brj.aseman.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=borj-pooshak-brj.aseman.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 17 | `app.kvakzon.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=app.kvakzon.top&port=443&secret=ee5b0fbf6320bd9abf4c494f0a5e5d36a16170702e6b76616b7a6f6e2e746f70) |
| 18 | `borj-pooshak-brj.aseman.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=borj-pooshak-brj.aseman.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 19 | `book.malavanann.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=book.malavanann.co.uk&port=2096&secret=ee1603010200010001fc030386e24c3add7777772e7961686f6f2e636f6d) |
| 20 | `just-money.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=just-money.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |


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
