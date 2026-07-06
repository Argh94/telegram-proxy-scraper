# 📊 نتایج استخراج: (آخرین بروزرسانی: 01:37 16-04-1405)

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
| 1 | `top.jamejanhani2.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=top.jamejanhani2.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 2 | `194.233.94.9` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.233.94.9&port=443&secret=eee3727d72c23452d6928e9a5ea16f0940676f6f676c65617069732e636f6d) |
| 3 | `188.40.68.169` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=188.40.68.169&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `kalakbaz.kalakbazi-co.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kalakbaz.kalakbazi-co.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add626973636F7474692E79656B74616E65742E636F6D) |
| 5 | `194.77.70.23` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.77.70.23&port=8080&secret=dd1603010200010001fc030386e24c3add) |
| 6 | `noron.jamejanhani1.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=noron.jamejanhani1.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 7 | `sv7.hajhossein.observer` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sv7.hajhossein.observer&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 9 | `win.golgoli1.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=win.golgoli1.co.uk&port=2053&secret=ee1603010200010001fc030386e24c3add7777772e7961686f6f2e636f6d) |
| 10 | `mizanesgh.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mizanesgh.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 11 | `groupe.avacloud.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=groupe.avacloud.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 12 | `cinema-hulk.avangement.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cinema-hulk.avangement.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 13 | `app.rknwatch.digital` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=app.rknwatch.digital&port=443&secret=ee7fb8b71569b0536bb15039e506afb65a6170702e726b6e77617463682e6469676974616c) |
| 15 | `87.248.129.47` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.47&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 17 | `eerie.proxytales.life` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=eerie.proxytales.life&port=443&secret=ee6a0333c1db3f8eaba5c76731a44203b6617669746f2e7275) |
| 19 | `sv.hajhossein.observer` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sv.hajhossein.observer&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |


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
