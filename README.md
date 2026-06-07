# 📊 نتایج استخراج: (آخرین بروزرسانی: 22:37 17-03-1405)

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
| 1 | `37.27.192.211` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=37.27.192.211&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `s02.neo-trading.org` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s02.neo-trading.org&port=443&secret=ee6ec9f7e082baf2397b450727ce78447e6f7a6f6e2e7275) |
| 3 | `51.250.71.16` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=51.250.71.16&port=443&secret=ee83664d92de321661cc33e6839bbeef1e617669746f2e7275) |
| 5 | `148.251.55.126` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=148.251.55.126&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `157.180.122.162` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=157.180.122.162&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 10 | `zoom.flowaccess.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zoom.flowaccess.site&port=443&secret=ee50179d3cf3b7e3600efe3b6001fa35c07a6f6f6d2e666c6f776163636573732e73697465) |
| 11 | `167.233.49.234` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.233.49.234&port=443&secret=ddd77db43ee3721f0fcb40a4ff63b5cd27) |
| 12 | `dash.flowstreamhub.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dash.flowstreamhub.site&port=443&secret=eee5860e3a92504e57496b5748749921d3646173682e666c6f7773747265616d6875622e73697465) |
| 15 | `213.133.102.101` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=213.133.102.101&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `159.69.100.158` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=159.69.100.158&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 19 | `yard-yaystal-menyat.yard-tg-bot.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=yard-yaystal-menyat.yard-tg-bot.online&port=443&secret=ee6a441d3845f1bfec1100662ce671d8ed76762e636f6d) |
| 20 | `fool.feel-fly.info` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fool.feel-fly.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |


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
