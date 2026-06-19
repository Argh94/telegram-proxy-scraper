# 📊 نتایج استخراج: (آخرین بروزرسانی: 06:25 29-03-1405)

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
| 1 | `New-Empire-On-World.ir.heazshddd.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=New-Empire-On-World.ir.heazshddd.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 2 | `br.kingproxynewdomailasiatech.ink` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=br.kingproxynewdomailasiatech.ink&port=22&secret=dd79e7010200010007f0030386e24c3add) |
| 3 | `87.248.129.202` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.202&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 4 | `cdn.toconvel.digital` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cdn.toconvel.digital&port=443&secret=eeddeeeeb0dda28d2a517ff1c71036f2c663646e2e746f636f6e76656c2e6469676974616c) |
| 5 | `87.229.56.249` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.229.56.249&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 6 | `link.mishkalapy.life` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=link.mishkalapy.life&port=443&secret=ee6d9ff342ecb0e149a6269f67d9383af26c696e6b2e6d6973686b616c6170792e6c696665) |
| 7 | `Iran.mother.ir.jetish.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Iran.mother.ir.jetish.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 9 | `gate.soluqent.pro` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gate.soluqent.pro&port=443&secret=ee6538b62fe47dff3c068ed861df1f0465676174652e736f6c7571656e742e70726f) |
| 10 | `junior.ir.the-nice-mtproto.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=junior.ir.the-nice-mtproto.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 12 | `87.248.129.101` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.101&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 13 | `edge.rknwatch.digital` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=edge.rknwatch.digital&port=443&secret=ee9e8767a28148936ae7e50eb9b0689a49656467652e726b6e77617463682e6469676974616c) |
| 14 | `football.world-pro.co.uk` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=football.world-pro.co.uk&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 16 | `cheetah-proxy.ir.hey-gardash.info.` | `1080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cheetah-proxy.ir.hey-gardash.info.&port=1080&secret=79e344818749bd7ac519130220c25d09) |
| 17 | `91.107.254.122` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.254.122&port=443&secret=ddd451f808fd60ed2c45f11d38fdbc87c5) |
| 19 | `87.229.56.6` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.229.56.6&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 20 | `87.248.129.197` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.197&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |


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
