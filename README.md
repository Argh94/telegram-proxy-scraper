# 📊 نتایج استخراج: (آخرین بروزرسانی: 09:15 10-05-1405)

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
| 1 | `mt.nowabst.net` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.nowabst.net&port=853&secret=ee4e9fcd5caf6e9be2f8ec43e370e902d6766b2e636f6d) |
| 3 | `subobdoa.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=subobdoa.co.uk.&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 4 | `most.karshenasi.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=most.karshenasi.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 5 | `night.workingproxy.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=night.workingproxy.xyz&port=443&secret=dde5d60707998c23e890e00e0bbe5eacdd) |
| 6 | `s44447n.ir.ir.ir.meli-n12.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s44447n.ir.ir.ir.meli-n12.info&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `medblock.ink` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=medblock.ink&port=443&secret=ee81bcf42079b8aea4608000f6d77285f36d6564626c6f636b2e696e6b) |
| 9 | `ge.nowabst.net` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ge.nowabst.net&port=853&secret=ee5a281fcc91f7ec3ce293d643395222ad766b2e636f6d) |
| 10 | `f1.car-race.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=f1.car-race.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 11 | `server.nl-arvancloud.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=server.nl-arvancloud.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 12 | `46.225.26.227` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.225.26.227&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 13 | `gate.soluqent.pro` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=gate.soluqent.pro&port=443&secret=eebdbd1f66a7c00e7bf92c6436d457861d676174652e736f6c7571656e742e70726f) |
| 15 | `dark.basicscotch.co.uk` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dark.basicscotch.co.uk&port=22&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 16 | `portal.balalaika.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=portal.balalaika.click&port=443&secret=ee3c7b046d6a7b00b2c910cd755314eb2e706f7274616c2e62616c616c61696b612e636c69636b) |
| 18 | `mizaneshgh2.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mizaneshgh2.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 19 | `va7slsho.ir.meli-n13.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=va7slsho.ir.meli-n13.info&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 20 | `chelipa.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=chelipa.co.uk.&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |


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
