# 📊 نتایج استخراج: (آخرین بروزرسانی: 06:12 15-02-1405)

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
| 1 | `89.125.113.15` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.125.113.15&port=443&secret=eee2aa8eea0145d9f9807b628705d6ea9379616e6465782e7275) |
| 2 | `win.sosproxy.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=win.sosproxy.space&port=443&secret=ee477ccce74a28c13a2ef6ec9e01510c3164726976652e676f6f676c652e636f6d) |
| 3 | `s.qcold.online` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s.qcold.online&port=853&secret=eea65967b55fdb60e0b3ac69aa46abc3de732e71636f6c642e6f6e6c696e65) |
| 4 | `proxy.proxymtproto.net` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.proxymtproto.net&port=443&secret=dd97caa3c6888366f26b12f994f02ecf1a) |
| 5 | `labuten.strawberries.cfd` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=labuten.strawberries.cfd&port=853&secret=ee58639c2a0869a8d109d1b6dde1aa98c677622e7275) |
| 6 | `185.117.0.248` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.117.0.248&port=443&secret=eed451f808fd60ed2c45f11d38fdbc87c57961686f6f2e636f6d) |
| 7 | `own.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=own.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 8 | `89.125.113.10` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.125.113.10&port=443&secret=ee700a15adb4cca8106fe1e0ad0dd35ce879616e6465782e7275) |
| 9 | `nya-nya.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nya-nya.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 10 | `how.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=how.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 11 | `believe-gravity.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=believe-gravity.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 13 | `proxytg.fit` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxytg.fit&port=443&secret=eec8f164f338f20e2e3c7a0f4e0408a51270726f787974672e666974) |
| 14 | `195.254.165.247` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.247&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 17 | `172.65.102.115` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.65.102.115&port=22&secret=dd79e344818749bd7ac519130220c25d09) |
| 18 | `195.254.165.250` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.250&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 19 | `89.125.113.14` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.125.113.14&port=443&secret=ee3e7641e0b5826dee9d6b6b265bfe05ed79616e6465782e7275) |
| 20 | `89.125.113.12` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.125.113.12&port=443&secret=ee5c435541940799bc8d9d4b591d62ddc179616e6465782e7275) |


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
