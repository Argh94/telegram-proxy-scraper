# 📊 نتایج استخراج: (آخرین بروزرسانی: 09:52 06-04-1405)

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
| 1 | `62.3.12.2` | `8444` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.3.12.2&port=8444&secret=ee6f7a6f6e2e7275f22c5421fa893965) |
| 2 | `sv4.hajhossein.observer` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sv4.hajhossein.observer&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 3 | `87.248.129.133` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.133&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 4 | `95.217.163.166` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.217.163.166&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `79.137.196.223` | `1443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.137.196.223&port=1443&secret=eeee52288a1c9bf20ef3423488f8418c3f087777772e636c6f7564666c6172652e636f6d) |
| 7 | `cloud.ir.asiatech-bestserver.technom.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cloud.ir.asiatech-bestserver.technom.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 8 | `79.133.126.125` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.133.126.125&port=443&secret=dd890938bf53a1dab0a211a217a9260763) |
| 10 | `87.248.144.21` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.144.21&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 12 | `For.dear-iranian-people.com.heazshddd.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=For.dear-iranian-people.com.heazshddd.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 13 | `hub.nowabst.net` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hub.nowabst.net&port=853&secret=ee55aabc9752a9d9d379e02943cf8117956164732e78352e7275) |
| 14 | `ad2.arixo.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ad2.arixo.shop&port=443&secret=eed09b88cbbd4e744865b890e5a0bd26876164322e617269786f2e73686f70) |
| 15 | `87.229.56.180` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.229.56.180&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 16 | `link.nowabst.net` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=link.nowabst.net&port=853&secret=ee1bbdcdcfd200974bb999813180a127386164732e78352e7275) |
| 17 | `so-cpu.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=so-cpu.co.uk.&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 19 | `87.248.129.49` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.49&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 20 | `3.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3.telbet.lol&port=25565&secret=dd79e7010200010007f0030386e24c3add) |


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
