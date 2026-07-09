# 📊 نتایج استخراج: (آخرین بروزرسانی: 05:24 18-04-1405)

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
| 2 | `sv4.hajhossein.observer` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sv4.hajhossein.observer&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 3 | `super.sub-ploter.co.uk` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=super.sub-ploter.co.uk&port=25565&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 4 | `mmd.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mmd.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `login.kerfilia.info` | `6775` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=login.kerfilia.info&port=6775&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |
| 6 | `ad2.arixo.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ad2.arixo.shop&port=443&secret=eed09b88cbbd4e744865b890e5a0bd26876164322e617269786f2e73686f70) |
| 8 | `b.sub-ploter.co.uk` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=b.sub-ploter.co.uk&port=22&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 9 | `8f3d1c4e-a9b2-475c-8e1f-2d6a9b4c7e3f.casa` | `80` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=8f3d1c4e-a9b2-475c-8e1f-2d6a9b4c7e3f.casa&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d) |
| 10 | `49.12.117.95` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=49.12.117.95&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 11 | `rudomain.info.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rudomain.info.&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 12 | `cinema-hulk.avangement.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cinema-hulk.avangement.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 13 | `net.pelmeshka.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=net.pelmeshka.top&port=443&secret=eefe12a66db0212791c3ba09df4f6123806e65742e70656c6d6573686b612e746f70) |
| 15 | `web.utkanos.life` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=web.utkanos.life&port=443&secret=ee36fd02bb86fbc4266de3a70114c13a247765622e75746b616e6f732e6c696665) |
| 16 | `gate.klyuch1k.org` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gate.klyuch1k.org&port=443&secret=eeae941a76ec4acf04faabaf8a24571080676174652e6b6c79756368316b2e6f7267) |
| 17 | `swag.caxero.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=swag.caxero.ru&port=443&secret=8f3c7a1d4b92e6c51a7d0fb843c2e91f) |
| 18 | `15.mmd1.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=15.mmd1.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 19 | `api.medhata.org` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=api.medhata.org&port=443&secret=eef93ad4b307071b377519e77642bc4dbe6170692e6d6564686174612e6f7267) |


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
