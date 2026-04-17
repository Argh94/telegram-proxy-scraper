# 📊 نتایج استخراج: (آخرین بروزرسانی: 01:12 29-01-1405)

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
| 1 | `95.217.28.246` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.217.28.246&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `85.9.193.147` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=85.9.193.147&port=443&secret=ddd944d6ff91828998a095ea9b93ab7d93) |
| 3 | `hyper.sosproxy.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hyper.sosproxy.space&port=443&secret=ee44adc4da5280b196fa8192ffb712cef964726976652e676f6f676c652e636f6d) |
| 4 | `116.203.0.182` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=116.203.0.182&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `172.65.117.172` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.65.117.172&port=22&secret=dd79e344818749bd7ac519130220c25d09) |
| 6 | `27289292.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=27289292.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 7 | `3.hajrozbeh.onl` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3.hajrozbeh.onl&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 8 | `94.130.190.170` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=94.130.190.170&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `31.220.73.93` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=31.220.73.93&port=443&secret=eefd4d1b6a40aef75802cb6569f0615e11636c6f7564666c6172652e636f6d) |
| 10 | `prxyhub.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=prxyhub.click&port=443&secret=eed68360458af63073bac1394e8c7a48da707278796875622e636c69636b) |
| 11 | `FAST.tgsecurity.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=FAST.tgsecurity.online&port=443&secret=ee7c5d4e1f2a3b9c8d7e6f5a4b3c2d1e0f766b2e636f6d) |
| 12 | `142.54.189.107` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=142.54.189.107&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 13 | `195.254.165.251` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.251&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 14 | `bezobhoda.freeon.name` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bezobhoda.freeon.name&port=8443&secret=eeed1a5a7f339b8ff9840d52df123829706164732e78352e7275) |
| 15 | `31.220.73.75` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=31.220.73.75&port=443&secret=ee15561483d7091829be01a81a8b550ea4636c6f7564666c6172652e636f6d) |
| 16 | `195.254.165.253` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.253&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 17 | `akenai.tg` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=akenai.tg&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 18 | `31.220.73.75` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=31.220.73.75&port=443&secret=ee15561483d7091829be01a81a8b550ea4636c6f7564666c6172652e636f6d) |
| 19 | `news1704.mtproxygram.lol` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=news1704.mtproxygram.lol&port=443&secret=ee608248722a8f45103ed03c7994abf9b062726f777365722e79616e6465782e636f6d) |


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
