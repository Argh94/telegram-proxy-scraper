# 📊 نتایج استخراج: (آخرین بروزرسانی: 10:29 15-03-1405)

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
| 1 | `91.107.240.187` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.240.187&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `161.97.169.231` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=161.97.169.231&port=443&secret=eecfcd09956992b6d4dd0bf6aa2a8f63cd676f6f676c65617069732e636f6d) |
| 3 | `wave.flowaccess.site` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=wave.flowaccess.site&port=8443&secret=eeea2f80ea6628006a3db2a8678d65bd07776176652e666c6f776163636573732e73697465) |
| 4 | `167.233.25.36` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.233.25.36&port=7443&secret=ee1603010200010001fc030386e24c3add646e2e79656b74616e65742e636f6d646c2e676f6f676c652e636f6d666172616B61762E636F6D160301020001000100000000000000000000000000000000) |
| 5 | `surf.flowaccess.site` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=surf.flowaccess.site&port=8443&secret=eeea26c2508652bcbd35ac3116045eb939737572662e666c6f776163636573732e73697465) |
| 6 | `195.254.165.18` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.18&port=8443&secret=ee1603010200010001fc030386e24c3add646565707365656B2E636F6D) |
| 8 | `turbovpn.obhod.fun` | `9443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=turbovpn.obhod.fun&port=9443&secret=76706e76706e76706e76706e76706e76) |
| 9 | `info.proxytime.info` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=info.proxytime.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 10 | `91.107.254.122` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.254.122&port=443&secret=ddd451f808fd60ed2c45f11d38fdbc87c5) |
| 12 | `91.217.166.13` | `16` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.217.166.13&port=16&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d) |
| 13 | `136.243.107.193` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=136.243.107.193&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 14 | `play.fast-mt.info` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=play.fast-mt.info&port=22&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 15 | `boost.flowstreamhub.site` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=boost.flowstreamhub.site&port=8443&secret=ee7ee0a641b78ecc8d210e47981904a50a626f6f73742e666c6f7773747265616d6875622e73697465) |
| 16 | `167.233.25.36` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.233.25.36&port=7443&secret=ee1603010200010001fc030386e24c3add646e2e79656b74616e65742e636f6d646c2e676f6f676c652e636f6d666172616B61762E636F6D160301020001000100000000000000000000000000000000) |
| 17 | `195.254.165.2` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.2&port=8443&secret=dd79e344818749bd7ac519130220c25d09) |
| 18 | `form.quickdl.info` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=form.quickdl.info&port=22&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 19 | `167.233.49.234` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.233.49.234&port=443&secret=ddd77db43ee3721f0fcb40a4ff63b5cd27) |


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
