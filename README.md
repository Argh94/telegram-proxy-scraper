# 📊 نتایج استخراج: (آخرین بروزرسانی: 01:13 19-01-1405)

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
| 1 | `195.254.165.247` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.247&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 3 | `176.123.165.52` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=176.123.165.52&port=443&secret=dd7c5d4e1f2a3b9c8d7e6f5a4b3c2d1e0f) |
| 5 | `72.60.186.130` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=72.60.186.130&port=8443&secret=ddfaec0dfe42eb966f1ebf85e262b9130e) |
| 6 | `he.de-fa.1.mtproto.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=he.de-fa.1.mtproto.ru&port=443&secret=ee2111222233334444555566667777888862726f777365722e79616e6465782e636f6d) |
| 7 | `91.186.216.239` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.186.216.239&port=8443&secret=eeb359972f13e568d2e15bc826257028d56d61782e7275) |
| 8 | `go.bolshevps.su` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=go.bolshevps.su&port=443&secret=ee617782cbbfb6dcc27b0e338f570da65f6164732e78352e7275) |
| 9 | `tg.shadeproxy.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.shadeproxy.ru&port=443&secret=dd9c19f63098a0e4f32bb78cfd3c573373) |
| 10 | `150.251.152.189` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=150.251.152.189&port=8443&secret=dd036f220431a6387a4094622dbdab8014) |
| 11 | `150.241.68.217` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=150.241.68.217&port=443&secret=d58f4e5985c8e84d72fa59a46cfa14cd) |
| 12 | `own.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=own.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 13 | `195.254.165.250` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.250&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 14 | `FAST.tgsecurity.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=FAST.tgsecurity.online&port=443&secret=ee7c5d4e1f2a3b9c8d7e6f5a4b3c2d1e0f766b2e636f6d) |
| 15 | `proxytop.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxytop.space&port=443&secret=7d793037a0760186574b0282f2f435e7) |
| 16 | `tg.vpnspacev.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.vpnspacev.com&port=443&secret=bc184fc14b62b9b1dc5f34edf9476421) |
| 17 | `195.254.165.252` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.252&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 18 | `158.160.232.216` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=158.160.232.216&port=443&secret=ee79612e727537ff352dabe2604c3fe5) |
| 19 | `195.254.165.247` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.247&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
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
