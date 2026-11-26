# 📊 نتایج استخراج: (آخرین بروزرسانی: 00:11 06-09-1405)

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
| 1 | `nab.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nab.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `zenith.lanternmoss.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zenith.lanternmoss.top&port=443&secret=ee3af44f54fb6bb24e664d38ffb1a781197a656e6974682e6c616e7465726e6d6f73732e746f70) |
| 3 | `178.105.249.190` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.105.249.190&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `85.133.200.44` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=85.133.200.44&port=8880&secret=dd1603010200010001fc030386e24c3add) |
| 5 | `87.248.144.153` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.144.153&port=8880&secret=dd79e344818749bd7ac519130220c25d09) |
| 6 | `nyakawai.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nyakawai.shop&port=443&secret=eeec15a78c3842e866c302c8526175a68c7975672d6c696e6b2e7275) |
| 7 | `chat.appnormoor.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=chat.appnormoor.com&port=443&secret=dd27729feca8dbcd8008c3fa4f12d92793) |
| 8 | `galaxy.heronglade.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=galaxy.heronglade.space&port=443&secret=eedac1697485fe37f9c1435848f8ec2ff5786170692e6f7a6f6e2e7275) |
| 10 | `maraka16.ashwren.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=maraka16.ashwren.xyz&port=443&secret=ee912defad667a620d66dbf5fd0b2a1bcc62726f777365722e79616e6465782e7275) |
| 11 | `server93.server-space52.info` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=server93.server-space52.info&port=2020&secret=00000000000000000000000000000000) |
| 12 | `haf.ionox.co.uk` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=haf.ionox.co.uk&port=8880&secret=79e344818749bd7ac519130220c25d09) |
| 13 | `tech.gooodrat.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tech.gooodrat.co.uk&port=2096&secret=79e344818749bd7ac519130220c25d09) |
| 14 | `server3.esantion.info` | `2020` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=server3.esantion.info&port=2020&secret=00000000000000000000000000000000) |
| 15 | `87.248.144.60` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.144.60&port=2053&secret=79e344818749bd7ac519130220c25d09) |
| 16 | `o09dyopx.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=o09dyopx.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `light.paperteapot.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=light.paperteapot.com&port=443&secret=eed09fb30e9ba945e3eb272875413c8c946c696768742e7061706572746561706f742e636f6d) |
| 18 | `zendebad.damavand.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zendebad.damavand.co.uk&port=2096&secret=79e344818749bd7ac519130220c25d09) |
| 19 | `orchid.velvetwindow.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=orchid.velvetwindow.cc&port=443&secret=eed09fb30e9ba945e3eb272875413c8c946f72636869642e76656c76657477696e646f772e6363) |
| 20 | `support.infinityhalo.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=support.infinityhalo.co.uk&port=8443&secret=79e344818749bd7ac519130220c25d09) |


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
