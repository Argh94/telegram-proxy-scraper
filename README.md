# 📊 نتایج استخراج: (آخرین بروزرسانی: 16:32 23-01-1405)

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
| 1 | `194.163.143.211` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.163.143.211&port=443&secret=ee49c11be00962c867f93716b5825a387f636c6f7564666c6172652e636f6d) |
| 2 | `27289292.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=27289292.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 3 | `195.254.165.250` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.250&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 4 | `194.163.128.208` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.163.128.208&port=443&secret=eeb5f3d79235638f620aa45da0bd1a07de636c6f7564666c6172652e636f6d) |
| 5 | `exact.begoodtunnel.su` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=exact.begoodtunnel.su&port=443&secret=eed802c58b0133cc8db3c6880bab5308c165786163742e6265676f6f6474756e6e656c2e7375) |
| 6 | `87.121.89.227` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.121.89.227&port=8443&secret=eeba15e0c527433a3a686b97f09254f5a0796f6e73652e6f7267) |
| 7 | `195.254.165.250` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.250&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 8 | `103.56.114.117` | `20001` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=103.56.114.117&port=20001&secret=eea5942ff95e1bc79f3598114dfc767d19617a7572652e6d6963726f736f66742e636f6d) |
| 11 | `mtprotofr.mtproxyserver.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtprotofr.mtproxyserver.site&port=443&secret=ee4f16151d4d748e02ab3a97325f54554d62726f777365722e79616e6465782e636f6d) |
| 12 | `95.217.28.150` | `45321` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.217.28.150&port=45321&secret=ee104462821249bd7ac519130220c25d096d61782e7275) |
| 13 | `195.254.165.243` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.243&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 14 | `tg.proxywing.net` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.proxywing.net&port=443&secret=dd398e9112420ca2ad72bac8bfd851ff42) |
| 15 | `free-proxy-03.duckdns.org` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=free-proxy-03.duckdns.org&port=443&secret=ddea63ef94c511c297c68017f7d71ce1db) |
| 17 | `31.130.151.16` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=31.130.151.16&port=443&secret=4931e9e6000537266a0de4dbb81f81fa) |
| 18 | `panel.meowmeowcat.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=panel.meowmeowcat.top&port=443&secret=ee1fa90a9cd9bd2e85299f3960238d39757777772e77696b6970656469612e6f7267) |
| 19 | `46.225.29.180` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.225.29.180&port=443&secret=ee636c6f7564666c6172652e636f6db6) |
| 20 | `217.60.36.37` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=217.60.36.37&port=443&secret=eee2970b9a0d34e958110ee25e8bc8378d6d61696c2e7275) |


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
