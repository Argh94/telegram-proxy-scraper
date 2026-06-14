# 📊 نتایج استخراج: (آخرین بروزرسانی: 10:47 24-03-1405)

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
| 1 | `65.21.113.80` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.21.113.80&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `iran.protocolsix.info.` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=iran.protocolsix.info.&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 3 | `Dade.mizbanonline.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Dade.mizbanonline.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 4 | `bolt.proxyonline.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bolt.proxyonline.online&port=443&secret=ee98741a4df96ee86a25ca542a538a3484626f6c742e70726f78796f6e6c696e652e6f6e6c696e65) |
| 5 | `b8rta.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=b8rta.co.uk.&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 6 | `apex.proxym.world` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=apex.proxym.world&port=443&secret=ee4459d77ba2b570d1a593a478d3cd94a4617065782e70726f78796d2e776f726c64) |
| 7 | `googel.alo-otp.info.` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=googel.alo-otp.info.&port=25565&secret=ee104462821249bd7ac519130220c25d0963646e2e79656b74616e65742e636f6d) |
| 8 | `storm.proxytelega.store` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=storm.proxytelega.store&port=443&secret=eedef3ae42d41ca0570cd030dea03fa6b373746f726d2e70726f787974656c6567612e73746f7265) |
| 9 | `87.248.129.131` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.131&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 11 | `87.248.129.130` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.130&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 12 | `fotbali.pw-pishi1.ir` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fotbali.pw-pishi1.ir&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `kilo.proxytop.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kilo.proxytop.space&port=443&secret=eeb029e3857037fbaf8616eea4f56124456b696c6f2e70726f7879746f702e7370616365) |
| 14 | `lumen.proxytop.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lumen.proxytop.space&port=443&secret=ee77a9c0a7c576db75ddb379ffc1ea49786c756d656e2e70726f7879746f702e7370616365) |
| 15 | `62.3.12.2` | `8444` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.3.12.2&port=8444&secret=ee6f7a6f6e2e7275f22c5421fa893965) |
| 17 | `fotbali.pw-pishi1.ir` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fotbali.pw-pishi1.ir&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `87.248.129.218` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.218&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 20 | `assets.prx.today` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=assets.prx.today&port=443&secret=ee595ef26a3a0072f97dadb2be7007dbac6173736574732e7072782e746f646179) |


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
