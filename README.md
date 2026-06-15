# 📊 نتایج استخراج: (آخرین بروزرسانی: 18:26 25-03-1405)

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
| 1 | `drift.proxyonline.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=drift.proxyonline.online&port=443&secret=eeacd41b6bbfa3b3f3d50a25511430857464726966742e70726f78796f6e6c696e652e6f6e6c696e65) |
| 2 | `vpn.prxtoday.store` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vpn.prxtoday.store&port=443&secret=ee29260362b2497c092e631593a534e5a376706e2e707278746f6461792e73746f7265) |
| 4 | `Ehsgh.kon.khoshgele.ir.biobarmesh.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Ehsgh.kon.khoshgele.ir.biobarmesh.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 5 | `mx.proxyz.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mx.proxyz.site&port=443&secret=ee76166fbf55209edbcfbe009bcc16f4646d782e70726f78797a2e73697465) |
| 6 | `hub.nowabst.net` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hub.nowabst.net&port=853&secret=ee55aabc9752a9d9d379e02943cf8117956164732e78352e7275) |
| 7 | `87.248.129.16` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.16&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 8 | `87.248.129.196` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.196&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 9 | `65.21.113.80` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.21.113.80&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `go.proxyz.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=go.proxyz.site&port=443&secret=ee36854d344477eab338dda799b071116b676f2e70726f78797a2e73697465) |
| 11 | `87.248.129.194` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.194&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 12 | `mizban.genuismind.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mizban.genuismind.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 13 | `get.proxyz.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=get.proxyz.site&port=443&secret=ee8bfeb37ebe59a0f6aed1ccae9b9981566765742e70726f78797a2e73697465) |
| 14 | `jet.proxym.world` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jet.proxym.world&port=443&secret=ee894a8e1c70d3ec137af76968609e04666a65742e70726f78796d2e776f726c64) |
| 15 | `Together-for-iran.jetish.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Together-for-iran.jetish.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 16 | `87.248.129.136` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.136&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 17 | `31.41.33.114` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=31.41.33.114&port=443&secret=eee854b22396ba5a74f23b6f126108294a6972616e2e6d69642e7275) |
| 18 | `cloud.prx.today` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cloud.prx.today&port=443&secret=eeda2d39fb15ca8ddb6582b915b149465c636c6f75642e7072782e746f646179) |
| 19 | `bolt.proxyonline.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bolt.proxyonline.online&port=443&secret=ee98741a4df96ee86a25ca542a538a3484626f6c742e70726f78796f6e6c696e652e6f6e6c696e65) |
| 20 | `mean.mahanam.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mean.mahanam.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |


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
