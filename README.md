# 📊 نتایج استخراج: (آخرین بروزرسانی: 16:28 16-01-1405)

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
| 3 | `hk.582597.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hk.582597.xyz&port=443&secret=eeb578f1c1d404356dc5527e6bc6569166617a7572652e6d6963726f736f66742e636f6d) |
| 5 | `hyper.happvpn.cc` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hyper.happvpn.cc&port=8443&secret=ee4852c1c04ab83db8a328c60eaf9a0db268797065722e6861707076706e2e6363) |
| 6 | `195.254.165.241` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.241&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 7 | `195.254.165.253` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.253&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 8 | `146.185.241.89` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=146.185.241.89&port=443&secret=c351841a608cca24813a321aa080bc91) |
| 9 | `195.254.165.251` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.251&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 10 | `proxytelega.store` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxytelega.store&port=443&secret=5d41402abc4b2a76b9719d911017c592) |
| 11 | `107.175.189.200` | `8447` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=107.175.189.200&port=8447&secret=554b3dd4c9d6fbbe2101c12765bb4229) |
| 12 | `be-free.stevbotview.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=be-free.stevbotview.ru&port=443&secret=eebc4aaf28ba8d24b41ae66a63035aa02562652d667265652e73746576626f74766965772e7275) |
| 13 | `jtproxy.life` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jtproxy.life&port=443&secret=eef0050d30441bab41f60acae779df0c40766473696e612e7275) |
| 14 | `soft.telegramharvester.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=soft.telegramharvester.ru&port=443&secret=ee05ca1fb5eadbac1e7e8c725695b48f0079612e7275) |
| 15 | `45.32.218.218` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.32.218.218&port=443&secret=b118904a6270d45988b34bc4a2ef235b) |
| 16 | `190.2.142.185` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=190.2.142.185&port=8443&secret=63f84be1fa69afb85f70d273f3e4d557) |
| 17 | `dowd.sportsmanship.steeplechaser.thy.urceolate.kapitoshka.info` | `15417` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dowd.sportsmanship.steeplechaser.thy.urceolate.kapitoshka.info&port=15417&secret=d6db8ab62ff9b9f70f6ca15ccb98c222) |
| 18 | `216.128.130.87` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=216.128.130.87&port=443&secret=5a3070d6a81a4b65b0f820662506979b) |
| 19 | `proxlet.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxlet.site&port=443&secret=8d969eef6ecad3c29a3a629280e686cf) |
| 20 | `172.65.117.172` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.65.117.172&port=22&secret=dd79e344818749bd7ac519130220c25d09) |


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
