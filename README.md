# 📊 نتایج استخراج: (آخرین بروزرسانی: 06:18 19-02-1405)

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License" />
  <img src="https://img.shields.io/badge/python-3.9-blue" alt="Python 3.9" />
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
| 1 | `connect.tproxyru.click` | `8980` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=connect.tproxyru.click&port=8980&secret=ee104462821249bd7ac519130220c25d09617669746f2e7275) |
| 2 | `195.254.165.253` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.253&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 3 | `calcium-credit.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=calcium-credit.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 4 | `xn--80agb2axz5d.xn--80ajveggb2e.xn--p1ai` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=xn--80agb2axz5d.xn--80ajveggb2e.xn--p1ai&port=443&secret=ee69e899d89ec68e220ca177557322b27f7275737369616e2d616e696d616c732e7275) |
| 5 | `m4in-fr4mes-are-comp1ex-but-cut3.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=m4in-fr4mes-are-comp1ex-but-cut3.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 7 | `132.243.235.196` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.235.196&port=443&secret=ee5895bbd18604365e8d18b63af6c3bfbe79616e6465782e7275) |
| 8 | `s.qcold.online` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s.qcold.online&port=853&secret=eea65967b55fdb60e0b3ac69aa46abc3de732e71636f6c642e6f6e6c696e65) |
| 10 | `akenai.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=akenai.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 12 | `tgobhod.forum` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tgobhod.forum&port=443&secret=ee1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d74676f62686f642e666f72756d) |
| 13 | `yazaebalsyadelatproxy.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=yazaebalsyadelatproxy.uk&port=443&secret=ee69e899d89ec68e220ca177557322b27f7275737369616e2d616e696d616c732e7275) |
| 14 | `132.243.235.187` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.235.187&port=443&secret=ee89db719934b04d0875b8a84c948e57fa79616e6465782e7275) |
| 16 | `188.137.250.103` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=188.137.250.103&port=443&secret=dd55e6dc2a653a5b98684624035dea96ce) |
| 17 | `how.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=how.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 18 | `132.243.235.197` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.235.197&port=443&secret=ee284388d5f6d5c468daaeb9b9fa2b01b179616e6465782e7275) |
| 19 | `172.65.117.172` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.65.117.172&port=22&secret=dd79e344818749bd7ac519130220c25d09) |


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
