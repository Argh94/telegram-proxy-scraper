# 📊 نتایج استخراج: (آخرین بروزرسانی: 05:58 09-01-1405)

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
| 1 | `91.107.182.200` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.182.200&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `45.139.29.50` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.139.29.50&port=8443&secret=ddf672deb6dcac2f471e8ccffb1eacc82f) |
| 3 | `195.254.165.249` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.249&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 4 | `5.39.250.20` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.39.250.20&port=443&secret=6356ebb33a57b6deda8a1c3cf2aee557) |
| 5 | `147.125.130.62` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=147.125.130.62&port=2083&secret=ee1603010200010001fc030386e24c3add68656c702e737465616d706f77657265642e636f6d) |
| 6 | `2.27.21.235` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.27.21.235&port=443&secret=ee636c6f7564666c6172652e636f6d02) |
| 7 | `185.237.95.231` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.237.95.231&port=443&secret=ee4571396297582727452bf660db01b789676f6f676c652e636f6d) |
| 8 | `dedicated.love-internet.xyz` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dedicated.love-internet.xyz&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |
| 9 | `147.125.130.47` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=147.125.130.47&port=2083&secret=ee1603010200010001fc030386e24c3add68656c702e737465616d706f77657265642e636f6d) |
| 10 | `144.31.230.217` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=144.31.230.217&port=443&secret=33d73370103ea05acd9418eb9dca989e) |
| 11 | `193.23.195.203` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=193.23.195.203&port=443&secret=dd6ca4bc3ac2493c924bd21db211bb910d) |
| 12 | `chipolata.flavorus.hoaxer.rattrap.scrub.akoypinoytv.net` | `7800` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=chipolata.flavorus.hoaxer.rattrap.scrub.akoypinoytv.net&port=7800&secret=bf027426b873e9821394c097a696ba61) |
| 13 | `195.254.165.250` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.250&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 14 | `195.254.165.247` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.247&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 15 | `free.tgsecurity.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=free.tgsecurity.online&port=443&secret=dd7c5d4e1f2a3b9c8d7e6f5a4b3c2d1e0f) |
| 16 | `45.90.13.34` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.90.13.34&port=443&secret=dda85f2776cc83dbff66b440fb03050cf7) |
| 17 | `utkapay.life` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=utkapay.life&port=443&secret=eec0ab2dc91cd75da14bf8bde752ca8222766473696e612e7275) |
| 18 | `147.125.130.18` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=147.125.130.18&port=2083&secret=ee1603010200010001fc030386e24c3add68656c702e737465616d706f77657265642e636f6d) |
| 20 | `147.125.130.65` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=147.125.130.65&port=2083&secret=ee1603010200010001fc030386e24c3add68656c702e737465616d706f77657265642e636f6d) |


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
