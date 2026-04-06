# 📊 نتایج استخراج: (آخرین بروزرسانی: 16:41 17-01-1405)

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
| 1 | `delist.fictile.judgeship.prescribing.recloser.umorina.info` | `36167` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=delist.fictile.judgeship.prescribing.recloser.umorina.info&port=36167&secret=c1e93aa1bcb004d184015832673e45a9) |
| 2 | `91.99.213.141` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.99.213.141&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `167.86.100.17` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.86.100.17&port=443&secret=eed2c4dc1c928e717578dc046e6213f1ee636c6f7564666c6172652e636f6d) |
| 4 | `104.238.183.122` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=104.238.183.122&port=443&secret=9673dd2cd90fb7e75141144f6d14098e) |
| 5 | `zoomit.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zoomit.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 6 | `185.237.95.231` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.237.95.231&port=443&secret=ee4571396297582727452bf660db01b789676f6f676c652e636f6d) |
| 7 | `obxod2.vpnforum.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=obxod2.vpnforum.ru&port=443&secret=bf9f2d60e8d4ca1b376a71ea5400c7d2) |
| 8 | `how.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=how.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 9 | `i.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=i.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 11 | `142.54.189.108` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=142.54.189.108&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 12 | `catholicity.gravely.pudgy.relaxed.scatterer.superpinoy.net` | `2400` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=catholicity.gravely.pudgy.relaxed.scatterer.superpinoy.net&port=2400&secret=c6e97411bd2f36aead173ff1b945c91e) |
| 13 | `213.108.21.105` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=213.108.21.105&port=2053&secret=dd586464b7256dddfd4b5ede01693551ee) |
| 14 | `89.169.33.141` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.169.33.141&port=443&secret=eef6cf7f962f5100401aea20b56d9404df73332e616d617a6f6e6177732e636f6d) |
| 15 | `45.77.62.172` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.77.62.172&port=443&secret=875315b6c314c20e6a135ed2d5c46ebd) |
| 16 | `prxyhub.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=prxyhub.click&port=443&secret=9f27410725ab8ab84ed17daf14723236) |
| 17 | `45.32.167.239` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.32.167.239&port=443&secret=a737f5af44b8972dde5af2b384942a5b) |
| 18 | `tgproxy2.appav.net` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tgproxy2.appav.net&port=443&secret=8bf3a57e01e2d2c226113d338840793d) |
| 19 | `Fast.love-internet.xyz` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Fast.love-internet.xyz&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |


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
