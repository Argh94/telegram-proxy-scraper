# 📊 نتایج استخراج: (آخرین بروزرسانی: 15:03 04-04-1405)

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
| 1 | `tg.nowabst.net` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.nowabst.net&port=853&secret=eebfbfb8093b088269716ea5262d483e1d6164732e78352e7275) |
| 2 | `1.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=1.telbet.lol&port=25565&secret=dd79e7010200010007f0030386e24c3add) |
| 3 | `3.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3.telbet.lol&port=25565&secret=dd79e7010200010007f0030386e24c3add) |
| 4 | `194.213.118.163` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.213.118.163&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 5 | `194.233.95.205` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.233.95.205&port=443&secret=eed0ed90376601d3a5e8a71cfd42d50944676f6f676c65617069732e636f6d) |
| 6 | `just-money.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=just-money.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 7 | `sv.just-money.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sv.just-money.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 8 | `mine.talebi.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mine.talebi.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 9 | `33.mtprotonewrunningproxasia.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=33.mtprotonewrunningproxasia.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 11 | `secure.gorbushkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=secure.gorbushkin.click&port=443&secret=eebbf55b9bfecba7ac5fd1e437a7a632447365637572652e676f72627573686b696e2e636c69636b) |
| 12 | `2.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.telbet.lol&port=25565&secret=dd79e7010200010007f0030386e24c3add) |
| 13 | `go.antitspu.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=go.antitspu.com&port=443&secret=ee6217919fd71929ed6ab41f8d01e20298676f2e616e7469747370752e636f6d) |
| 14 | `login.klyuch1k.org` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=login.klyuch1k.org&port=443&secret=eecabbd4d9fd4481bbb66bcaf9f424d7c56c6f67696e2e6b6c79756368316b2e6f7267) |
| 16 | `138.201.192.170` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=138.201.192.170&port=88&secret=ee0000f00f0f775555fffffff5006e2e69626973636f7474692e79656b74616e65742e636f6d) |
| 17 | `ams1.tlgfast.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ams1.tlgfast.com&port=443&secret=083fe0c452e2407d835537872f097c54) |
| 18 | `94.249.225.233` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=94.249.225.233&port=88&secret=ee0000f00f0f775555fffffff5006e2e69626973636f7474692e79656b74616e65742e636f6d) |
| 19 | `ethereal1.arixo.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ethereal1.arixo.shop&port=443&secret=eed38044efdfe3e067bbe3e6a683a07de4657468657265616c312e617269786f2e73686f70) |


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
