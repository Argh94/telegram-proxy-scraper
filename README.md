# 📊 نتایج استخراج: (آخرین بروزرسانی: 00:50 05-05-1404)

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
| 1 | `5.255.126.122` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.255.126.122&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 2 | `95.181.173.143` | `9` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.181.173.143&port=9&secret=dd9a158f74da4d63d2cdfb4e09dbafffee`) |
| 3 | `91.99.20.56` | `155` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.99.20.56&port=155&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ) |
| 4 | `194.164.34.200` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.164.34.200&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D)|[پروکسی](https://t.me/proxy?server=89.110.76.65) |
| 5 | `117.55.203.133` | `56068` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=117.55.203.133&port=56068&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d) |
| 6 | `11899.meli.meli.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=11899.meli.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 7 | `188.245.196.206` | `888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=188.245.196.206&port=888&secret=1320PuNyHw_LQKT_Y7XNJw) |
| 8 | `88.99.61.188` | `2908` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=88.99.61.188&port=2908&secret=DDBighLLvXrFGRMCBVJdFQRueWVrdGFuZXQuY29t) |
| 9 | `193.3.190.48` | `85` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=193.3.190.48&port=85&secret=7gAA8A8Pd1VV____9QBuLmljaGF0Z3B0LmNvbQ==) |
| 10 | `Mortal-Vovok.nuremborg-hamborg.dodos-codam.mehrvilla.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Mortal-Vovok.nuremborg-hamborg.dodos-codam.mehrvilla.info&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 11 | `62.60.178.104` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.60.178.104&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)`) |
| 12 | `185.222.28.15` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.222.28.15&port=8443&secret=1320PuNyHw_LQKT_Y7XNJw==) |
| 13 | `150.241.78.70` | `70` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=150.241.78.70&port=70&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0=) |
| 14 | `91.99.164.169` | `4637` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.99.164.169&port=4637&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t)__) |
| 15 | `87.248.132.17` | `343` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.132.17&port=343&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D)`) |
| 16 | `91.99.85.639l.ir` | `110` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.99.85.639l.ir&port=110&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0=](https://t.me/netv2reyng) |
| 17 | `12.meli.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=12.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 18 | `fitidream.fiziotr.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fitidream.fiziotr.info&port=443&secret=FgMBAgABAAH8AwOG4kw63Q==) |
| 19 | `88800.meli.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=88800.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 20 | `93.88.205.15` | `888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=93.88.205.15&port=888&secret=eeNEgYdJvXrFGRMCIMJdCQ) |


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
