# 📊 نتایج استخراج: (آخرین بروزرسانی: 16:10 04-05-1404)

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
| 1 | `response.cinere.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=response.cinere.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f7765726) |
| 2 | `79.172.228.10` | `700` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.172.228.10&port=700&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 3 | `212.34.141.71` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=212.34.141.71&port=443&secret=1320PuNyHw_LQKT_Y7XNJw) |
| 4 | `109.104.154.226` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=109.104.154.226&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t**) |
| 5 | `1.df.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.the_internet.brobalair.store` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=1.df.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.the_internet.brobalair.store&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q) |
| 6 | `irancell-hamrah.soren-mashin.ir.` | `9741` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=irancell-hamrah.soren-mashin.ir.&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d)__) |
| 7 | `193.3.190.47` | `85` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=193.3.190.47&port=85&secret=ee0000f00f0f775555fffffff5006e2e69636861746770742e636f6d) |
| 8 | `176.65.128.50` | `155` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=176.65.128.50&port=155&secret=ee07df7df7df7dffdffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d) |
| 9 | `7884.Ir.ir.ir.ir.ir.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=7884.Ir.ir.ir.ir.ir.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t__) |
| 10 | `193.3.190.51` | `85` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=193.3.190.51&port=85&secret=ee0000f00f0f775555fffffff5006e2e69636861746770742e636f6d) |
| 11 | `62.60.176.139` | `9741` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.60.176.139&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 12 | `91.99.172.214` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.99.172.214&port=8888&secret=7gAA8A8Pd1VV) |
| 13 | `12.meli.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=12.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 14 | `159.69.33.168` | `551` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=159.69.33.168&port=551&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 15 | `89.251.10.36` | `6443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.251.10.36&port=6443&secret=ee151151151151151151151151151151156d656469612e737465616d706f77657265642e636f6d) |
| 16 | `79.172.228.96` | `700` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.172.228.96&port=700&secret=7gAA8A8Pd1VV9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t__) |
| 17 | `barname-darsi.aivalai.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=barname-darsi.aivalai.info&port=443&secret=1603010200010001fc030386e24c3add) |
| 18 | `212.34.130.72` | `3598` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=212.34.130.72&port=3598&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 19 | `213.145.71.35` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=213.145.71.35&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 20 | `91.99.187.112` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.99.187.112&port=443&secret=ee151151151151151151151151151151156D656469612E737465616D706F77657265642E636F6D) |


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
