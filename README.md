# 📊 نتایج استخراج: (آخرین بروزرسانی: 22:23 26-03-1405)

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
| 1 | `server.mizbanonline.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=server.mizbanonline.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 2 | `rudomain.info.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rudomain.info.&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 3 | `Telegram.best.ir.heazshddd.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Telegram.best.ir.heazshddd.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 4 | `proxy.speedbreaker.info` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.speedbreaker.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 5 | `87.248.129.193` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.193&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 6 | `go.proxyz.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=go.proxyz.site&port=443&secret=ee36854d344477eab338dda799b071116b676f2e70726f78797a2e73697465) |
| 7 | `abrafagh.finecooking.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=abrafagh.finecooking.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 8 | `87.248.129.202` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.202&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 9 | `cheetah-proxy.ir.hey-gardash.info.` | `1080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cheetah-proxy.ir.hey-gardash.info.&port=1080&secret=79e344818749bd7ac519130220c25d09) |
| 10 | `echo.proxym.world` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=echo.proxym.world&port=443&secret=ee03856fdd3a0b54784892677df90144a06563686f2e70726f78796d2e776f726c64) |
| 11 | `New-Empire-On-World.ir.heazshddd.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=New-Empire-On-World.ir.heazshddd.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 12 | `www.merco-karco.website` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.merco-karco.website&port=443&secret=ee1603010200010001fc030386e24c3add626973636F7474692E79656B74616E65742E636F6D) |
| 13 | `come.vak1l.ir` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=come.vak1l.ir&port=22&secret=dd79e7010200010007f0030386e24c3add) |
| 14 | `172.65.100.05` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.65.100.05&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 15 | `proxy49.arixo.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy49.arixo.shop&port=443&secret=eeb8cca49a16a3e22fdaef226700c69502617669746f2e7275) |
| 16 | `1.vak1l.ir` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=1.vak1l.ir&port=22&secret=dd79e7010200010007f0030386e24c3add) |
| 17 | `142.132.167.80` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=142.132.167.80&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 18 | `Day-and-night.ir.gybshdjls.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Day-and-night.ir.gybshdjls.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 19 | `cdn.yektanet.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cdn.yektanet.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 20 | `api.prxtoday.store` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=api.prxtoday.store&port=443&secret=ee1fed31d4c3ce8255aedc8c4c14a36f536170692e707278746f6461792e73746f7265) |


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
