# 📊 نتایج استخراج: (آخرین بروزرسانی: 22:40 24-03-1405)

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
| 1 | `core.proxyvpn.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=core.proxyvpn.site&port=443&secret=eeeaedcd5747e28104b7a1cbc25cf37ec1636f72652e70726f787976706e2e73697465) |
| 2 | `echo.proxym.world` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=echo.proxym.world&port=443&secret=ee03856fdd3a0b54784892677df90144a06563686f2e70726f78796d2e776f726c64) |
| 3 | `194.213.118.98` | `1010` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.213.118.98&port=1010&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 5 | `vpn.prxtoday.store` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vpn.prxtoday.store&port=443&secret=ee29260362b2497c092e631593a534e5a376706e2e707278746f6461792e73746f7265) |
| 6 | `flux.proxym.world` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=flux.proxym.world&port=443&secret=ee9f447c337d66b416b8e4f81a27e8e344666c75782e70726f78796d2e776f726c64) |
| 7 | `87.248.129.219` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.219&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 9 | `87.248.129.235` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.235&port=4455&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 10 | `91.107.160.196` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.160.196&port=443&secret=104462821249bd7ac519130220c25d09) |
| 11 | `digi.technom.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=digi.technom.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 12 | `176.65.138.99` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=176.65.138.99&port=8443&secret=ee1603010200010001fc030386e24c3add646565707365656B2E636F6D) |
| 14 | `play.proxyvpn.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=play.proxyvpn.site&port=443&secret=ee4d0c82ca73f261e6933ec36e5d902ff6706c61792e70726f787976706e2e73697465) |
| 15 | `proxy18.arixo.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy18.arixo.shop&port=443&secret=ee819b4efa2397a9470682aae92babee31617669746f2e7275) |
| 16 | `sync.proxyvpn.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sync.proxyvpn.site&port=443&secret=eeb9c7994a075883f404453b50e306f9cf73796e632e70726f787976706e2e73697465) |
| 17 | `176.65.138.97` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=176.65.138.97&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 18 | `172.65.100.05` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.65.100.05&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 19 | `31.41.33.114` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=31.41.33.114&port=443&secret=eee854b22396ba5a74f23b6f126108294a6972616e2e6d69642e7275) |
| 20 | `87.248.129.196` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.196&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |


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
