# 📊 نتایج استخراج: (آخرین بروزرسانی: 01:12 29-04-1405)

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
| 2 | `ad4.arixo.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ad4.arixo.shop&port=443&secret=eec699329f2f8c2d33cd1e1a9f10e5d32d6164312e617269786f2e73686f70) |
| 4 | `sv2.just-money.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sv2.just-money.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 5 | `178.104.176.206` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.104.176.206&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `relay.neoqua.pro` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=relay.neoqua.pro&port=443&secret=ee368216360fa09c0c83149537f4ff23b972656c61792e6e656f7175612e70726f) |
| 7 | `49.12.117.95` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=49.12.117.95&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `tg.nftauctiontg.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.nftauctiontg.online&port=443&secret=ee82dd6ba1475a9793a9613364fee70e2f74672e6e667461756374696f6e74672e6f6e6c696e65) |
| 10 | `basic.here-funnycloud.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=basic.here-funnycloud.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 11 | `moon.talebi.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=moon.talebi.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 13 | `biaberim.estakhr.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=biaberim.estakhr.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 14 | `sv4.just-money.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sv4.just-money.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 15 | `app.librava.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=app.librava.click&port=443&secret=eefb55d5d8eb78368af5bf96be5b6cd09a6170702e6c6962726176612e636c69636b) |
| 16 | `5.75.218.54` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.75.218.54&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `blond.basicscotch.co.uk` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=blond.basicscotch.co.uk&port=25565&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 19 | `most.karshenasi.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=most.karshenasi.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |


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
