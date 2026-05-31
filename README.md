# 📊 نتایج استخراج: (آخرین بروزرسانی: 06:00 10-03-1405)

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
| 2 | `62.238.37.167` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.238.37.167&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `s13.neo-trading.org` | `993` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s13.neo-trading.org&port=993&secret=eec3fefd89a25d37ca3af1a602c7bfd8de7777772e636c6f7564666c6172652e636f6d) |
| 4 | `87.248.129.220` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.220&port=2053&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 6 | `135.181.35.14` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=135.181.35.14&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `rah.time-meli.info` | `155` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rah.time-meli.info&port=155&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `85.192.29.173` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=85.192.29.173&port=443&secret=ee764656762499295cd6aef0714a2a4bdf766b2e636f6d) |
| 10 | `35.178.212.203` | `80` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=35.178.212.203&port=80&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `miinecrafto.com` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=miinecrafto.com&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 12 | `r21.proxytg.space` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=r21.proxytg.space&port=8443&secret=eec5963870566a7e0d9a04f5f792d9faf47232312e70726f787974672e7370616365) |
| 15 | `87.248.129.225` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.225&port=443&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d) |
| 16 | `r28.proxytg.space` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=r28.proxytg.space&port=8443&secret=eed5f4455563d14c2b8c8a38868c7d91607232382e70726f787974672e7370616365) |
| 17 | `evening.nolags.pw` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=evening.nolags.pw&port=443&secret=dd29b3afb209c4427676b4c43eecb7f556) |
| 18 | `sexy.arixo.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sexy.arixo.shop&port=443&secret=eec11798ab008831b474066c9e1ebf5c59617669746f2e7275) |
| 19 | `89.167.100.114` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.167.100.114&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `89.167.101.96` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.167.101.96&port=8443&secret=dd104462821249bd7ac519130220c25d09) |


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
