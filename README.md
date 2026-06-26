# 📊 نتایج استخراج: (آخرین بروزرسانی: 15:10 05-04-1405)

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
| 1 | `blue.protocolsix.info` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=blue.protocolsix.info&port=22&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 2 | `194.213.118.163` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.213.118.163&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 3 | `googel.alo-otp.info.` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=googel.alo-otp.info.&port=25565&secret=ee104462821249bd7ac519130220c25d0963646e2e79656b74616e65742e636f6d) |
| 4 | `br.kingproxynewdomailasiatech.ink` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=br.kingproxynewdomailasiatech.ink&port=22&secret=dd79e7010200010007f0030386e24c3add) |
| 5 | `h.hajagha.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=h.hajagha.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 6 | `Loti.vak1l.ir` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Loti.vak1l.ir&port=22&secret=dd79e7010200010007f0030386e24c3add) |
| 7 | `62.3.12.2` | `8444` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.3.12.2&port=8444&secret=ee6f7a6f6e2e7275f22c5421fa893965) |
| 8 | `so-cpu.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=so-cpu.co.uk.&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 10 | `87.248.129.180` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.180&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 11 | `stockholm.viking-vibe.co.uk` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=stockholm.viking-vibe.co.uk&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 12 | `fresh.t-proxy.info.` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fresh.t-proxy.info.&port=25565&secret=ee104462821249bd7ac519130220c25d0963646e2e79656b74616e65742e636f6d) |
| 13 | `book.malavanann.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=book.malavanann.co.uk&port=2053&secret=ee1603010200010001fc030386e24c3add706c61792e676f6f676c652e636f6d) |
| 14 | `www.merco-karco.website` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.merco-karco.website&port=443&secret=ee1603010200010001fc030386e24c3add626973636F7474692E79656B74616E65742E636F6D) |
| 15 | `malmo.viking-vibe.co.uk` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=malmo.viking-vibe.co.uk&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 16 | `sv2.hajhossein.observer` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sv2.hajhossein.observer&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 17 | `87.248.129.179` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.179&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 18 | `proxy65.arixo.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy65.arixo.shop&port=443&secret=ee3ceb82a3b4254e6e6ae1971021f3c209617669746f2e7275) |
| 19 | `87.248.129.180` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.180&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 20 | `b8rta.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=b8rta.co.uk.&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |


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
