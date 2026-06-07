# 📊 نتایج استخراج: (آخرین بروزرسانی: 10:30 17-03-1405)

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
| 1 | `195.254.165.25` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.25&port=8443&secret=ee1603010200010001fc030386e24c3add646565707365656B2E636F6D) |
| 3 | `65.108.29.212` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.108.29.212&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `91.107.254.122` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.254.122&port=443&secret=ddd451f808fd60ed2c45f11d38fdbc87c5) |
| 5 | `blaze.flowaccess.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=blaze.flowaccess.site&port=443&secret=eec799e0af5c33d8ffc2310d4f0154379c626c617a652e666c6f776163636573732e73697465) |
| 6 | `78.47.129.193` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=78.47.129.193&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `91.217.166.11` | `16` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.217.166.11&port=16&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d) |
| 8 | `178.105.232.49` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.105.232.49&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `185.8.104.135` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.8.104.135&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `195.254.165.24` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.24&port=8443&secret=ee1603010200010001fc030386e24c3add646565707365656B2E636F6D) |
| 12 | `hamrah.net-sabet.adadb-1hgujoiah-xy1xutr095-tk.info.` | `1080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hamrah.net-sabet.adadb-1hgujoiah-xy1xutr095-tk.info.&port=1080&secret=79e344818749bd7ac519130220c25d09) |
| 13 | `65.108.201.8` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.108.201.8&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `sonic.quickrouteapp.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sonic.quickrouteapp.xyz&port=443&secret=eebd8b54149182b64d403ef9c5141fc3ee736f6e69632e717569636b726f7574656170702e78797a) |
| 17 | `167.233.60.38` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.233.60.38&port=443&secret=ddd77db43ee3721f0fcb40a4ff63b5cd27) |
| 18 | `www.alo-otp.info.` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.alo-otp.info.&port=25565&secret=ee104462821249bd7ac519130220c25d0963646e2e79656b74616e65742e636f6d) |


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
