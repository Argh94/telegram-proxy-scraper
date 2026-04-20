# 📊 نتایج استخراج: (آخرین بروزرسانی: 14:19 31-01-1405)

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
| 1 | `tg.plusonevpn.com` | `1984` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.plusonevpn.com&port=1984&secret=dd4c7671c23268cbcb7330ff7ee9ab0622) |
| 2 | `2A.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2A.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 3 | `oneproxys.best` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=oneproxys.best&port=443&secret=eed68360458af63073bac1394e8c7a48da6f6e6570726f7879732e62657374) |
| 4 | `65.21.184.226` | `54921` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.21.184.226&port=54921&secret=ee104462821249bd7ac519130220c25d096d61782e7275) |
| 5 | `87.106.137.212` | `21212` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.106.137.212&port=21212&secret=312b91cf4831abf49809466752b9c364) |
| 6 | `clickproxy.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=clickproxy.online&port=443&secret=ee79612e7275e8e3100d7adf36efa572) |
| 7 | `how.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=how.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 8 | `142.54.189.108` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=142.54.189.108&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 9 | `bezobhoda.freeon.name` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bezobhoda.freeon.name&port=8443&secret=eeed1a5a7f339b8ff9840d52df123829706164732e78352e7275) |
| 10 | `107.150.34.99` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=107.150.34.99&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 11 | `i.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=i.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 12 | `64.188.64.195` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=64.188.64.195&port=443&secret=f24524a119212e8d79635194dd77642d) |
| 13 | `49.13.35.164` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=49.13.35.164&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 14 | `pugoholic.ydns.eu` | `9443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pugoholic.ydns.eu&port=9443&secret=6a08a96f53b99a7e517a2c5cb46468be) |
| 15 | `95.217.28.246` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.217.28.246&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `64.188.64.195` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=64.188.64.195&port=443&secret=f24524a119212e8d79635194dd77642d) |
| 18 | `144.91.120.39` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=144.91.120.39&port=443&secret=ee24f320786f2121a2e797016f01a5e614636c6f7564666c6172652e636f6d) |
| 19 | `proxyrknsosatb.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxyrknsosatb.site&port=443&secret=eed68360458af63073bac1394e8c7a48da70726f7879726b6e736f736174622e73697465) |
| 20 | `poll1704.mtproxygram.lol` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=poll1704.mtproxygram.lol&port=443&secret=eec39eef5b0ab34eb882b893c156b4c14a62726f777365722e79616e6465782e636f6d) |


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
