# 📊 نتایج استخراج: (آخرین بروزرسانی: 21:28 07-03-1405)

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
| 6 | `80.96.112.222` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=80.96.112.222&port=443&secret=ee2e7fcf4666472ebd58e4fea75357105f7777772e79616e6465782e7275) |
| 7 | `cloud.mtproxy.pw` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cloud.mtproxy.pw&port=443&secret=ee3f8a91c2d7e04b6a9f12c5e8370bd4aa786170692e6f7a6f6e2e7275) |
| 9 | `172.65.38.26` | `9443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.65.38.26&port=9443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 10 | `connect.tproxy.store` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=connect.tproxy.store&port=8443&secret=dd79e7010200010007f0030386e24c3add) |
| 11 | `s4.neo-trading.org` | `993` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s4.neo-trading.org&port=993&secret=ee181e2ad5e63c27262781187f2dedc4bb7777772e636c6f7564666c6172652e636f6d) |
| 12 | `172.65.38.26` | `9443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.65.38.26&port=9443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 13 | `87.248.129.210` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.210&port=4455&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 14 | `r22.proxytg.space` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=r22.proxytg.space&port=8443&secret=eeace5ab7ab128f81a0b16ada143ec10807232322e70726f787974672e7370616365) |
| 17 | `r15.proxytg.space` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=r15.proxytg.space&port=8443&secret=ee031cb73865e145aac3f4aee0fd1a714d7231352e70726f787974672e7370616365) |
| 18 | `r16.proxytg.space` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=r16.proxytg.space&port=8443&secret=ee58ff3d2285478b5a749af32da19f36707231362e70726f787974672e7370616365) |
| 19 | `178.105.188.16` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.105.188.16&port=7443&secret=ee1603010200010001fc030386e24c3add646e2e79656b74616e65742e636f6d646c2e676f6f676c652e636f6d666172616B61762E636F6D160301020001000100000000000000000000000000000000) |


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
