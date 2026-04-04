# 📊 نتایج استخراج: (آخرین بروزرسانی: 16:26 15-01-1405)

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
| 1 | `peyk.acharbashi.info` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=peyk.acharbashi.info&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |
| 2 | `155.138.202.81` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=155.138.202.81&port=443&secret=9e4862383f46562395c4c546479acd33) |
| 3 | `108.61.179.245` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=108.61.179.245&port=443&secret=e8fc2977f2a2ac84d99e895d0a96884f) |
| 4 | `tg.safepal.life` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.safepal.life&port=443&secret=ee7c5474451d78bb07ae047680e9de3d8079616e6465782e6e6574) |
| 5 | `95.216.28.120` | `6800` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.216.28.120&port=6800&secret=4dcebaabeb692bdc9ad03486b090da76) |
| 6 | `90.156.150.59` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=90.156.150.59&port=443&secret=9a327c9c52a366e306fd74d617de517d) |
| 7 | `2.27.23.23` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.27.23.23&port=8443&secret=f5a97ceadd1bbedd918fbd9f1c9387dd) |
| 8 | `89.208.85.188` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.208.85.188&port=8443&secret=eea94a50c3db2b9e640351831e8bd42bba6164732e78352e7275) |
| 9 | `193.104.198.0` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=193.104.198.0&port=443&secret=dd40aa72a0f79e4f3b2be25dd56e07de72) |
| 10 | `66.42.120.23` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=66.42.120.23&port=443&secret=46a67591e903fe25c32c983024284c8b) |
| 11 | `94.156.115.80` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=94.156.115.80&port=443&secret=ee470cb2b8b29aeadfbdf8a2f7bee5ca3b62726f777365722e79616e6465782e636f6d) |
| 12 | `Fast.love-internet.xyz` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Fast.love-internet.xyz&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |
| 13 | `64.188.65.63` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=64.188.65.63&port=443&secret=14f9b82c38f7cc3f9f938277dc6c6038) |
| 14 | `185.237.95.231` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.237.95.231&port=443&secret=ee4571396297582727452bf660db01b789676f6f676c652e636f6d) |
| 15 | `pivo.shukafish.ru` | `5443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pivo.shukafish.ru&port=5443&secret=ddf5199e949c0f23bc887581218ad8c1e6) |
| 16 | `150.241.66.222` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=150.241.66.222&port=443&secret=dd3d8f75897e52b428eeca825810bbc79f) |
| 17 | `146.185.241.89` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=146.185.241.89&port=443&secret=c351841a608cca24813a321aa080bc91) |
| 18 | `laura.proxyprosto.sbs` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=laura.proxyprosto.sbs&port=443&secret=ee79612e7275dcdfd8017f6ee7c1beb0) |
| 19 | `176.108.255.233` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=176.108.255.233&port=443&secret=dd7c5d4e1f2a3b9c8d7e6f5a4b3c2d1e0f) |
| 20 | `utkapay.life` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=utkapay.life&port=443&secret=eec0ab2dc91cd75da14bf8bde752ca8222766473696e612e7275) |


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
