# 📊 نتایج استخراج: (آخرین بروزرسانی: 19:55 15-02-1405)

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
| 1 | `2.26.125.172` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.26.125.172&port=443&secret=667161e1e8616dd33fdf8e43e40784d9) |
| 2 | `172.65.117.172` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.65.117.172&port=22&secret=dd79e344818749bd7ac519130220c25d09) |
| 3 | `6161627.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=6161627.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 4 | `i.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=i.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 5 | `yazdan.htop.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=yazdan.htop.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 6 | `gg.etherealvpn.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gg.etherealvpn.uk&port=443&secret=eee2c7176c8fc89b33fef34325dc5b9f01d186d17777772e6d6963726f736f66742e636f6d) |
| 7 | `khoda.hafez.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=khoda.hafez.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 8 | `79.137.196.223` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.137.196.223&port=8443&secret=eeeeacd334a255675ccc880cb6b8c9caf07777772e636c6f7564666c6172652e636f6d) |
| 10 | `proxy.proxymtproto.net` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.proxymtproto.net&port=443&secret=dd97caa3c6888366f26b12f994f02ecf1a) |
| 11 | `believe-gravity.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=believe-gravity.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 12 | `92.118.234.215` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=92.118.234.215&port=443&secret=dddb9b51b5ce9a2820ff62d348cb23f1b9) |
| 13 | `0xb00b5.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=0xb00b5.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 14 | `own.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=own.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 15 | `195.254.165.253` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.253&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 16 | `116.203.134.165` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=116.203.134.165&port=443&secret=ee636c6f7564666c6172652e636f6db6) |
| 17 | `89.125.113.11` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.125.113.11&port=443&secret=eebcb694130943ff7dcaf08c93b0564ff179616e6465782e7275) |
| 18 | `87.106.137.212` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.106.137.212&port=443&secret=eea1b2c3d4e5f60123456789abcdef012373332e616d617a6f6e6177732e636f6d) |
| 19 | `193.23.199.16` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=193.23.199.16&port=8443&secret=eed942e15d1c4f6a22a8c8fc1d631f6eb9646c2e676f6f676c652e636f6d) |
| 20 | `132.243.228.115` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.228.115&port=443&secret=ee3caf4d06bf6b23313068e4b3e743f91e79616e6465782e7275) |


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
