# 📊 نتایج استخراج: (آخرین بروزرسانی: 16:55 26-03-1405)

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
| 1 | `Loti.vak1l.ir` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Loti.vak1l.ir&port=22&secret=dd79e7010200010007f0030386e24c3add) |
| 2 | `87.248.129.47` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.47&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 3 | `panel-portal.managep.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=panel-portal.managep.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 4 | `87.248.129.183` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.183&port=443&secret=ee74531eb0ee43745c6ddb8efe247626cb3132333333332e732e732e732e652e6565666566656665662e69722d2d) |
| 5 | `abrafagh.finecooking.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=abrafagh.finecooking.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 6 | `Iran.mother.ir.jetish.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Iran.mother.ir.jetish.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 7 | `b8rta.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=b8rta.co.uk.&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 8 | `Telegram.best.ir.heazshddd.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Telegram.best.ir.heazshddd.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 9 | `form.quickdl.info` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=form.quickdl.info&port=22&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 10 | `87.248.129.182` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.182&port=443&secret=ee74531eb0ee43745c6ddb8efe247626cb3132333333332e732e732e732e652e6565666566656665662e69722d2d) |
| 11 | `pizza.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pizza.telbet.lol&port=25565&secret=dd79e7010200010007f0030386e24c3add) |
| 12 | `get.utkanos.life` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=get.utkanos.life&port=443&secret=ee9657c0f5d3500ab1649000fcd8a0ad816765742e75746b616e6f732e6c696665) |
| 13 | `mail.proxyz.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mail.proxyz.site&port=443&secret=ee34cce08e4b2b62d5f9b3c4d71f6bd2646d61696c2e70726f78797a2e73697465) |
| 14 | `relay.nowabst.net` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=relay.nowabst.net&port=853&secret=ee19f4ad26c65891fd22cf3b7a59f0d1036164732e78352e7275) |
| 15 | `melat.managep.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=melat.managep.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 16 | `proxy.speedbreaker.info` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.speedbreaker.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 17 | `Darvin.vak1l.ir` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Darvin.vak1l.ir&port=22&secret=dd79e7010200010007f0030386e24c3add) |
| 18 | `87.248.129.133` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.133&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 19 | `87.248.129.196` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.196&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 20 | `87.248.129.201` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.201&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |


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
