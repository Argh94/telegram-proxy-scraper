# 📊 نتایج استخراج: (آخرین بروزرسانی: 02:11 04-05-1404)

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
| 1 | `62.60.179.207` | `9880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.60.179.207&port=9880&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 2 | `87.229.100.227` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.229.100.227&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 3 | `62.60.176.235` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.60.176.235&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)|) |
| 4 | `100.meli.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=100.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 5 | `www.sshputty.icu.` | `888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.sshputty.icu.&port=888&secret=ee0c30628212cbbd7ac519130205525d1569612e737465616d706f77657265642e636f6d) |
| 6 | `194.164.34.200` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.164.34.200&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 7 | `195.200.28.225` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.200.28.225&port=443&secret=eeNEgYdJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 8 | `95.216.22.207` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.216.22.207&port=443&secret=iORid5lJ237IiBMGYMQMdw==) |
| 9 | `link.irpower-e.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=link.irpower-e.ir&port=443&secret=ee07df7df7df7dfffffdfffffffffffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d) |
| 10 | `151.244.42.18` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=151.244.42.18&port=443&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 11 | `mofidonline.emofid.bourse24.moflidonline.mofiidonline.ir` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mofidonline.emofid.bourse24.moflidonline.mofiidonline.ir&port=2053&secret=3QAA8A8Pd1VV____9QBuLmk) |
| 12 | `Komatso-Japan.www.google.com.ganool-com.info` | `300` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Komatso-Japan.www.google.com.ganool-com.info&port=300&secret=eeRigzNJvXrFGRMCIMJdEARueWVrdGFuZXQuY29tZmFyYTrhdi5jb212YZ6ubmFqXeEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 13 | `www.udpoutgoinn.xyz.` | `888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.udpoutgoinn.xyz.&port=888&secret=ee0c30628212cbbd7ac519130205525d1569612e737465616d706f77657265642e636f6d****) |
| 14 | `darknamikonina.beramaqhyou.cyou` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=darknamikonina.beramaqhyou.cyou&port=443&secret=eee6607B90889CC60719D2170CB2851962737465616D706F77657265642E636F6D)__) |
| 15 | `176.65.136.62` | `70` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=176.65.136.62&port=70&secret=3dd9tD7jch8Py0Ck_2O1zSc=) |
| 16 | `87.248.132.23` | `70` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.132.23&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 17 | `daem.fsaremi.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=daem.fsaremi.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 18 | `87.229.100.239` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.229.100.239&port=443&secret=eeRighJJvXrFGRMCIMJdCQ) |
| 19 | `95.216.201.145` | `9091` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.216.201.145&port=9091&secret=7ggggggg-r-r-r__AAAAAAAtLmNvbS0=)__) |
| 20 | `00600.meli.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=00600.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t**) |


> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید.

## 🤝 مشارکت
از ایده‌ها و مشارکت شما استقبال می‌کنیم! برای بهبود پروژه:
1. یک **Issue** در مخزن باز کنید.
2. یا یک **Pull Request** با تغییرات پیشنهادی ارسال کنید.

## 📜 لایسنس
این پروژه تحت [لایسنس MIT](LICENSE) منتشر شده است.

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
