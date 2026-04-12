# 📊 نتایج استخراج: (آخرین بروزرسانی: 13:15 23-01-1405)

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
| 1 | `137.220.48.103` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=137.220.48.103&port=443&secret=f09009648a7027384281126b6ce46f15) |
| 2 | `31.59.103.64` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=31.59.103.64&port=443&secret=eee2970b9a0d34e958110ee25e8bc8378d6d61696c2e7275) |
| 3 | `62.171.183.101` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.171.183.101&port=443&secret=ee36ee4a84e1fa2cca6f1d430eee851de7636c6f7564666c6172652e636f6d) |
| 4 | `62.171.164.255` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.171.164.255&port=443&secret=eed00f99d3053051a66446182549bb84c8636c6f7564666c6172652e636f6d) |
| 5 | `195.254.165.247` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.247&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 6 | `tg.proxywing.net` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.proxywing.net&port=443&secret=dd398e9112420ca2ad72bac8bfd851ff42) |
| 7 | `exact.begoodtunnel.su` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=exact.begoodtunnel.su&port=443&secret=eed802c58b0133cc8db3c6880bab5308c165786163742e6265676f6f6474756e6e656c2e7375) |
| 8 | `free-proxy-03.duckdns.org` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=free-proxy-03.duckdns.org&port=443&secret=ddea63ef94c511c297c68017f7d71ce1db) |
| 9 | `195.254.165.253` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.253&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 10 | `195.254.165.243` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.243&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 11 | `mt.white-bars.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.white-bars.ru&port=8443&secret=12da224b61c3662bcda2294414b5eda9) |
| 12 | `nid1.mtproxyserver.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nid1.mtproxyserver.site&port=443&secret=ee4981407056399dc3f8c168e96d42fb9962726f777365722e79616e6465782e636f6d) |
| 13 | `3.hajrozbeh.onl` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3.hajrozbeh.onl&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 14 | `178.18.248.188` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.18.248.188&port=443&secret=ee4bb5230f72689fed962d818fac46923f636c6f7564666c6172652e636f6d) |
| 15 | `proxy.ciaowner.lol` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.ciaowner.lol&port=443&secret=ee1459dda62dc99782f8741f1ab0deb4f2706574726f766963682e7275) |
| 16 | `185.117.0.248` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.117.0.248&port=443&secret=eed451f808fd60ed2c45f11d38fdbc87c57961686f6f2e636f6d) |
| 17 | `116.203.134.165` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=116.203.134.165&port=443&secret=ee636c6f7564666c6172652e636f6db6) |
| 18 | `havene5c9-c9862954.proxytg.ink` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=havene5c9-c9862954.proxytg.ink&port=443&secret=b968de5d8c88024af77ee0ed494abb74) |
| 19 | `158.160.245.131` | `17372` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=158.160.245.131&port=17372&secret=314ce48f4f975874163a7961444c3b66) |


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
