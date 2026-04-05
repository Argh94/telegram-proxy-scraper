# 📊 نتایج استخراج: (آخرین بروزرسانی: 08:43 16-01-1405)

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
| 1 | `2.27.23.23` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.27.23.23&port=8443&secret=f5a97ceadd1bbedd918fbd9f1c9387dd) |
| 2 | `2.27.23.23` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.27.23.23&port=8443&secret=f5a97ceadd1bbedd918fbd9f1c9387dd) |
| 3 | `85.9.193.178` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=85.9.193.178&port=443&secret=ee7777772e676f6f676c652e636f6d9d) |
| 4 | `91.107.182.200` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.182.200&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `hyper.happvpn.cc` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hyper.happvpn.cc&port=8443&secret=ee4852c1c04ab83db8a328c60eaf9a0db268797065722e6861707076706e2e6363) |
| 8 | `soft.telegramharvester.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=soft.telegramharvester.ru&port=443&secret=ee05ca1fb5eadbac1e7e8c725695b48f0079612e7275) |
| 9 | `burned.concordantly.onlay.unicolourous.wholesale.superpinoy.net` | `2500` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=burned.concordantly.onlay.unicolourous.wholesale.superpinoy.net&port=2500&secret=fd35d27eb736c8d1527e44aa67d57649) |
| 10 | `65.109.16.139` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.16.139&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `o6xodum.duckdns.org` | `1488` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=o6xodum.duckdns.org&port=1488&secret=ee494c3d5858be223fcbb9970d8bf05a036d6f746f76736b696b682e7275) |
| 12 | `77.90.63.2` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=77.90.63.2&port=443&secret=ee8dd986e1d1ea297bdb58db4b5e369af57777772e676f6f676c652e636f6d) |
| 14 | `mtproto.proproxies.pro` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtproto.proproxies.pro&port=8443&secret=ee8e60f2fe61cf363f9ed0d0695b59c6d86d7470726f746f2e70726f70726f786965732e70726f) |
| 15 | `how.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=how.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 16 | `alo.acharbashi.info` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=alo.acharbashi.info&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |
| 17 | `190.2.142.250` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=190.2.142.250&port=8443&secret=24eb9ed0e56d5ea9832d45459feb2058) |
| 18 | `de.nerdpol.ovh` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=de.nerdpol.ovh&port=4515&secret=ee3177bef597bf8246bae855cee6fe0aa564652e6e657264706f6c2e6f7668) |
| 19 | `proxyobhod.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxyobhod.online&port=443&secret=71c30cc28759e0a10b6de5b471d69751) |
| 20 | `proxy.ciaowner.lol` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.ciaowner.lol&port=443&secret=ee1459dda62dc99782f8741f1ab0deb4f2706574726f766963682e7275) |


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
