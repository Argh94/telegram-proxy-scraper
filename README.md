# 📊 نتایج استخراج: (آخرین بروزرسانی: 18:56 31-02-1405)

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
| 1 | `194.50.94.65` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.50.94.65&port=443&secret=ee0c534d144bf266c6b7a09c532a2e529f79616e6465782e7275) |
| 2 | `78.17.71.42` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=78.17.71.42&port=443&secret=eeec75b855ebcc01c982f3e013af8ed92a7777772e79616e6465782e7275) |
| 3 | `195.254.165.249` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.249&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 4 | `5.181.0.202` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.181.0.202&port=443&secret=eec11798ab008831b474066c9e1ebf5c96617669746f2e7275) |
| 5 | `185.224.215.250` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.224.215.250&port=443&secret=eea1b2c3d4e5f60123456789adadad432173332e616d617a6f6e6177732e636f6d) |
| 6 | `195.254.165.250` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.250&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 7 | `5.252.20.116` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.252.20.116&port=443&secret=eec11798ab008831b474066c9e1ebf5c93617669746f2e7275) |
| 8 | `195.254.165.253` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.253&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 9 | `hl.routefastnet.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hl.routefastnet.online&port=443&secret=eea9a5f5674069d982088b5ad27dca4584686c2e726f757465666173746e65742e6f6e6c696e65) |
| 10 | `103.110.64.211` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=103.110.64.211&port=443&secret=ee457a1d7a9004f780d4ca5ad2290f7e1a79616e6465782e7275) |
| 11 | `46.62.132.241` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.62.132.241&port=443&secret=eeae762d0e4d199c7a7085525d37e230c97777772e636c6f7564666c6172652e636f6d) |
| 12 | `178.104.244.158` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.104.244.158&port=8080&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `two.turboproxy.pro` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=two.turboproxy.pro&port=8443&secret=eec8150abdb60a541343858be088e857f66669727374627974652e7275) |
| 14 | `2.27.20.169` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.27.20.169&port=8443&secret=9f60a844dffc0498423716281fad33a5) |
| 15 | `50.7.41.162` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=50.7.41.162&port=443&secret=ee011808bcccfd224644ca7f231846a7d46d61782e7275) |
| 16 | `194.50.94.98` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.50.94.98&port=443&secret=ee75a53853cb3f53976737c82a53d4f13879616e6465782e7275) |
| 18 | `103.110.64.210` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=103.110.64.210&port=443&secret=eeaf249464f27f61e3c8f0e0dce07f413379616e6465782e7275) |
| 19 | `y0u-found-a-way-ou7-of-gorphosts-lockd0wn.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=y0u-found-a-way-ou7-of-gorphosts-lockd0wn.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 20 | `mt.rimuruproject.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.rimuruproject.ru&port=443&secret=ee0b32a6d19fd9f1c1f8b3e48c8638a29c79612e7275) |


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
