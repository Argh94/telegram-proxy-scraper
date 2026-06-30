# 📊 نتایج استخراج: (آخرین بروزرسانی: 17:25 09-04-1405)

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
| 1 | `aghaye.aseman.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=aghaye.aseman.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 2 | `edge.rknwatch.digital` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=edge.rknwatch.digital&port=443&secret=ee1f46fcc7e9b3991677f71d2c1cb2ac92656467652e726b6e77617463682e6469676974616c) |
| 3 | `Www.merco-karco.website` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Www.merco-karco.website&port=443&secret=ee1603010200010001fc030386e24c3add626973636F7474692E79656B74616E65742E636F6D) |
| 4 | `cdn.kvakzon.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cdn.kvakzon.top&port=443&secret=ee4c9e204ef11de2b7b95e7ea9d11d284063646e2e6b76616b7a6f6e2e746f70) |
| 5 | `signin-signout-manager.davazdah.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=signin-signout-manager.davazdah.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 6 | `b8rta.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=b8rta.co.uk.&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 7 | `95.85.230.56` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.85.230.56&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 8 | `ikco.denatara.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ikco.denatara.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 9 | `cdn.yektanet.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cdn.yektanet.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 10 | `3.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3.telbet.lol&port=25565&secret=dd79e7010200010007f0030386e24c3add) |
| 11 | `87.229.56.5` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.229.56.5&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 12 | `hetzner.bkontek.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hetzner.bkontek.co.uk.&port=443&secret=eeddffffffc5a1168b2ff3eba31cbfffff6865747a6e65722e636f6d) |
| 13 | `signin-signout-manager.davazdah.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=signin-signout-manager.davazdah.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 15 | `get.utkanos.life` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=get.utkanos.life&port=443&secret=eef09a7a4c51b6bc6caf4d3134b312b0f56765742e75746b616e6f732e6c696665) |
| 16 | `tabibie.del.davazdah.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tabibie.del.davazdah.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 19 | `87.248.129.174` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.174&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 20 | `194.77.70.83` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.77.70.83&port=8080&secret=1603010200010001fc030386e24c3add) |


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
