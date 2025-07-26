# 📊 نتایج استخراج: (آخرین بروزرسانی: 18:51 04-05-1404)

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
| 1 | `45.129.199.72` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.129.199.72&port=443&secret=ee100404ff0f48064fffffff9001b8696d696d656469612e737465616d706f77657265642e636f6d) |
| 2 | `1.dfff.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.the_internet.zban-df.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=1.dfff.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.the_internet.zban-df.info&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q) |
| 3 | `87.248.132.38` | `85` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.132.38&port=85&secret=ee0000f00f0f775555fffffff5006e2e69646F776E6C6F61642E77696E646F77737570646174652E636F6D) |
| 4 | `204.76.203.84` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=204.76.203.84&port=443&secret=15115115115115115115115115115115) |
| 5 | `91.84.107.88` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.84.107.88&port=443&secret=ee07df7df7df7dfffffdfffffffffffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d) |
| 6 | `bib.bib.game.zx2hgujoiah-xy1xutr021-2tk.com` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bib.bib.game.zx2hgujoiah-xy1xutr021-2tk.com&port=8443&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0=)__) |
| 7 | `88.210.35.238` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=88.210.35.238&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 8 | `146.103.97.147` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=146.103.97.147&port=443&secret=eeNEgYdJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 9 | `500.meli.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=500.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 10 | `62.60.176.183` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.60.176.183&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 11 | `157.180.123.236` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=157.180.123.236&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q) |
| 12 | `www.uptv.digital.` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.uptv.digital.&port=8888&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 13 | `151.244.42.20` | `70` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=151.244.42.20&port=70&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 14 | `AMD-epic.sheshko.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=AMD-epic.sheshko.info&port=443&secret=7hYDAQIAAQAB_AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 15 | `BodoBodo.khoshghovar.online.` | `888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=BodoBodo.khoshghovar.online.&port=888&secret=7gwwYoISy716xRkTAgVSXRVpYS5zdGVhbXBvd2VyZWQuY29t****) |
| 16 | `87.248.132.65` | `155` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.132.65&port=155&secret=ee0000f00f0f775555fffffff5006e2e69646f776e6c6f61642e77696e646f77737570646174652e636f6d) |
| 17 | `01111.meli.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=01111.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t)__) |
| 18 | `151.244.42.5` | `85` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=151.244.42.5&port=85&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 19 | `109.107.167.113` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=109.107.167.113&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWR1aS5jb20) |
| 20 | `45.135.192.253` | `85` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.135.192.253&port=85&secret=ee0000f00f0f775555fffffff5006e2e69646F776E6C6F61642E77696E646F77737570646174652E636F6D) |


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
