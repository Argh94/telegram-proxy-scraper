# 📊 نتایج استخراج: (آخرین بروزرسانی: 10:43 22-03-1405)

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
| 2 | `ge.nowabst.net` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ge.nowabst.net&port=853&secret=eefdf6175e50069c01bd22d786534aa2b26164732e78352e7275) |
| 3 | `ai.kerfilia.info` | `6775` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ai.kerfilia.info&port=6775&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |
| 4 | `apex.proxyux.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=apex.proxyux.site&port=443&secret=ee1e16392ec634c2ebce9387a9edcf24e3617065782e70726f787975782e73697465) |
| 5 | `135.181.69.129` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=135.181.69.129&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `gw.nowabst.net` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gw.nowabst.net&port=853&secret=ee6104d5fd936c4930978f0227166deaa96164732e78352e7275) |
| 7 | `172.65.104.042` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.65.104.042&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 8 | `the-nice-future.info.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=the-nice-future.info.&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 9 | `212.56.44.174` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=212.56.44.174&port=443&secret=ee79ba93b4e649ba70dcd191e72539c99e676f6f676c65617069732e636f6d) |
| 10 | `fast.proxytelega.store` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fast.proxytelega.store&port=8443&secret=ee3d75d4605342be40f01e37f606946e81666173742e70726f787974656c6567612e73746f7265) |
| 15 | `87.248.129.105` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.105&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 16 | `87.248.129.235` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.235&port=4455&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 18 | `tg.nowabst.net` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.nowabst.net&port=853&secret=eebfbfb8093b088269716ea5262d483e1d6164732e78352e7275) |
| 19 | `track.proxytg.live` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=track.proxytg.live&port=443&secret=ee8e4bd7b2a034418fd924aeed3c97cd7b747261636b2e70726f787974672e6c697665) |
| 20 | `jet.proxytop.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jet.proxytop.space&port=443&secret=ee08a1d5ae74a7f39b214722c152b1eef46a65742e70726f7879746f702e7370616365) |


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
