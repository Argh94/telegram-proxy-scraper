# 📊 نتایج استخراج: (آخرین بروزرسانی: 01:13 11-05-1405)

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

این اسکریپت با استفاده از `requests` برای منابع متنی و کانال‌های تلگرام، پروکسی‌های MTProto را جمع‌آوری می‌کند. پروکسی‌های تکراری حذف شده و نتایج در فایل `proxy.txt` ذخیره می‌شوند. این فرآیند به‌صورت خودکار با **GitHub Actions** هر 3 ساعت اجرا می‌شود.

## 🚀 ویژگی‌ها
- 🌐 جمع‌آوری پروکسی از منابع متنی و کانال‌های تلگرام
- 🔄 به‌روزرسانی خودکار هر 3 ساعت
- 🗑 حذف پروکسی‌های تکراری
- 🔑 بدون نیاز به API تلگرام
- 📱 مناسب برای کاربران در جستجوی پروکسی‌های فعال MTProto

## 📋 پیش‌نیازها
- 🐍 پایتون 3.9
- 📦 کتابخانه‌های مورد نیاز: `requests`, `beautifulsoup4`, `pytz`, `jdatetime`
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
| 1 | `FOR-IRAN.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=FOR-IRAN.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `va7slsho.ir.meli-n13.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=va7slsho.ir.meli-n13.info&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 3 | `gate.soluqent.pro` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gate.soluqent.pro&port=443&secret=eebdbd1f66a7c00e7bf92c6436d457861d676174652e736f6c7571656e742e70726f) |
| 4 | `book.malavanann.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=book.malavanann.co.uk&port=2096&secret=ee1603010200010001fc030386e24c3add7777772e7961686f6f2e636f6d) |
| 5 | `rudomain.info.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rudomain.info.&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 6 | `portal.balalaika.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=portal.balalaika.click&port=443&secret=ee3c7b046d6a7b00b2c910cd755314eb2e706f7274616c2e62616c616c61696b612e636c69636b) |
| 7 | `f1.car-race.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=f1.car-race.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 8 | `46.225.26.227` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.225.26.227&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `chehsmat.ir.hadihoda.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=chehsmat.ir.hadihoda.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e69626973636f7474692e79656b74616e65742e636f6d) |
| 11 | `31.77.170.81` | `2443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=31.77.170.81&port=2443&secret=ee9e80d7b4d8395848062bf981d13fb3d3706c7567696e732e6a6574627261696e732e636f6d) |
| 12 | `Lashboy.muzanesghy.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Lashboy.muzanesghy.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `nachrichten.dripflux.ir.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nachrichten.dripflux.ir.&port=443&secret=ee1603010200010001fc030386e24c3add7777772e7961686f6f2e636f6d) |
| 14 | `logs.jinxandjack.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=logs.jinxandjack.co.uk.&port=443&secret=eeddffffffc5a1168b2ff3eba31cbfffff7765622e62616c652e6169) |
| 15 | `13376.ir.meli-n13.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=13376.ir.meli-n13.info&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 16 | `Strait-of-Hormuz.ir.jursdheks.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Strait-of-Hormuz.ir.jursdheks.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e69626973636f7474692e79656b74616e65742e636f6d) |
| 17 | `pathory.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pathory.co.uk.&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 18 | `17213.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=17213.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 19 | `ad3.arixo.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ad3.arixo.shop&port=443&secret=ee722fba8d97b9027b5fc4deb041b290cb6164332e617269786f2e73686f70) |


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
