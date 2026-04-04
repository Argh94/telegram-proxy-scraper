# 📊 نتایج استخراج: (آخرین بروزرسانی: 19:03 15-01-1405)

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License" />
  <img src="https://img.shields.io/badge/python-3.9-blue" alt="Python 3.9" />
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
| 1 | `fi-1.quomis.pw` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fi-1.quomis.pw&port=443&secret=ee6b13503e2e0bbb66b5dad03ba89088b56d61782e7275) |
| 2 | `176.108.255.233` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=176.108.255.233&port=443&secret=dd7c5d4e1f2a3b9c8d7e6f5a4b3c2d1e0f) |
| 3 | `prx.today` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=prx.today&port=443&secret=b3f0c7f6af7dc2dc2e9c80d0d80e8162) |
| 4 | `rkn.tg` | `1337` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rkn.tg&port=1337&secret=dda2d3fa639a6ddcf8d6d1c5913d001531) |
| 5 | `195.66.87.243` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.66.87.243&port=443&secret=ee361e6f00fe51e3551cfebfbd6ebe75e27765622e6d61782e7275) |
| 6 | `mt.fl8.vdl.lat` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.fl8.vdl.lat&port=443&secret=dd1a21752bd8823f6d2e7ac3642f2608ac) |
| 7 | `193.104.198.0` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=193.104.198.0&port=443&secret=dd40aa72a0f79e4f3b2be25dd56e07de72) |
| 8 | `proxytelega.store` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxytelega.store&port=443&secret=5d41402abc4b2a76b9719d911017c592) |
| 9 | `p5.new-ai.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=p5.new-ai.uk&port=443&secret=ee27b68bda6b4b99915f73a423b17f768470352e6e65772d61692e756b) |
| 10 | `3.hajrozbeh.onl` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3.hajrozbeh.onl&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 11 | `proxydazhenaparkovke.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxydazhenaparkovke.site&port=443&secret=dde8aa2e8c1ad50570b7d6fe7e0ba3d677) |
| 12 | `2A.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2A.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 13 | `27289292.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=27289292.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 14 | `91.149.241.35` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.149.241.35&port=443&secret=eed95a7f7f310f44feab4f9d1a8a703f536769746875622e636f6d) |
| 15 | `89.208.85.188` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.208.85.188&port=8443&secret=eea94a50c3db2b9e640351831e8bd42bba6164732e78352e7275) |
| 16 | `laura.proxyprosto.sbs` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=laura.proxyprosto.sbs&port=443&secret=ee79612e7275dcdfd8017f6ee7c1beb0) |
| 17 | `takhtekhab.rylvin.bar` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=takhtekhab.rylvin.bar&port=443&secret=5839ef5285c1a55062cc35f9197003cb) |
| 18 | `178.104.98.160` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.104.98.160&port=443&secret=ee636c6f7564666c6172652e636f6db6) |
| 19 | `2.27.23.23` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.27.23.23&port=8443&secret=f5a97ceadd1bbedd918fbd9f1c9387dd) |
| 20 | `95.179.209.62` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.179.209.62&port=443&secret=ee141abb4d84cd9487e359caea13e460) |


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
