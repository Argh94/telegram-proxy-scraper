# 📊 نتایج استخراج: (آخرین بروزرسانی: 23:23 22-03-1405)

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
| 1 | `194.213.118.59` | `1010` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.213.118.59&port=1010&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 2 | `87.248.129.105` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.105&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 3 | `b8rta.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=b8rta.co.uk.&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 4 | `fotbali.pw-pishi1.ir` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fotbali.pw-pishi1.ir&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `jet.proxyux.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=jet.proxyux.site&port=443&secret=eed2024b83c7a14889f7d69bd82ca087c16a65742e70726f787975782e73697465) |
| 6 | `iranian-cheetah.ir.the-nice-mtproto.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=iranian-cheetah.ir.the-nice-mtproto.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 8 | `fotbali.pw-pishi1.ir` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fotbali.pw-pishi1.ir&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 9 | `iranian-cheetah.ir.the-nice-mtproto.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=iranian-cheetah.ir.the-nice-mtproto.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 10 | `mt.nowabst.net` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.nowabst.net&port=853&secret=ee12893ffd2044cecd31104edc02a7e5586164732e78352e7275) |
| 11 | `surge.linkflowhub.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=surge.linkflowhub.shop&port=443&secret=ee932f87d141afddf9a957c5e3c85d8bb673757267652e6c696e6b666c6f776875622e73686f70) |
| 13 | `91.107.254.122` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.254.122&port=443&secret=ddd451f808fd60ed2c45f11d38fdbc87c5) |
| 14 | `flux.proxyux.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=flux.proxyux.site&port=443&secret=ee0a7ecff0ebda97b34dc84157b8cbfad3666c75782e70726f787975782e73697465) |
| 17 | `apex.proxytop.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=apex.proxytop.space&port=443&secret=ee05d3d7463edfb7a674cc1d89ba24eeba617065782e70726f7879746f702e7370616365) |
| 18 | `flux.proxytop.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=flux.proxytop.space&port=443&secret=ee939c94e58cb9ac7dec74ae86d8461089666c75782e70726f7879746f702e7370616365) |
| 19 | `lumen.proxyux.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lumen.proxyux.site&port=443&secret=ee46a405cdf38698927aa7352341e2ba0a6c756d656e2e70726f787975782e73697465) |
| 20 | `bekhan-mara.info.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bekhan-mara.info.&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |


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
