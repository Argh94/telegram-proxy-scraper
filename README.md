# 📊 نتایج استخراج: (آخرین بروزرسانی: 05:40 11-04-1405)

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
| 1 | `Best.for.iran.zydgjdinc.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Best.for.iran.zydgjdinc.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e697374617469632e666172616b61762e636f6d) |
| 2 | `157.180.119.226` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=157.180.119.226&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `167.233.179.218` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.233.179.218&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `h.hajagha.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=h.hajagha.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 6 | `app.kvakzon.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=app.kvakzon.top&port=443&secret=ee5b0fbf6320bd9abf4c494f0a5e5d36a16170702e6b76616b7a6f6e2e746f70) |
| 7 | `kala.golgoli1.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kala.golgoli1.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add7777772e7961686f6f2e636f6d) |
| 9 | `best-sellerst.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=best-sellerst.co.uk.&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 10 | `87.229.56.183` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.229.56.183&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 11 | `permiiium.lavazemi2.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=permiiium.lavazemi2.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add7777772e7961686f6f2e636f6d) |
| 12 | `gate.soluqent.pro` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gate.soluqent.pro&port=443&secret=eed66f4a5efedfdb0b2a74cf0596b12d17676174652e736f6c7571656e742e70726f) |
| 13 | `top.jamejanhani2.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=top.jamejanhani2.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 14 | `pl.nowabst.net` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pl.nowabst.net&port=853&secret=ee82ce1f84af4033cc7e7b021069be3d5b766b2e636f6d) |
| 15 | `aghaye.aseman.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=aghaye.aseman.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 16 | `87.248.129.16` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.16&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 17 | `hetzner.bkontek.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hetzner.bkontek.co.uk.&port=443&secret=eeddffffffc5a1168b2ff3eba31cbfffff6865747a6e65722e636f6d) |
| 18 | `collider.web-yektanet-com.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=collider.web-yektanet-com.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636F7474692E79656B74616E65742E636F6D) |
| 19 | `5.75.172.150` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.75.172.150&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `book.malavanann.co.uk` | `2053` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=book.malavanann.co.uk&port=2053&secret=ee1603010200010001fc030386e24c3add706c61792e676f6f676c652e636f6d) |


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
