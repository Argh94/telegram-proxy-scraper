# 📊 نتایج استخراج: (آخرین بروزرسانی: 02:23 29-03-1405)

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
| 1 | `Iran.mother.ir.jetish.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Iran.mother.ir.jetish.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 2 | `proxy.speedbreaker.info` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.speedbreaker.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 3 | `87.120.216.254` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.120.216.254&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 4 | `room.coworcker.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=room.coworcker.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 5 | `login.veltura.digital` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=login.veltura.digital&port=443&secret=ee4f5545c56e0ee3271606a2985459773e6c6f67696e2e76656c747572612e6469676974616c) |
| 6 | `Loti.vak1l.ir` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Loti.vak1l.ir&port=22&secret=dd79e7010200010007f0030386e24c3add) |
| 8 | `junior.ir.the-nice-mtproto.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=junior.ir.the-nice-mtproto.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 9 | `For.you.ir.gdhbvjshjrf.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=For.you.ir.gdhbvjshjrf.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 10 | `167.233.159.224` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.233.159.224&port=8443&secret=dd79e344818749bd7ac519130220c25d09) |
| 11 | `go.pelmeshka.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=go.pelmeshka.top&port=443&secret=ee3b27756fba95be04fa17a91e1fb1434e676f2e70656c6d6573686b612e746f70) |
| 12 | `For.dear-iranian-people.com.heazshddd.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=For.dear-iranian-people.com.heazshddd.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 13 | `1.vak1l.ir` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=1.vak1l.ir&port=22&secret=dd79e7010200010007f0030386e24c3add) |
| 14 | `login.klyuch1k.org` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=login.klyuch1k.org&port=443&secret=ee7b0d5223fb0484933823a8e0e823194c6c6f67696e2e6b6c79756368316b2e6f7267) |
| 15 | `Day-and-night.ir.gybshdjls.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Day-and-night.ir.gybshdjls.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 16 | `go.antitspu.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=go.antitspu.com&port=443&secret=ee31d386ef7e695ee39f4f28ecfbd28a37676f2e616e7469747370752e636f6d) |
| 17 | `cdn.ma-rd.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cdn.ma-rd.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 18 | `digi.technom.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=digi.technom.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |


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
