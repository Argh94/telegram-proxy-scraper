# 📊 نتایج استخراج: (آخرین بروزرسانی: 05:00 31-04-1405)

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
| 1 | `207pana.denatara.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=207pana.denatara.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 2 | `3.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3.telbet.lol&port=25565&secret=dd79e7010200010007f0030386e24c3add) |
| 3 | `football.world-pro.co.uk` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=football.world-pro.co.uk&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 4 | `qqpp7hhhuuu991m2.ir.meli-n13.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=qqpp7hhhuuu991m2.ir.meli-n13.info&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 5 | `cstudio.semiconductor.mistloop.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cstudio.semiconductor.mistloop.ir&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 6 | `2e9f6jwj1.mmd1.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2e9f6jwj1.mmd1.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `Strait-of-Hormuz.ir.jursdheks.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Strait-of-Hormuz.ir.jursdheks.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 8 | `b.sub-ploter.co.uk` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=b.sub-ploter.co.uk&port=22&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 9 | `www.172-63.ir.` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.172-63.ir.&port=8443&secret=ee8b8238601de9360f332514afa56ada45626973636f7474692e79656b74616e65742e636f6d) |
| 10 | `come.vak1l.ir` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=come.vak1l.ir&port=22&secret=dd79e7010200010007f0030386e24c3add) |
| 11 | `shir.dokhtar.hedoit.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=shir.dokhtar.hedoit.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 12 | `permiiium.lavazemi2.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=permiiium.lavazemi2.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add7777772e7961686f6f2e636f6d) |
| 14 | `ad1.arixo.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ad1.arixo.shop&port=443&secret=eee09f46368021f91b92ad3dea14c7ac896164312e617269786f2e73686f70) |
| 15 | `cdn.savelyev.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cdn.savelyev.click&port=443&secret=ee289573f97532f1d66fe239efbf0585ad63646e2e736176656c7965762e636c69636b) |
| 16 | `jounob-iran-dar-ghalb-mast.simbol.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jounob-iran-dar-ghalb-mast.simbol.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 18 | `api.medhata.org` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=api.medhata.org&port=443&secret=ee32bc9ea34e230a726f9364c05e4ea2086170692e6d6564686174612e6f7267) |
| 19 | `7001m1.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=7001m1.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `kala.golgoli1.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kala.golgoli1.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add7777772e7961686f6f2e636f6d) |


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
