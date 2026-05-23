# 📊 نتایج استخراج: (آخرین بروزرسانی: 19:32 02-03-1405)

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
| 1 | `78.17.71.42` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=78.17.71.42&port=443&secret=eeec75b855ebcc01c982f3e013af8ed92a7777772e79616e6465782e7275) |
| 2 | `y0u-found-a-way-ou7-of-gorphosts-lockd0wn.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=y0u-found-a-way-ou7-of-gorphosts-lockd0wn.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 3 | `2.27.41.207` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.27.41.207&port=443&secret=9436fa39ab47ccb34f217ac6d06b4e58) |
| 4 | `178.104.81.34` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.104.81.34&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `mtp.yard-tg-bot.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtp.yard-tg-bot.ru&port=443&secret=eef658bb6d89b284874149c13e7d27d9da79616e6465782e7275) |
| 6 | `178.104.244.158` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.104.244.158&port=8080&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `wave.proxyu.site` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=wave.proxyu.site&port=8443&secret=ee38a4d5d648d6af5196c71c2018eb6fa6776176652e70726f7879752e73697465) |
| 8 | `one.turboproxy.pro` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=one.turboproxy.pro&port=443&secret=ee74e2e117f2160c55370f68df7381d5d361657a612e7275) |
| 9 | `two.turboproxy.pro` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=two.turboproxy.pro&port=8443&secret=eec8150abdb60a541343858be088e857f66669727374627974652e7275) |
| 10 | `195.254.165.143` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.143&port=4455&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d) |
| 12 | `50.7.41.162` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=50.7.41.162&port=443&secret=ee011808bcccfd224644ca7f231846a7d46d61782e7275) |
| 13 | `espress0-macch1ato-p0r-favor3.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=espress0-macch1ato-p0r-favor3.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 14 | `87.120.108.48` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.120.108.48&port=443&secret=074e7d1d37cc043746fd0c823f20d21a) |
| 15 | `186.246.16.232` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=186.246.16.232&port=443&secret=eec11798ab008831b474066c9e1ebf5c85617669746f2e7275) |
| 16 | `37.27.38.205` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=37.27.38.205&port=443&secret=ee9d659fc2ae43e0b8323c082960233d7b7777772e636c6f7564666c6172652e636f6d) |
| 17 | `proxy.fluxoria.it.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.fluxoria.it.com&port=443&secret=ee307242dd41275c771f40035565d0750a70726f78792e666c75786f7269612e69742e636f6d) |
| 18 | `mt.nowaboost.com` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.nowaboost.com&port=853&secret=4fd95a487c5c87ae82b6639a9b6b5ff2) |
| 19 | `62.238.27.70` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.238.27.70&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `mt.shifor.live` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.shifor.live&port=443&secret=eee1de11495a1f99a91c4ee0c863252b586d742e736869666f722e6c697665) |


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
