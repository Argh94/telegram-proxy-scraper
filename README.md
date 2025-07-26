# 📊 نتایج استخراج: (آخرین بروزرسانی: 21:58 04-05-1404)

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License" />
  <img src="https://img.shields.io/badge/python-3.9-blue" alt="Python 3.9" />
  <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions Welcome" />
  <img src="https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg" alt="Proxy Scraper Workflow" />
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
  - [MhdiTaheri/ProxyCollector](https://raw.githubusercontent.com/MhdiTaheri/ProxyCollector/main/proxy.txt)
  - [SoliSpirit/mtproto](https://raw.githubusercontent.com/SoliSpirit/mtproto/master/all_proxies.txt)
- **کانال‌های تلگرام**:
  - iporoto, HiProxy, iproxy, iRoProxy, proxyforopeta, IRN_Proxy, MProxy_ir, ProxyHagh, PyroProxy, ProxyMTProto, MTPro_XYZ, vpns, mtmvpn, asr_proxy, proxyskyy

## 📈 نمونه پروکسی‌ها
جدول زیر نمونه‌ای از 20 پروکسی فعال از فایل `proxy.txt` را نمایش می‌دهد. برای استفاده، روی لینک پروکسی کلیک کنید یا آن را کپی کنید:

| # | سرور (Server) | پورت (Port) | وضعیت | لینک پروکسی |
|---|---------------|-------------|-------|-------------|
| 1 | `6.dfff.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.the_internet.zban-df.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=6.dfff.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.the_internet.zban-df.info&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q) |
| 2 | `185.222.28.152` | `23` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.222.28.152&port=23&secret=1320PuNyHw_LQKT_Y7XNJw==) |
| 3 | `87.248.134.172` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.134.172&port=443&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D) |
| 4 | `79.172.228.161` | `333` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.172.228.161&port=333&secret=ee79e462821249bd7ac519130220c25d096D656469612E737465616D706F77657265642E636F6D) |
| 5 | `91.99.233.5` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.99.233.5&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 6 | `157.180.126.9` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=157.180.126.9&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q) |
| 7 | `5.75.199.133` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.75.199.133&port=443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 8 | `95.169.173.8` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.169.173.8&port=8443&secret=1320PuNyHw_LQKT_Y7XNJw) |
| 9 | `62.60.177.166` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.60.177.166&port=8443&secret=FgMBAgABAAfwAwOG4kw63Q) |
| 10 | `87.248.132.96` | `200` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.132.96&port=200&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 11 | `51.159.149.220` | `8000` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=51.159.149.220&port=8000&secret=eee72cf91a4fee7902896720b31c3c14e27777772e736974652e636f6d) |
| 12 | `142.132.174.75` | `551` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=142.132.174.75&port=551&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 13 | `77.238.239.178` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=77.238.239.178&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D)|[ایرانسل](https://t.me/proxy?server=212.34.139.251) |
| 14 | `62.60.177.35` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.60.177.35&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ) |
| 15 | `157.180.123.236` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=157.180.123.236&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q) |
| 16 | `91.99.172.152` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.99.172.152&port=8888&secret=7gAA8A8Pd1VV) |
| 17 | `87.248.132.10` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.132.10&port=443&secret=eeRighJJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 18 | `23.88.70.165` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=23.88.70.165&port=443&secret=EERighJJvXrFGRMCIMJdCQ==) |
| 19 | `146.103.105.74` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=146.103.105.74&port=443&secret=7gAA8A8Pd1VV____9QBuLmktLS1-wrHinJMtLS0) |
| 20 | `51.38.223.137` | `110` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=51.38.223.137&port=110&secret=ee050e992bf52dd097871abc372c25dede7777772e636c6f7564666c6172652e636f6d)|) |


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
