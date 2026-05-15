# 📊 نتایج استخراج: (آخرین بروزرسانی: 17:37 25-02-1405)

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
| 1 | `195.254.165.251` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.251&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 2 | `185.117.0.248` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.117.0.248&port=443&secret=eed451f808fd60ed2c45f11d38fdbc87c57961686f6f2e636f6d) |
| 3 | `62.238.27.70` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.238.27.70&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `calcium-credit.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=calcium-credit.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 6 | `germany.tgproxysokol.pro` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=germany.tgproxysokol.pro&port=8443&secret=ee4215d16e455242e9b5ffb6349df285d06164732e78352e7275) |
| 8 | `178.104.81.34` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.104.81.34&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `y0u-found-a-way-ou7-of-gorphosts-lockd0wn.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=y0u-found-a-way-ou7-of-gorphosts-lockd0wn.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 10 | `132.243.235.191` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.235.191&port=443&secret=ee62c1113f25b902304012745a2b34649979616e6465782e7275) |
| 11 | `proxy.fluxoria.it.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.fluxoria.it.com&port=443&secret=ee307242dd41275c771f40035565d0750a70726f78792e666c75786f7269612e69742e636f6d) |
| 12 | `132.243.235.194` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.235.194&port=443&secret=eebbef585db7c10242e5b3654910e1d91479616e6465782e7275) |
| 13 | `89.125.113.155` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.125.113.155&port=443&secret=ee67af7b545eb72c3c47fc2ccb74aa41c979616e6465782e7275) |
| 15 | `144.31.221.15` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=144.31.221.15&port=443&secret=b2d53412432435cd7d8e90b4d0821d60) |
| 16 | `mt.corph.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.corph.ru&port=443&secret=ee2ed7517b077ef414e24b106e0729335d6d742e636f7270682e7275) |
| 17 | `138.124.127.154` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=138.124.127.154&port=443&secret=ee0c480abc71136dd1c5dadf918e32cea7766b2e636f6d) |
| 18 | `2.27.41.207` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.27.41.207&port=443&secret=9436fa39ab47ccb34f217ac6d06b4e58) |
| 19 | `mtp.fsoc-app.online` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtp.fsoc-app.online&port=853&secret=ee1d49946a9bd11022149e2c68f1d75f6774656c2e66736f632d6170702e6f6e6c696e65) |
| 20 | `194.120.230.199` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.120.230.199&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |


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
