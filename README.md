# 📊 نتایج استخراج: (آخرین بروزرسانی: 23:44 30-02-1405)

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
| 1 | `mt.rimuruproject.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.rimuruproject.ru&port=443&secret=ee0b32a6d19fd9f1c1f8b3e48c8638a29c79612e7275) |
| 2 | `w.arixo.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=w.arixo.shop&port=443&secret=eec11798ab008831b474066c9e1ebf5c97617669746f2e7275) |
| 3 | `ak.yourline.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ak.yourline.online&port=443&secret=eed74b20f8b196edebcfdc6de8c8985d60616b2e796f75726c696e652e6f6e6c696e65) |
| 4 | `195.254.165.250` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.250&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 6 | `195.254.165.247` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.247&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 7 | `62.238.27.70` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.238.27.70&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `144.31.54.207` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=144.31.54.207&port=443&secret=eec5081bcd191b76e90ee894d248e44c42706574726f766963682e7275) |
| 9 | `mt.shifor.live` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.shifor.live&port=443&secret=eee1de11495a1f99a91c4ee0c863252b586d742e736869666f722e6c697665) |
| 10 | `87.120.108.48` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.120.108.48&port=443&secret=074e7d1d37cc043746fd0c823f20d21a) |
| 11 | `y0u-found-a-way-ou7-of-gorphosts-lockd0wn.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=y0u-found-a-way-ou7-of-gorphosts-lockd0wn.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 12 | `He.jlpoKcu.cloud` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=He.jlpoKcu.cloud&port=443&secret=ee3f8a91c2d7e04b6a9f12c5e8370bd4aa786170692e6f7a6f6e2e7275) |
| 13 | `mtp.webvirt.cloud` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtp.webvirt.cloud&port=443&secret=ee938dd87467bc49301de2e9765cf20f4374656c2e776562766972742e636c6f7564) |
| 14 | `tp.ascel.la` | `543` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tp.ascel.la&port=543&secret=eec1f71e1f27f7169fff4d48d2d03ca39e7777772e7472656c6c6f2e636f6d) |
| 15 | `89.125.113.155` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.125.113.155&port=443&secret=ee67af7b545eb72c3c47fc2ccb74aa41c979616e6465782e7275) |
| 16 | `45.39.33.160` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.39.33.160&port=443&secret=ee39f8e9a2673ca05251ec002f7e7eff6e7777772e6d6963726f736f66742e636f6d) |
| 17 | `37.27.38.205` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=37.27.38.205&port=443&secret=ee9d659fc2ae43e0b8323c082960233d7b7777772e636c6f7564666c6172652e636f6d) |
| 19 | `one.turboproxy.pro` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=one.turboproxy.pro&port=443&secret=ee74e2e117f2160c55370f68df7381d5d361657a612e7275) |
| 20 | `103.110.64.213` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=103.110.64.213&port=443&secret=eecb034302623216896e2887011d848d6479616e6465782e7275) |


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
