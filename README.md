# 📊 نتایج استخراج: (آخرین بروزرسانی: 13:33 13-01-1405)

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
| 1 | `proxy.qwencloud.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.qwencloud.ru&port=443&secret=ee2fd003fc6d1b55727d17db09c8b174107765622e6d61782e7275) |
| 2 | `rkn.tg` | `1337` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rkn.tg&port=1337&secret=dda2d3fa639a6ddcf8d6d1c5913d001531) |
| 3 | `65.109.215.115` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.215.115&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `alo.acharbashi.info` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=alo.acharbashi.info&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |
| 5 | `tg.safepal.life` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.safepal.life&port=443&secret=094d1e6d9047716b1672fc5560683bfd) |
| 6 | `own.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=own.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 7 | `i.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=i.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 8 | `193.58.122.56` | `11443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=193.58.122.56&port=11443&secret=02e4244221ce5b63ab3ba63af30cdf51) |
| 9 | `95.216.178.41` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.216.178.41&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `proxyobhod.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxyobhod.online&port=443&secret=01b307acba4f54f55aafc33bb06bbbf6) |
| 11 | `146.185.241.89` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=146.185.241.89&port=443&secret=c351841a608cca24813a321aa080bc91) |
| 12 | `proxyonline.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxyonline.online&port=443&secret=7b52009b64fd0a2a49e6d8a939753077) |
| 13 | `49.13.35.164` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=49.13.35.164&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 14 | `142.54.189.107` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=142.54.189.107&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 15 | `45.90.13.34` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.90.13.34&port=443&secret=dda85f2776cc83dbff66b440fb03050cf7) |
| 18 | `44.223.90.89` | `80` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=44.223.90.89&port=80&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `188.137.232.184` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=188.137.232.184&port=443&secret=ee6293ee0eaa15186ea42d9b571b9275b17777772e636c6f7564666c6172652e636f6d) |


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
