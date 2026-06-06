# 📊 نتایج استخراج: (آخرین بروزرسانی: 14:21 16-03-1405)

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
| 1 | `167.233.52.240` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.233.52.240&port=443&secret=ddd77db43ee3721f0fcb40a4ff63b5cd27) |
| 2 | `172.65.104.042` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.65.104.042&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 5 | `91.107.246.35` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.246.35&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `ghtash.co.uk` | `9965` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ghtash.co.uk&port=9965&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `65.109.245.52` | `7980` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.245.52&port=7980&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 10 | `65.109.254.108` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.254.108&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 11 | `3.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3.telbet.lol&port=25565&secret=dd79e7010200010007f0030386e24c3add) |
| 12 | `94.130.163.60` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=94.130.163.60&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `vortex.flowstreamhub.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vortex.flowstreamhub.site&port=443&secret=eeafcde96fcec1b95dd190a95814b0f026766f727465782e666c6f7773747265616d6875622e73697465) |
| 14 | `78.47.129.193` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=78.47.129.193&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `87.248.129.51` | `15` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.51&port=15&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d) |
| 16 | `rkn.proxytelega.store` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rkn.proxytelega.store&port=8443&secret=eeec48b14805acf33a64f494fe7cf6656a726b6e2e70726f787974656c6567612e73746f7265) |
| 18 | `46.225.254.148` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.225.254.148&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 19 | `flash.quickrouteapp.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=flash.quickrouteapp.xyz&port=443&secret=eec7b876f355b93b6b786cb4b6c9daee79666c6173682e717569636b726f7574656170702e78797a) |
| 20 | `light.nolags.pw` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=light.nolags.pw&port=443&secret=dd84b5a5dbe775244bd0b061c72f4e4c73) |


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
