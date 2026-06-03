# 📊 نتایج استخراج: (آخرین بروزرسانی: 02:30 14-03-1405)

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
| 2 | `mc-ssh.t-proxyru.info.` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mc-ssh.t-proxyru.info.&port=25565&secret=ee104462821249bd7ac519130220c25d0963646e2e79656b74616e65742e636f6d) |
| 4 | `37.27.192.211` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=37.27.192.211&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `62.238.32.249` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.238.32.249&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `195.254.165.25` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.25&port=8443&secret=ee1603010200010001fc030386e24c3add646565707365656B2E636F6D) |
| 7 | `95.216.191.201` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.216.191.201&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `136.243.107.193` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=136.243.107.193&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `87.248.129.53` | `15` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.53&port=15&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 10 | `87.248.129.246` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.246&port=8443&secret=dd79e344818749bd7ac519130220c25d09) |
| 11 | `95.216.191.201` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.216.191.201&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 12 | `87.248.129.212` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.212&port=25565&secret=79e344818749bd7ac519130220c25d0979e344818749bd7ac519130220c25d0979e344818749bd7ac519130220c25d0979e344818749bd7ac519130220c25d09) |
| 13 | `46.225.248.130` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.225.248.130&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `158.160.232.183` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=158.160.232.183&port=443&secret=eefab80a27431eaf7ddafa501cc79b4531617669746f2e7275) |
| 16 | `87.248.129.200` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.200&port=4455&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 17 | `167.233.25.36` | `7443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.233.25.36&port=7443&secret=ee1603010200010001fc030386e24c3add646e2e79656b74616e65742e636f6d646c2e676f6f676c652e636f6d666172616B61762E636F6D160301020001000100000000000000000000000000000000) |
| 19 | `norm.quickdl.info` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=norm.quickdl.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 20 | `161.97.167.251` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=161.97.167.251&port=443&secret=eec14b841016ce9b05f48e9ed7f2d9de9e676f6f676c65617069732e636f6d) |


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
