# 📊 نتایج استخراج: (آخرین بروزرسانی: 20:23 05-05-1405)

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License" />
  <img src="https://img.shields.io/badge/python-3.9-blue" alt="Python 3.11" />
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
| 1 | `shir.dokhtar.hedoit.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=shir.dokhtar.hedoit.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 2 | `www.172-63.ir.` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.172-63.ir.&port=8443&secret=ee8b8238601de9360f332514afa56ada45626973636f7474692e79656b74616e65742e636f6d) |
| 3 | `adn-stg.yourservice.janosup.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=adn-stg.yourservice.janosup.ir&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 4 | `logs.jinxandjack.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=logs.jinxandjack.co.uk.&port=443&secret=eeddffffffc5a1168b2ff3eba31cbfffff7765622e62616c652e6169) |
| 5 | `mizaneshgh2.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mizaneshgh2.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `FOR-IRAN.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=FOR-IRAN.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `cdn.toconvel.digital` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cdn.toconvel.digital&port=443&secret=ee66662d8b5d623ffda118af7c38d439c163646e2e746f636f6e76656c2e6469676974616c) |
| 9 | `mirror.malevich7.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mirror.malevich7.top&port=443&secret=ee7c82f41a05f94f839fe2a11af5a7185e6d6972726f722e6d616c6576696368372e746f70) |
| 10 | `just.hedoit.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=just.hedoit.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 11 | `runpy.estakhr.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=runpy.estakhr.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 13 | `host.mizbanonline.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=host.mizbanonline.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 14 | `win.golgoli1.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=win.golgoli1.co.uk&port=2053&secret=ee1603010200010001fc030386e24c3add7777772e7961686f6f2e636f6d) |
| 15 | `signin-signout-manager.davazdah.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=signin-signout-manager.davazdah.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 16 | `www.veildrop.ir.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.veildrop.ir.&port=443&secret=ee1603010200010001fc030386e24c3add7777772e7961686f6f2e636f6d) |
| 17 | `mohandes.karshenasi.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mohandes.karshenasi.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 18 | `link.mishkalapy.life` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=link.mishkalapy.life&port=443&secret=ee593055789a7706cf0634b2ca4acb8f046c696e6b2e6d6973686b616c6170792e6c696665) |
| 19 | `go.antitspu.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=go.antitspu.com&port=443&secret=ee0608461f74efe871ce9c80067205f13e676f2e616e7469747370752e636f6d) |
| 20 | `net.pelmeshka.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=net.pelmeshka.top&port=443&secret=ee2c2bb36f545cc672afc5b80918bc08516e65742e70656c6d6573686b612e746f70) |


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
