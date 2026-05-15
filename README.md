# 📊 نتایج استخراج: (آخرین بروزرسانی: 06:59 25-02-1405)

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
| 1 | `185.117.0.248` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.117.0.248&port=443&secret=eed451f808fd60ed2c45f11d38fdbc87c57961686f6f2e636f6d) |
| 2 | `132.243.235.196` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.235.196&port=443&secret=ee5895bbd18604365e8d18b63af6c3bfbe79616e6465782e7275) |
| 3 | `195.254.165.247` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.247&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 4 | `77.110.98.131` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=77.110.98.131&port=443&secret=eee81e60b985ab58eb0d4c219ed761f249616d617a6f6e2e636f6d) |
| 5 | `132.243.235.194` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.235.194&port=443&secret=eebbef585db7c10242e5b3654910e1d91479616e6465782e7275) |
| 6 | `194.120.230.199` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.120.230.199&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 7 | `swekitty.grittytarantula.sbs` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=swekitty.grittytarantula.sbs&port=443&secret=ee7c9245a98f1f79bd6f318cbd8118c10f7377656b697474792e677269747479746172616e74756c612e736273) |
| 8 | `vfast.proxytg.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vfast.proxytg.space&port=443&secret=ee4b3ce8c172e8a23ff5f953069ef6c38a64726976652e676f6f676c652e636f6d) |
| 9 | `i-love-femboys.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=i-love-femboys.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 10 | `hello.proxytg.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hello.proxytg.space&port=443&secret=ee57b7509fe484325abedc85f18804843768656c6c6f2e70726f787974672e7370616365) |
| 11 | `tp.ascel.la` | `543` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tp.ascel.la&port=543&secret=eec1f71e1f27f7169fff4d48d2d03ca39e7777772e7472656c6c6f2e636f6d) |
| 12 | `one.turboproxy.pro` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=one.turboproxy.pro&port=443&secret=ee74e2e117f2160c55370f68df7381d5d361657a612e7275) |
| 13 | `mtp.webvirt.cloud` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtp.webvirt.cloud&port=443&secret=ee938dd87467bc49301de2e9765cf20f4374656c2e776562766972742e636c6f7564) |
| 14 | `xd.rkn.lat` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=xd.rkn.lat&port=443&secret=eec58bbb0e46e9fe769afc157088d87a076d61782e7275) |
| 16 | `62.238.27.70` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.238.27.70&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `204.168.129.90` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=204.168.129.90&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `178.104.81.34` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.104.81.34&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 19 | `calcium-credit.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=calcium-credit.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 20 | `111.88.156.136` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=111.88.156.136&port=443&secret=dd8e8284414d21cdc5575cf17d59c5307e) |


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
