# 📊 نتایج استخراج: (آخرین بروزرسانی: 16:58 24-03-1405)

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
| 1 | `31.41.33.114` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=31.41.33.114&port=443&secret=eee854b22396ba5a74f23b6f126108294a6972616e2e6d69642e7275) |
| 2 | `flux.proxytelega.store` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=flux.proxytelega.store&port=443&secret=eec57f379567b25a79cbd1fa0ad73b98d9666c75782e70726f787974656c6567612e73746f7265) |
| 3 | `Kingdom-persia.ir.hey-gardash.info.` | `1080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Kingdom-persia.ir.hey-gardash.info.&port=1080&secret=79e344818749bd7ac519130220c25d09) |
| 4 | `drift.proxyonline.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=drift.proxyonline.online&port=443&secret=eeacd41b6bbfa3b3f3d50a25511430857464726966742e70726f78796f6e6c696e652e6f6e6c696e65) |
| 5 | `87.248.129.219` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.219&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 6 | `drift.proxyonline.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=drift.proxyonline.online&port=443&secret=eeacd41b6bbfa3b3f3d50a25511430857464726966742e70726f78796f6e6c696e652e6f6e6c696e65) |
| 7 | `87.248.129.98` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.98&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 8 | `51.250.85.134` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=51.250.85.134&port=443&secret=eec7b827c1a6a0ad8b441e271442137a86617669746f2e7275) |
| 10 | `pizza.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pizza.telbet.lol&port=25565&secret=dd79e7010200010007f0030386e24c3add) |
| 11 | `194.213.118.98` | `1010` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.213.118.98&port=1010&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 12 | `87.248.129.201` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.201&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 13 | `mc-ssh.t-proxyru.info.` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mc-ssh.t-proxyru.info.&port=25565&secret=ee104462821249bd7ac519130220c25d0963646e2e79656b74616e65742e636f6d) |
| 14 | `194.213.118.28` | `1010` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.213.118.28&port=1010&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 15 | `irancell-mci.ir.gybshdjls.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=irancell-mci.ir.gybshdjls.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 16 | `87.248.129.16` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.16&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 17 | `176.65.138.99` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=176.65.138.99&port=8443&secret=ee1603010200010001fc030386e24c3add646565707365656B2E636F6D) |
| 18 | `flux.proxytop.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=flux.proxytop.space&port=443&secret=ee939c94e58cb9ac7dec74ae86d8461089666c75782e70726f7879746f702e7370616365) |


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
