# 📊 نتایج استخراج: (آخرین بروزرسانی: 14:36 14-02-1405)

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
| 1 | `195.254.165.253` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.253&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 2 | `185.117.0.248` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.117.0.248&port=443&secret=eed451f808fd60ed2c45f11d38fdbc87c57961686f6f2e636f6d) |
| 3 | `ultra.telehelp.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ultra.telehelp.top&port=443&secret=ee1d36cba6cc6ae2eb779806189b95efb864726976652e676f6f676c652e636f6d) |
| 4 | `ctfd-is-shit.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ctfd-is-shit.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 5 | `195.254.165.252` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.252&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 6 | `94.183.177.239` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=94.183.177.239&port=443&secret=ee1f1e82326bfdd9633604a61d7df8018d7777772e6d6963726f736f66742e7275) |
| 7 | `79.137.196.223` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.137.196.223&port=8443&secret=eeeeacd334a255675ccc880cb6b8c9caf07777772e636c6f7564666c6172652e636f6d) |
| 8 | `195.254.165.247` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.247&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 9 | `akenai.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=akenai.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 10 | `178.104.98.160` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.104.98.160&port=443&secret=ee636c6f7564666c6172652e636f6db6) |
| 11 | `i-love-cu.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=i-love-cu.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 12 | `89.125.113.8` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.125.113.8&port=443&secret=eeb9e6c48a8244eecdb64a7422108aebeb79616e6465782e7275) |
| 13 | `s5.proxyru.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s5.proxyru.top&port=443&secret=eefe281d2bfa13f991ed6be43138e5e14c79612e7275) |
| 14 | `92.118.234.215` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=92.118.234.215&port=443&secret=dddb9b51b5ce9a2820ff62d348cb23f1b9) |
| 15 | `tproxyru.live.` | `8980` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tproxyru.live.&port=8980&secret=ee104462821249bd7ac519130220c25d09617669746f2e7275) |
| 16 | `195.254.165.249` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.249&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 17 | `91.107.166.142` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.166.142&port=8888&secret=ddb10c15b9f659ae2b9f1e646c9c7c1f40) |
| 18 | `how.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=how.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 19 | `connect.tproxyru.live` | `8980` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=connect.tproxyru.live&port=8980&secret=ee104462821249bd7ac519130220c25d09617669746f2e7275) |
| 20 | `87.106.137.212` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.106.137.212&port=443&secret=eea1b2c3d4e5f60123456789abcdef012373332e616d617a6f6e6177732e636f6d) |


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
