# 📊 نتایج استخراج: (آخرین بروزرسانی: 12:19 25-03-1405)

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
| 1 | `data.proxyvpn.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=data.proxyvpn.site&port=443&secret=ee7d75b7a3d02eefad99691681a534c1fe646174612e70726f787976706e2e73697465) |
| 2 | `best-sellerst.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=best-sellerst.co.uk.&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 3 | `cloud.prx.today` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cloud.prx.today&port=443&secret=eeda2d39fb15ca8ddb6582b915b149465c636c6f75642e7072782e746f646179) |
| 4 | `edge.prxtoday.store` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=edge.prxtoday.store&port=443&secret=ee9ca7db6793ada8892580787426c44fa2656467652e707278746f6461792e73746f7265) |
| 5 | `drift.proxyonline.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=drift.proxyonline.online&port=443&secret=eeacd41b6bbfa3b3f3d50a25511430857464726966742e70726f78796f6e6c696e652e6f6e6c696e65) |
| 6 | `87.248.129.103` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.103&port=8443&secret=ee1603010200010001fc030386e24c3add646565707365656B2E636F6D) |
| 7 | `server.mizbanonline.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=server.mizbanonline.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 9 | `194.213.118.26` | `1010` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.213.118.26&port=1010&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 13 | `secure.proxyz.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=secure.proxyz.site&port=443&secret=ee6971f00b20112546804a9453a1a13fde7365637572652e70726f78797a2e73697465) |
| 14 | `data.proxyvpn.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=data.proxyvpn.site&port=443&secret=ee7d75b7a3d02eefad99691681a534c1fe646174612e70726f787976706e2e73697465) |
| 15 | `87.248.129.133` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.133&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 17 | `dl.prx.today` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dl.prx.today&port=443&secret=ee9b9483de201ca0a074d391d3c4b63152646c2e7072782e746f646179) |
| 18 | `87.248.129.105` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.105&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 19 | `gw.nowabst.net` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gw.nowabst.net&port=853&secret=ee6104d5fd936c4930978f0227166deaa96164732e78352e7275) |
| 20 | `relay.nowabst.net` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=relay.nowabst.net&port=853&secret=ee19f4ad26c65891fd22cf3b7a59f0d1036164732e78352e7275) |


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
