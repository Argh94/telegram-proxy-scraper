# 📊 نتایج استخراج: (آخرین بروزرسانی: 22:48 12-05-1405)

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

این اسکریپت با استفاده از `requests` برای منابع متنی و کانال‌های تلگرام، پروکسی‌های MTProto را جمع‌آوری می‌کند. پروکسی‌های تکراری حذف شده و نتایج در فایل `proxy.txt` ذخیره می‌شوند. این فرآیند به‌صورت خودکار با **GitHub Actions** هر 3 ساعت اجرا می‌شود.

## 🚀 ویژگی‌ها
- 🌐 جمع‌آوری پروکسی از منابع متنی و کانال‌های تلگرام
- 🔄 به‌روزرسانی خودکار هر 3 ساعت
- 🗑 حذف پروکسی‌های تکراری
- 🔑 بدون نیاز به API تلگرام
- 📱 مناسب برای کاربران در جستجوی پروکسی‌های فعال MTProto

## 📋 پیش‌نیازها
- 🐍 پایتون 3.9
- 📦 کتابخانه‌های مورد نیاز: `requests`, `beautifulsoup4`, `pytz`, `jdatetime`
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
| 1 | `ad4.arixo.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ad4.arixo.shop&port=443&secret=eec699329f2f8c2d33cd1e1a9f10e5d32d6164312e617269786f2e73686f70) |
| 2 | `live.gorbushkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=live.gorbushkin.click&port=443&secret=eec85666282a2a3091eb56c31302da3c9f6c6976652e676f72627573686b696e2e636c69636b) |
| 3 | `cross-over.lamari.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cross-over.lamari.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 4 | `app.librava.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=app.librava.click&port=443&secret=eea1eceac9a9088b02d582d0ca99d9365e6170702e6c6962726176612e636c69636b) |
| 5 | `logs.jinxandjack.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=logs.jinxandjack.co.uk.&port=443&secret=eeddffffffc5a1168b2ff3eba31cbfffff7765622e62616c652e6169) |
| 8 | `164.90.162.103` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=164.90.162.103&port=443&secret=eeb4dd220363231daa02b2e5c56de2c3b7636c6f7564666c6172652e636f6d) |
| 9 | `94.130.190.150` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=94.130.190.150&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `most.karshenasi.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=most.karshenasi.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 11 | `ad5.arixo.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ad5.arixo.shop&port=443&secret=ee995469d4d5a3221f69a1cc24d1cafa506164322e617269786f2e73686f70) |
| 12 | `ad4.arixo.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ad4.arixo.shop&port=443&secret=eec699329f2f8c2d33cd1e1a9f10e5d32d6164312e617269786f2e73686f70) |
| 14 | `book.malavanann.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=book.malavanann.co.uk&port=2096&secret=ee1603010200010001fc030386e24c3add7777772e7961686f6f2e636f6d) |
| 15 | `net.antitspu.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=net.antitspu.com&port=443&secret=ee24918e3782cee00f652c0018f2867ffd6e65742e616e7469747370752e636f6d) |
| 16 | `FOR-IRAN.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=FOR-IRAN.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `molfix.range-abia.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=molfix.range-abia.ir&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 18 | `195.201.249.19` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.201.249.19&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 19 | `a.red-eyes.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=a.red-eyes.co.uk&port=443&secret=ee3d452ace1dc3eba3f6064fe8291dfd59626973636f7474692e79656b74616e65742e636f6d) |
| 20 | `portal.balalaika.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=portal.balalaika.click&port=443&secret=ee3c7b046d6a7b00b2c910cd755314eb2e706f7274616c2e62616c616c61696b612e636c69636b) |


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
