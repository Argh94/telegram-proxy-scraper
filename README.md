# 📊 نتایج استخراج: (آخرین بروزرسانی: 14:34 07-09-1405)

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
| 1 | `node3.serverix.cloud` | `3252` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=node3.serverix.cloud&port=3252&secret=ee511203dfda7df167a06c0b772e12018e7777772e676f6f676c652e636f6d) |
| 2 | `parts.kemerovo.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=parts.kemerovo.online&port=443&secret=ee1111222233334444555566667777888874342e6d79726b612e6469676974616c) |
| 3 | `88.99.30.66` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=88.99.30.66&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `79.137.196.223` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.137.196.223&port=443&secret=eeee525b778775d1c3b1e2beb8af08e2017777772e636c6f7564666c6172652e636f6d) |
| 5 | `sq.oy.8v.9m.f.f6.6ld.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sq.oy.8v.9m.f.f6.6ld.ir&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 6 | `2.masi.ir.he6fhd.ru` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.masi.ir.he6fhd.ru&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `red.telehelp.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=red.telehelp.top&port=443&secret=eefa58f5720fab51caf38ad09ee80c16d964726976652e676f6f676c652e636f6d) |
| 8 | `ultraproxy.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ultraproxy.shop&port=443&secret=eeec15a78c3842e866c302c8526175a68c7975672d6c696e6b2e7275) |
| 9 | `torobchesho.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=torobchesho.co.uk&port=443&secret=ee5f7ce28a2c4816c6c923dfd4d5630e01746f726f6263686573686f2e636f2e756b) |
| 10 | `gardenkite.heronglade.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gardenkite.heronglade.space&port=443&secret=ee4b20619b99880640b45f275c18e20555706574726f766963682e7275) |
| 11 | `188.40.68.169` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=188.40.68.169&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 12 | `elite.telehelp.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=elite.telehelp.top&port=443&secret=eece53761a75bac14ee003070656d8304664726976652e676f6f676c652e636f6d) |
| 13 | `uk-02.rrhosting.eu` | `7960` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=uk-02.rrhosting.eu&port=7960&secret=ee6670c1d7f2cb97920f59142e6044d4567777772e676f6f676c652e636f6d) |
| 14 | `5.222.24.244` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.222.24.244&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `laurelbreeze.sorrelbay.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=laurelbreeze.sorrelbay.xyz&port=8443&secret=ee827bb7e0257a090d747ba7dde413ab0562726f777365722e79616e6465782e7275) |
| 16 | `48.mt.p6.fo.s.u.44-94-14-4.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=48.mt.p6.fo.s.u.44-94-14-4.ir&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 17 | `nab.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nab.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `65.109.98.231` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.98.231&port=443&secret=dd79e7010200010007f0030386e24c3add) |
| 20 | `135.181.74.183` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=135.181.74.183&port=443&secret=dd79e7010200010007f0030386e24c3add) |


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
