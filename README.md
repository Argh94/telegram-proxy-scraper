# 📊 نتایج استخراج: (آخرین بروزرسانی: 23:32 18-03-1405)

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License" />
  <img src="https://img.shields.io/badge/python-3.9-blue" alt="Python 3.11" />
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
| 2 | `conn-now.tpro-ru.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=conn-now.tpro-ru.info&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 3 | `87.248.129.103` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.103&port=8443&secret=ee1603010200010001fc030386e24c3add646565707365656B2E636F6D) |
| 5 | `132.243.213.221` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.213.221&port=443&secret=ee4d3cf6b01fed616495b9651ebe37313f766b2e7275) |
| 7 | `87.248.129.247` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.247&port=4455&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 9 | `zoom.flowaccess.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zoom.flowaccess.site&port=443&secret=ee50179d3cf3b7e3600efe3b6001fa35c07a6f6f6d2e666c6f776163636573732e73697465) |
| 11 | `87.248.129.104` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.104&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 12 | `167.233.60.38` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.233.60.38&port=443&secret=ddd77db43ee3721f0fcb40a4ff63b5cd27) |
| 14 | `176.65.138.97` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=176.65.138.97&port=8443&secret=ee1603010200010001fc030386e24c3add646565707365656B2E636F6D) |
| 15 | `65.109.250.30` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.250.30&port=443&secret=dd79ee65acf6c575bd6f8b3c1ddc7107a3) |
| 16 | `yard-yaystal-menyat.yard-tg-bot.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=yard-yaystal-menyat.yard-tg-bot.online&port=443&secret=ee6a441d3845f1bfec1100662ce671d8ed76762e636f6d) |
| 17 | `norm.quickdl.info` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=norm.quickdl.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 18 | `nova.flowstreamhub.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nova.flowstreamhub.site&port=443&secret=eeb1a90b2bd080b288badd320bf824277c6e6f76612e666c6f7773747265616d6875622e73697465) |
| 19 | `fool.feel-fly.info` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fool.feel-fly.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 20 | `167.233.54.153` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.233.54.153&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |


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
