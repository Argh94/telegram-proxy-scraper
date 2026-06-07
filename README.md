# 📊 نتایج استخراج: (آخرین بروزرسانی: 01:29 18-03-1405)

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
| 1 | `37.27.192.211` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=37.27.192.211&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 3 | `167.233.73.69` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.233.73.69&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 4 | `136.243.107.193` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=136.243.107.193&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `167.233.53.71` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.233.53.71&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `proxy.speedbreaker.info` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.speedbreaker.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 7 | `rocket.flowaccess.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rocket.flowaccess.site&port=443&secret=ee03d3d1b9bda832390669bc06167720d8726f636b65742e666c6f776163636573732e73697465) |
| 10 | `www.merco-karco.website` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.merco-karco.website&port=443&secret=ee1603010200010001fc030386e24c3add626973636F7474692E79656B74616E65742E636F6D) |
| 12 | `87.248.129.13` | `15` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.13&port=15&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d) |
| 13 | `178.105.226.11` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.105.226.11&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `167.233.51.33` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.233.51.33&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `95.216.195.146` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.216.195.146&port=443&secret=ee04901ee18641067c6df1e28cccbbb01f636c6f7564666c6172652e636f6d) |
| 17 | `87.248.129.223` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.223&port=4455&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 18 | `vortex.flowstreamhub.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vortex.flowstreamhub.site&port=443&secret=eeafcde96fcec1b95dd190a95814b0f026766f727465782e666c6f7773747265616d6875622e73697465) |
| 19 | `167.233.65.204` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.233.65.204&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `87.248.129.101` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.101&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |


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
