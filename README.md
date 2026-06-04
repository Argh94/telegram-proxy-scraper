# 📊 نتایج استخراج: (آخرین بروزرسانی: 01:47 15-03-1405)

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
| 1 | `87.248.129.245` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.245&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 2 | `Roo3beh.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Roo3beh.telbet.lol&port=25565&secret=dd79e7010200010007f0030386e24c3add) |
| 4 | `62.238.32.249` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.238.32.249&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `87.248.129.50` | `15` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.50&port=15&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 6 | `195.254.165.25` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.25&port=8443&secret=ee1603010200010001fc030386e24c3add646565707365656B2E636F6D) |
| 7 | `87.248.129.200` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.200&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 9 | `blue.protocolsix.info` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=blue.protocolsix.info&port=22&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 10 | `91.217.166.12` | `16` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.217.166.12&port=16&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d) |
| 11 | `87.248.129.244` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.244&port=4455&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 12 | `87.248.129.132` | `16` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.132&port=16&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d) |
| 13 | `161.97.167.251` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=161.97.167.251&port=443&secret=eec14b841016ce9b05f48e9ed7f2d9de9e676f6f676c65617069732e636f6d) |
| 15 | `jet.quickrouteapp.xyz` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jet.quickrouteapp.xyz&port=8443&secret=eeedca657d767c71c26de484e74182c3076a65742e717569636b726f7574656170702e78797a) |
| 16 | `turbo2proxy.vpnproxy.cc` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=turbo2proxy.vpnproxy.cc&port=8443&secret=ee56af68a36d94c4d47d100196d6a59f1d747572626f3270726f78792e76706e70726f78792e6363) |
| 17 | `wave.flowaccess.site` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=wave.flowaccess.site&port=8443&secret=eeea2f80ea6628006a3db2a8678d65bd07776176652e666c6f776163636573732e73697465) |
| 18 | `info.proxytime.info` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=info.proxytime.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 19 | `87.248.129.247` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.247&port=4455&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 20 | `161.97.169.231` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=161.97.169.231&port=443&secret=eecfcd09956992b6d4dd0bf6aa2a8f63cd676f6f676c65617069732e636f6d) |


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
