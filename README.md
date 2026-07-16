# 📊 نتایج استخراج: (آخرین بروزرسانی: 01:27 26-04-1405)

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
| 1 | `s010.neo-trading.org` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s010.neo-trading.org&port=8443&secret=ee2c46ee89b4f2c79c1d8325d13091e580706574726f766963682e7275) |
| 2 | `symbol.simbol.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=symbol.simbol.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 7 | `dullaa55332222.ir.meli-n13.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dullaa55332222.ir.meli-n13.info&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 8 | `65.109.254.91` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.254.91&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `mtp.nowabst.net` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtp.nowabst.net&port=853&secret=eeceaec97c86b6332adc48b3c081954e60766b2e636f6d) |
| 10 | `zilch.chunkycorp.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zilch.chunkycorp.shop&port=443&secret=ee6a0333c1db3f8eaba5c76731a44203b6617669746f2e7275) |
| 11 | `r77roo88001m1.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=r77roo88001m1.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `34.178.220.38` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=34.178.220.38&port=443&secret=dd706dfa5dc42ec06475bee1b28952ecc1) |
| 14 | `116.203.140.198` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=116.203.140.198&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `mt.nowabst.net` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.nowabst.net&port=853&secret=ee4e9fcd5caf6e9be2f8ec43e370e902d6766b2e636f6d) |
| 16 | `go.antitspu.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=go.antitspu.com&port=443&secret=eedec8518ddb0fd2fb190d6e8ede49e581676f2e616e7469747370752e636f6d) |
| 17 | `130.193.39.208` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=130.193.39.208&port=443&secret=ee6a0333c1db3f8eaba5c76731a44203b6617669746f2e7275) |
| 19 | `s4.postpulse.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s4.postpulse.space&port=443&secret=ee4ed06711abba996600b11cd356a7674c6164312e617269786f2e73686f70) |


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
