# 📊 نتایج استخراج: (آخرین بروزرسانی: 14:52 25-02-1405)

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
| 1 | `two.turboproxy.pro` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=two.turboproxy.pro&port=8443&secret=eec8150abdb60a541343858be088e857f66669727374627974652e7275) |
| 2 | `144.31.221.15` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=144.31.221.15&port=443&secret=a882fe13626155c2ea56b8b79639576c) |
| 3 | `178.104.81.34` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.104.81.34&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `194.120.230.199` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.120.230.199&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 5 | `i-love-hse.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=i-love-hse.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 6 | `194.50.94.98` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.50.94.98&port=443&secret=ee75a53853cb3f53976737c82a53d4f13879616e6465782e7275) |
| 8 | `s1.proxytg.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s1.proxytg.space&port=443&secret=ee481fc4aa7c63d939142d4dbf07e1aac464726976652e676f6f676c652e636f6d) |
| 9 | `one.turboproxy.pro` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=one.turboproxy.pro&port=443&secret=ee74e2e117f2160c55370f68df7381d5d361657a612e7275) |
| 10 | `138.124.79.102` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=138.124.79.102&port=443&secret=eeef989ce1d22d2afce85121376fed00176d61782e7275) |
| 11 | `espress0-macch1ato-p0r-favor3.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=espress0-macch1ato-p0r-favor3.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 12 | `tproxyru.live.` | `8980` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tproxyru.live.&port=8980&secret=ee104462821249bd7ac519130220c25d09617669746f2e7275) |
| 13 | `hello.proxytg.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hello.proxytg.space&port=443&secret=ee57b7509fe484325abedc85f18804843768656c6c6f2e70726f787974672e7370616365) |
| 14 | `138.124.127.157` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=138.124.127.157&port=443&secret=ee776ed6e05e7099a53f923bdcc99f659e766b2e636f6d) |
| 15 | `lovevesper.zoryx.tech` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lovevesper.zoryx.tech&port=853&secret=ee2a43151ca1c75d56a2f8f63c87bfaae374726176656c6c696e652e7275) |
| 16 | `proxy.fluxoria.it.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.fluxoria.it.com&port=443&secret=ee307242dd41275c771f40035565d0750a70726f78792e666c75786f7269612e69742e636f6d) |
| 17 | `195.254.165.247` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.247&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 18 | `germany.tgproxysokol.pro` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=germany.tgproxysokol.pro&port=8443&secret=ee4215d16e455242e9b5ffb6349df285d06164732e78352e7275) |
| 19 | `204.168.129.90` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=204.168.129.90&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `195.254.165.250` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.250&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |


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
