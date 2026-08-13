# 📊 نتایج استخراج: (آخرین بروزرسانی: 10:40 22-05-1405)

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
| 1 | `icon.davazdah.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=icon.davazdah.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 2 | `d6gddje6bbk888hh0djjj00lan.ir.meli-n13.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=d6gddje6bbk888hh0djjj00lan.ir.meli-n13.info&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 3 | `tr.silaber.qzz.io` | `8880` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tr.silaber.qzz.io&port=8880&secret=eec59c9f50147cb42abf6bfc03185b566a636c6f7564666c6172652e636f6d) |
| 4 | `f1.car-race.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=f1.car-race.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 5 | `api2.kvakzon.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=api2.kvakzon.top&port=443&secret=eef6cce71eb4d775d3d908fef1301395b5617069322e6b76616b7a6f6e2e746f70) |
| 6 | `bia.guguli.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bia.guguli.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 7 | `dark.canmycheshm.co.uk.` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dark.canmycheshm.co.uk.&port=25565&secret=ee104462821249bd7ac519130220c25d0963646e2e79656b74616e65742e636f6d) |
| 10 | `shop.startnetwork.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=shop.startnetwork.shop&port=443&secret=dd56771eb41fb312ed11c1993f341aa923) |
| 13 | `webhook.vingardium.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=webhook.vingardium.co.uk.&port=443&secret=eeddffffffc5a1168b2ff3eba31cbfffff7765622e62616c652e6169) |
| 14 | `bezan-roo.connectina.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bezan-roo.connectina.co.uk.&port=443&secret=eeddffffffc5a1168b2ff3eba31cbfffff7765622e62616c652e6169) |
| 15 | `webhook.jinxandjack.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=webhook.jinxandjack.co.uk.&port=443&secret=eeddffffffc5a1168b2ff3eba31cbfffff7765622e62616c652e6169) |
| 17 | `app.what-ever.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=app.what-ever.co.uk.&port=443&secret=eeddffffffc5a1168b2ff3eba31cbfffff7765622e62616c652e6169) |
| 18 | `r1.balebale.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=r1.balebale.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `65.109.30.208` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.30.208&port=8443&secret=dd104462821249bd7ac519130220c25d09) |


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
