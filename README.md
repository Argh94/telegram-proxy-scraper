# 📊 نتایج استخراج: (آخرین بروزرسانی: 19:22 10-05-1405)

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
| 1 | `ma.hastim.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ma.hastim.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 2 | `a.red-eyes.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=a.red-eyes.co.uk&port=443&secret=ee3d452ace1dc3eba3f6064fe8291dfd59626973636f7474692e79656b74616e65742e636f6d) |
| 4 | `94.130.190.150` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=94.130.190.150&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `13376.ir.meli-n13.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=13376.ir.meli-n13.info&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 6 | `app.librava.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=app.librava.click&port=443&secret=eea1eceac9a9088b02d582d0ca99d9365e6170702e6c6962726176612e636c69636b) |
| 7 | `46.225.26.227` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.225.26.227&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `79.137.196.223` | `10443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.137.196.223&port=10443&secret=ee63fccdeb9951e5f99d66d274148278b97777772e636c6f7564666c6172652e636f6d) |
| 9 | `syzygy.sosun4ik.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=syzygy.sosun4ik.top&port=443&secret=ee6a0333c1db3f8eaba5c76731a44203b6617669746f2e7275) |
| 10 | `ad5.arixo.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ad5.arixo.shop&port=443&secret=ee995469d4d5a3221f69a1cc24d1cafa506164322e617269786f2e73686f70) |
| 11 | `cdn.savelyev.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cdn.savelyev.click&port=443&secret=ee2d9508afda3c91ec2ce75e2e0916437c63646e2e736176656c7965762e636c69636b) |
| 12 | `zon-b0z.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zon-b0z.co.uk.&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 13 | `did-domak.ir.hadihoda.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=did-domak.ir.hadihoda.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e69626973636f7474692e79656b74616e65742e636f6d) |
| 14 | `a.red-eyes.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=a.red-eyes.co.uk&port=443&secret=ee3d452ace1dc3eba3f6064fe8291dfd59612e7265642d657965732e636f2e756b) |
| 16 | `65.109.254.50` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.254.50&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 17 | `blue.golgoli2.co.uk` | `2096` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=blue.golgoli2.co.uk&port=2096&secret=ee1603010200010001fc030386e24c3add7777772e7961686f6f2e636f6d) |
| 18 | `br8ta.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=br8ta.co.uk.&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 19 | `webhook.vingardium.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=webhook.vingardium.co.uk.&port=443&secret=eeddffffffc5a1168b2ff3eba31cbfffff7765622e62616c652e6169) |
| 20 | `opeenhostings.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=opeenhostings.co.uk.&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |


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
