# 📊 نتایج استخراج: (آخرین بروزرسانی: 04:19 07-09-1405)

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
| 1 | `o09dhdopx.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=o09dhdopx.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `bi-bakm.37-100jamal.ir` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bi-bakm.37-100jamal.ir&port=2020&secret=00000000000000000000000000000000) |
| 3 | `79.137.196.223` | `5443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.137.196.223&port=5443&secret=eeee1b84950935ebf99951bc30e394445c9b7777772e636c6f7564666c6172652e636f6d) |
| 4 | `you.mf.7f.li.6.5nb.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=you.mf.7f.li.6.5nb.ir&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 5 | `scofield.iaubpanel.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=scofield.iaubpanel.info&port=8443&secret=1603010200010001fc030386e24c3add) |
| 6 | `ir-landofgods.fourie.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ir-landofgods.fourie.co.uk&port=8443&secret=104462821249bd7ac519130220c8dd09) |
| 7 | `65.109.147.39` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.147.39&port=443&secret=dd79e7010200010007f0030386e24c3add) |
| 8 | `noh.anotelinopalk.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=noh.anotelinopalk.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 9 | `star.talebi.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=star.talebi.co.uk&port=2096&secret=79e344818749bd7ac519130220c25d09) |
| 10 | `jasminespark.kelpmoor.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jasminespark.kelpmoor.xyz&port=443&secret=eea6765d2e85cb4496f4e0fd16b26b94c4706574726f766963682e7275) |
| 11 | `breeze.paperteapot.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=breeze.paperteapot.com&port=443&secret=eed09fb30e9ba945e3eb272875413c8c94627265657a652e7061706572746561706f742e636f6d) |
| 12 | `my.fastprx.co.uk` | `2052` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=my.fastprx.co.uk&port=2052&secret=aea1191522c9b281d2633610a34e730d) |
| 13 | `zone88.sorrelbay.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zone88.sorrelbay.xyz&port=8443&secret=ee0a717e9ba394eff63a9943ff11493cc2706574726f766963682e7275) |
| 14 | `tehran.bingi.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tehran.bingi.co.uk&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 15 | `5.222.24.244` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.222.24.244&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `731.masi.ir.he6fhd.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=731.masi.ir.he6fhd.ru&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `torobchesho.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=torobchesho.co.uk&port=443&secret=ee5f7ce28a2c4816c6c923dfd4d5630e01746f726f6263686573686f2e636f2e756b) |
| 18 | `168.119.142.46` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=168.119.142.46&port=443&secret=dd79e7010200010007f0030386e24c3add) |
| 19 | `char.torob.ir.solzairanbad.ir` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=char.torob.ir.solzairanbad.ir&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 20 | `s2.server-space52.info` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s2.server-space52.info&port=2020&secret=00000000000000000000000000000000) |


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
