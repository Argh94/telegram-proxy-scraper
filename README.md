# 📊 نتایج استخراج: (آخرین بروزرسانی: 01:50 23-03-1405)

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
| 1 | `87.248.129.218` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.218&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 5 | `fast.proxytelega.store` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fast.proxytelega.store&port=8443&secret=ee3d75d4605342be40f01e37f606946e81666173742e70726f787974656c6567612e73746f7265) |
| 6 | `link.nowabst.net` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=link.nowabst.net&port=853&secret=ee1bbdcdcfd200974bb999813180a127386164732e78352e7275) |
| 7 | `49.12.113.123` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=49.12.113.123&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `googel.alo-otp.info.` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=googel.alo-otp.info.&port=25565&secret=ee104462821249bd7ac519130220c25d0963646e2e79656b74616e65742e636f6d) |
| 10 | `172.65.100.05` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.65.100.05&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 11 | `view.proxytg.live` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=view.proxytg.live&port=443&secret=ee3624bb4d06c88a513638a3d32327277e766965772e70726f787974672e6c697665) |
| 12 | `172.65.104.042` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.65.104.042&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 13 | `b8rta.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=b8rta.co.uk.&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 14 | `87.248.129.217` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.217&port=443&secret=eea44ea5e1b8331727a895b81e8c43c59e7777772e617276616e636c6f75642e6972) |
| 15 | `flux.proxytop.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=flux.proxytop.space&port=443&secret=ee939c94e58cb9ac7dec74ae86d8461089666c75782e70726f7879746f702e7370616365) |
| 16 | `212.56.44.184` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=212.56.44.184&port=443&secret=ee79ba93b4e649ba70dcd191e72539c99e676f6f676c65617069732e636f6d) |
| 17 | `lk.proxytg.live` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lk.proxytg.live&port=443&secret=eea33a0973394ea248c4f402ae6745b17b6c6b2e70726f787974672e6c697665) |
| 19 | `87.248.129.99` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.99&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 20 | `87.248.129.47` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.47&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |


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
