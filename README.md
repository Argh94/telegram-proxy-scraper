# 📊 نتایج استخراج: (آخرین بروزرسانی: 19:17 06-09-1405)

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
| 1 | `box-to-box.dablecheckz.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=box-to-box.dablecheckz.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 2 | `shahname.ferdosisets.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=shahname.ferdosisets.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 3 | `lol-lock.godserver52.info` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lol-lock.godserver52.info&port=2020&secret=00000000000000000000000000000000) |
| 4 | `168.119.142.46` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=168.119.142.46&port=443&secret=dd79e7010200010007f0030386e24c3add) |
| 5 | `rose.heronglade.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rose.heronglade.space&port=443&secret=eef34d88320a4d0b6e8aaf11541681dd7c706574726f766963682e7275) |
| 6 | `elite.telehelp.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=elite.telehelp.top&port=443&secret=eece53761a75bac14ee003070656d8304664726976652e676f6f676c652e636f6d) |
| 7 | `ottercedar.velvetwindow.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ottercedar.velvetwindow.cc&port=443&secret=eed09fb30e9ba945e3eb272875413c8c946f7474657263656461722e76656c76657477696e646f772e6363) |
| 8 | `name.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=name.golgoli2.co.uk&port=2096&secret=79e344818749bd7ac519130220c25d09) |
| 9 | `matrixxx.wtf` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=matrixxx.wtf&port=443&secret=ee9250b2b65b8921d01a306376fc2dd2ca6d617472697878782e777466) |
| 10 | `really.azadaiu.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=really.azadaiu.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 11 | `o09opx.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=o09opx.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 12 | `79.137.196.223` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.137.196.223&port=443&secret=eeee525b778775d1c3b1e2beb8af08e2017777772e636c6f7564666c6172652e636f6d) |
| 13 | `79.137.196.223` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.137.196.223&port=8443&secret=eeeeacd334a255675ccc880cb6b8c9caf07777772e636c6f7564666c6172652e636f6d) |
| 14 | `85.133.199.22` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=85.133.199.22&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 15 | `91.107.170.11` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.170.11&port=8443&secret=79e344818749bd7ac519130220c25d09) |
| 16 | `amb.telehelp.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=amb.telehelp.top&port=443&secret=ee5447efddb6d2d618e850c2f2eef65b5964726976652e676f6f676c652e636f6d) |
| 17 | `jadide.mamadali.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jadide.mamadali.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `hadaf.golgoli2.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hadaf.golgoli2.co.uk&port=2053&secret=79e344818749bd7ac519130220c25d09) |
| 19 | `karbon.torobchesho.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=karbon.torobchesho.co.uk&port=443&secret=ee79e344828749bd7ac519130220c25d096b6172626f6e2e746f726f6263686573686f2e636f2e756b) |
| 20 | `char.torob.ir.solzairanbad.ir` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=char.torob.ir.solzairanbad.ir&port=8880&secret=79e344818749bd7ac519130220c25d09) |


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
