# 📊 نتایج استخراج: (آخرین بروزرسانی: 20:39 15-03-1405)

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
| 1 | `195.254.165.2` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.2&port=8443&secret=dd79e344818749bd7ac519130220c25d09) |
| 2 | `95.217.27.56` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.217.27.56&port=8080&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `167.233.60.38` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.233.60.38&port=443&secret=ddd77db43ee3721f0fcb40a4ff63b5cd27) |
| 4 | `info.proxytime.info` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=info.proxytime.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 6 | `185.224.3.209` | `80` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.224.3.209&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d) |
| 7 | `157.90.70.229` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=157.90.70.229&port=8443&secret=963a7fd525b04c4533ce776c9bd70f34) |
| 9 | `turbo.quickrouteapp.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=turbo.quickrouteapp.xyz&port=8443&secret=ee7e87773423c90bb0792a4e005f54119d747572626f2e717569636b726f7574656170702e78797a) |
| 10 | `65.109.247.232` | `9965` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.247.232&port=9965&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `one.nolags.pw` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=one.nolags.pw&port=443&secret=ddb42df8d0f53f13032f0e8b3e145ef053) |
| 12 | `blue.protocolsix.info` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=blue.protocolsix.info&port=22&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 14 | `blue.protocolsix.info` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=blue.protocolsix.info&port=22&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 15 | `91.107.254.122` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.254.122&port=443&secret=ddd451f808fd60ed2c45f11d38fdbc87c5) |
| 16 | `mt.nowaboost.com` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.nowaboost.com&port=853&secret=4fd95a487c5c87ae82b6639a9b6b5ff2) |
| 17 | `87.248.129.53` | `15` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.53&port=15&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 18 | `167.233.52.240` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.233.52.240&port=443&secret=ddd77db43ee3721f0fcb40a4ff63b5cd27) |
| 19 | `norm.quickdl.info` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=norm.quickdl.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 20 | `195.254.165.22` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.22&port=8443&secret=ee1603010200010001fc030386e24c3add646565707365656B2E636F6D) |


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
