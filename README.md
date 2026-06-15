# 📊 نتایج استخراج: (آخرین بروزرسانی: 22:32 25-03-1405)

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
| 1 | `ams1.tlgfast.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ams1.tlgfast.com&port=443&secret=083fe0c452e2407d835537872f097c54) |
| 2 | `fresh.t-proxy.info.` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fresh.t-proxy.info.&port=25565&secret=ee104462821249bd7ac519130220c25d0963646e2e79656b74616e65742e636f6d) |
| 3 | `87.248.129.106` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.106&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 4 | `api.prxtoday.store` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=api.prxtoday.store&port=443&secret=ee1fed31d4c3ce8255aedc8c4c14a36f536170692e707278746f6461792e73746f7265) |
| 5 | `Geng.etherealvpn.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Geng.etherealvpn.uk&port=443&secret=eefd6c10517940b3ad79ce5e3d40c9972e617669746f2e7275) |
| 6 | `core.proxyvpn.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=core.proxyvpn.site&port=443&secret=eeeaedcd5747e28104b7a1cbc25cf37ec1636f72652e70726f787976706e2e73697465) |
| 7 | `For.dear-iranian-people.com.heazshddd.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=For.dear-iranian-people.com.heazshddd.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 8 | `panel-portal.managep.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=panel-portal.managep.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 9 | `irancell-mci.ir.gybshdjls.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=irancell-mci.ir.gybshdjls.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 10 | `get.proxyz.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=get.proxyz.site&port=443&secret=ee8bfeb37ebe59a0f6aed1ccae9b9981566765742e70726f78797a2e73697465) |
| 11 | `digi.technom.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=digi.technom.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 12 | `static.prxtoday.store` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=static.prxtoday.store&port=443&secret=ee3740849efd941157c45810d974fd66097374617469632e707278746f6461792e73746f7265) |
| 13 | `app.prxtoday.store` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=app.prxtoday.store&port=443&secret=ee1ee902d3b8cc7c7f1691838d544efee96170702e707278746f6461792e73746f7265) |
| 14 | `googel.alo-otp.info.` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=googel.alo-otp.info.&port=25565&secret=ee104462821249bd7ac519130220c25d0963646e2e79656b74616e65742e636f6d) |
| 15 | `87.248.129.190` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.190&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 16 | `subobdoa.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=subobdoa.co.uk.&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 17 | `mahanmizban.genuismind.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mahanmizban.genuismind.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 18 | `apex.proxym.world` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=apex.proxym.world&port=443&secret=ee4459d77ba2b570d1a593a478d3cd94a4617065782e70726f78796d2e776f726c64) |
| 19 | `65.21.113.80` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.21.113.80&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `dl.prx.today` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dl.prx.today&port=443&secret=ee9b9483de201ca0a074d391d3c4b63152646c2e7072782e746f646179) |


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
