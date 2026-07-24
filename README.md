# 📊 نتایج استخراج: (آخرین بروزرسانی: 16:47 02-05-1405)

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
| 1 | `5.75.218.54` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.75.218.54&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `go.pelmeshka.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=go.pelmeshka.top&port=443&secret=eed62d0ddaa394f160c6110be34e8e7fee676f2e70656c6d6573686b612e746f70) |
| 3 | `www.172-63.ir.` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.172-63.ir.&port=8443&secret=ee8b8238601de9360f332514afa56ada45626973636f7474692e79656b74616e65742e636f6d) |
| 5 | `r1.balebale.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=r1.balebale.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 6 | `5.75.220.5` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.75.220.5&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `br.financas.meshflow.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=br.financas.meshflow.ir&port=443&secret=ee1603010200010001fc030386e24c3add7777772e7961686f6f2e636f6d) |
| 8 | `tgb92cf27d.koshkaproxy.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tgb92cf27d.koshkaproxy.shop&port=443&secret=ee1e355000114cdb95628c1564225a404b36326334346231662e6b6f73686b6170726f78792e73686f70) |
| 9 | `vayfay.harah-irancell.info.` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=vayfay.harah-irancell.info.&port=8443&secret=ee1701186abd0ea60123192e26434f91a5626973636f7474692e79656b74616e65742e636f6d) |
| 10 | `class.ir.masnavi.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=class.ir.masnavi.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 12 | `Loti.vak1l.ir` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Loti.vak1l.ir&port=22&secret=dd79e7010200010007f0030386e24c3add) |
| 13 | `sub.iran-tehran.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sub.iran-tehran.co.uk.&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 14 | `webhook.jinxandjack.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=webhook.jinxandjack.co.uk.&port=443&secret=eeddffffffc5a1168b2ff3eba31cbfffff7765622e62616c652e6169) |
| 15 | `naz6ggar.ir.meli-n13.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=naz6ggar.ir.meli-n13.info&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 16 | `fas8t.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fas8t.co.uk.&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 17 | `49.12.117.95` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=49.12.117.95&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `estable.mokhtarname.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=estable.mokhtarname.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 19 | `net.antitspu.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=net.antitspu.com&port=443&secret=ee6a993b83cd2e872361ed136b4e7b28146e65742e616e7469747370752e636f6d) |


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
