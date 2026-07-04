# 📊 نتایج استخراج: (آخرین بروزرسانی: 01:19 14-04-1405)

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
| 1 | `secure.gorbushkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=secure.gorbushkin.click&port=443&secret=eeb45561860b2de5d002ab0a9a23481b2c7365637572652e676f72627573686b696e2e636c69636b) |
| 2 | `87.248.129.49` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.49&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 3 | `mizanesgh.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mizanesgh.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 5 | `room.talebi.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=room.talebi.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 6 | `887881z367752876777.ir.fulldf.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=887881z367752876777.ir.fulldf.info&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 8 | `api.medhata.org` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=api.medhata.org&port=443&secret=eef93ad4b307071b377519e77642bc4dbe6170692e6d6564686174612e6f7267) |
| 9 | `mazo-ir.masnavi.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mazo-ir.masnavi.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 10 | `194.77.70.85` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.77.70.85&port=8080&secret=1603010200010001fc030386e24c3add) |
| 11 | `kala.golgoli1.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kala.golgoli1.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add7777772e7961686f6f2e636f6d) |
| 12 | `194.77.70.84` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.77.70.84&port=8080&secret=1603010200010001fc030386e24c3add) |
| 13 | `goodman.lamari.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=goodman.lamari.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 15 | `207pana.denatara.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=207pana.denatara.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 16 | `8f3d1c4e-a9b2-475c-8e1f-2d6a9b4c7e3f.casa` | `80` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=8f3d1c4e-a9b2-475c-8e1f-2d6a9b4c7e3f.casa&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d) |
| 17 | `mmd.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mmd.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `8f911859.etherealvpn.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=8f911859.etherealvpn.uk&port=443&secret=eee2c4f26e0246dea5eb84f95c325ea46062343233353730312e657468657265616c76706e2e756b) |
| 19 | `dena-plus-auto.denatara.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dena-plus-auto.denatara.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 20 | `Www.karako.co.uk` | `600` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Www.karako.co.uk&port=600&secret=ee1603010200010001fc030386e24c3add626973636F7474692E79656B74616E65742E636F6D) |


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
