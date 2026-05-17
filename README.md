# 📊 نتایج استخراج: (آخرین بروزرسانی: 06:54 27-02-1405)

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
| 1 | `calcium-credit.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=calcium-credit.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 2 | `89.125.113.189` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.125.113.189&port=443&secret=ee19835aa301cd9a6ceb68ad8d5ad9e0ac79616e6465782e7275) |
| 3 | `mtp.webvirt.cloud` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtp.webvirt.cloud&port=443&secret=ee938dd87467bc49301de2e9765cf20f4374656c2e776562766972742e636c6f7564) |
| 4 | `91.108.248.15` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.108.248.15&port=443&secret=eec42cb4ae81a45f8c81cd512599925c7c79616e6465782e7275) |
| 5 | `138.124.127.154` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=138.124.127.154&port=443&secret=ee0c480abc71136dd1c5dadf918e32cea7766b2e636f6d) |
| 6 | `195.254.165.250` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.250&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 7 | `204.168.255.33` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=204.168.255.33&port=8080&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `mt.corph.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.corph.ru&port=443&secret=ee2ed7517b077ef414e24b106e0729335d6d742e636f7270682e7275) |
| 9 | `connect.tproxyru.click` | `8980` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=connect.tproxyru.click&port=8980&secret=ee104462821249bd7ac519130220c25d09617669746f2e7275) |
| 10 | `win.sosproxy.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=win.sosproxy.space&port=443&secret=ee477ccce74a28c13a2ef6ec9e01510c3164726976652e676f6f676c652e636f6d) |
| 11 | `mt.shifor.live` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.shifor.live&port=443&secret=eee1de11495a1f99a91c4ee0c863252b586d742e736869666f722e6c697665) |
| 12 | `germany.tgproxysokol.pro` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=germany.tgproxysokol.pro&port=8443&secret=ee4215d16e455242e9b5ffb6349df285d06164732e78352e7275) |
| 13 | `dealer2-de.dealer.ac` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dealer2-de.dealer.ac&port=8443&secret=ee81535a864acce5de15b221500c24f3357477656e7475722e636f6d) |
| 14 | `95.216.222.63` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.216.222.63&port=443&secret=ee85f51151981bd69a6281f9e85395161a676f6f676c65617069732e636f6d) |
| 15 | `138.124.127.157` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=138.124.127.157&port=443&secret=ee776ed6e05e7099a53f923bdcc99f659e766b2e636f6d) |
| 17 | `185.224.215.250` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.224.215.250&port=443&secret=eea1b2c3d4e5f60123456789adadad432173332e616d617a6f6e6177732e636f6d) |
| 18 | `i-love-boobs.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=i-love-boobs.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 19 | `y0u-found-a-way-ou7-of-gorphosts-lockd0wn.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=y0u-found-a-way-ou7-of-gorphosts-lockd0wn.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 20 | `s1.proxytg.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s1.proxytg.space&port=443&secret=ee481fc4aa7c63d939142d4dbf07e1aac464726976652e676f6f676c652e636f6d) |


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
