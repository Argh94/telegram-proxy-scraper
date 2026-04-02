# 📊 نتایج استخراج: (آخرین بروزرسانی: 22:28 13-01-1405)

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
| 1 | `95.216.178.41` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.216.178.41&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `95.85.231.6` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.85.231.6&port=8443&secret=46b107169c2e3968abc49eba40928782) |
| 3 | `utkapay.life` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=utkapay.life&port=443&secret=eec0ab2dc91cd75da14bf8bde752ca8222766473696e612e7275) |
| 4 | `proxym.world` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxym.world&port=443&secret=1b6453892473a467d07372d45eb05abc) |
| 5 | `185.174.137.50` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.174.137.50&port=8443&secret=676c4049812b842b7792954bf2a32943) |
| 6 | `116.203.134.165` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=116.203.134.165&port=443&secret=ee636c6f7564666c6172652e636f6db6) |
| 7 | `6161627.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=6161627.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 8 | `mt.fl8.vdl.lat` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.fl8.vdl.lat&port=443&secret=dd1a21752bd8823f6d2e7ac3642f2608ac) |
| 9 | `204.168.204.85` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=204.168.204.85&port=443&secret=ee414d88c9e2cee256c6d242797c69927d636c6f7564666c6172652e636f6d) |
| 10 | `0da62.blancproxy.link` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=0da62.blancproxy.link&port=443&secret=dd97c420070f5eb3ba3c22b9635576d9f1) |
| 11 | `proxium.rest` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxium.rest&port=443&secret=a665a45920422f9d417e4867efdc4fb8) |
| 12 | `188.137.232.184` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=188.137.232.184&port=443&secret=ee6293ee0eaa15186ea42d9b571b9275b17777772e636c6f7564666c6172652e636f6d) |
| 13 | `hyper.happvpn.cc` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hyper.happvpn.cc&port=8443&secret=ee4852c1c04ab83db8a328c60eaf9a0db268797065722e6861707076706e2e6363) |
| 14 | `proxyobhod.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxyobhod.online&port=443&secret=01b307acba4f54f55aafc33bb06bbbf6) |
| 15 | `158.220.115.52` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=158.220.115.52&port=443&secret=ee70a7cdefd71ce8402a97d26a8115b23c636c6f7564666c6172652e636f6d) |
| 16 | `31.130.151.16` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=31.130.151.16&port=443&secret=4931e9e6000537266a0de4dbb81f81fa) |
| 17 | `rkn.tg` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rkn.tg&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 18 | `142.54.189.109` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=142.54.189.109&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 19 | `107.150.34.101` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=107.150.34.101&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 20 | `prxygo.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=prxygo.shop&port=443&secret=48181acd22b3edaebc8a447868a7dfcb) |


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
