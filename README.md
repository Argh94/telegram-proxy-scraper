# 📊 نتایج استخراج: (آخرین بروزرسانی: 01:16 02-02-1405)

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License" />
  <img src="https://img.shields.io/badge/python-3.9-blue" alt="Python 3.9" />
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
| 1 | `95.217.28.246` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.217.28.246&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `193.25.216.19` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=193.25.216.19&port=443&secret=ee79612e7275ed3a9baef550b4583f00) |
| 3 | `paitakht.arasto.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=paitakht.arasto.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 4 | `2.26.101.98` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.26.101.98&port=443&secret=ee79612e72759919d926b370909e148e) |
| 5 | `proxy.datamtdatafemida.club` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.datamtdatafemida.club&port=443&secret=ee353f27c43bad4054b23f2837b80c87277777772e676f6f676c652e636f6d) |
| 6 | `92.118.234.215` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=92.118.234.215&port=443&secret=dddb9b51b5ce9a2820ff62d348cb23f1b9) |
| 7 | `91.107.189.181` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.189.181&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `mtproxy.neverspy.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtproxy.neverspy.online&port=443&secret=dde8653d2faf392a302d829d79537abbe7) |
| 9 | `71a3067ecd02.sn.mynetname.net` | `7997` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=71a3067ecd02.sn.mynetname.net&port=7997&secret=ee4c670831e7ee84c7c3a287a2184181d8626979736b32322e7275) |
| 10 | `31.220.73.75` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=31.220.73.75&port=443&secret=ee15561483d7091829be01a81a8b550ea4636c6f7564666c6172652e636f6d) |
| 11 | `142.54.189.107` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=142.54.189.107&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 12 | `tee.mobemouy.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tee.mobemouy.com&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 13 | `6161627.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=6161627.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 14 | `142.54.189.106` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=142.54.189.106&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 15 | `46.62.219.0` | `4367` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.62.219.0&port=4367&secret=ee104462821249bd7ac519130220c25d096d61696c2e7275) |
| 16 | `tg.caxero.ru` | `6767` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.caxero.ru&port=6767&secret=fffc0efade691faeaccb0ee0cdbf1773) |
| 17 | `142.54.189.110` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=142.54.189.110&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 18 | `proxy.proxymtproto.net` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.proxymtproto.net&port=443&secret=dd97caa3c6888366f26b12f994f02ecf1a) |
| 19 | `27289292.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=27289292.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 20 | `proxyg.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxyg.site&port=443&secret=eed68360458af63073bac1394e8c7a48da70726f7879672e73697465) |


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
