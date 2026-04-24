# 📊 نتایج استخراج: (آخرین بروزرسانی: 13:52 04-02-1405)

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
| 1 | `107.150.34.98` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=107.150.34.98&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 2 | `pvnexus.xyz` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pvnexus.xyz&port=443&secret=eed68360458af63073bac1394e8c7a48da70766e657875732e78797a) |
| 3 | `2.27.86.91` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.27.86.91&port=443&secret=eee3ba5e814a7b81ef8d7608d18813913679616e6465782e7275) |
| 4 | `5.75.212.43` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.75.212.43&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 5 | `195.254.165.250` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.250&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 7 | `168.222.254.236` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=168.222.254.236&port=443&secret=1e7143ca2186934f892b7ec833ce209b) |
| 8 | `46.62.248.139` | `6532` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.62.248.139&port=6532&secret=ee104462821249bd7ac519130220c25d096d61782e7275) |
| 9 | `anarchy.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=anarchy.click&port=443&secret=ee7118c792a6da15636cc9753bf90cfc2d62726f777365722e79616e6465782e636f6d) |
| 10 | `195.254.165.247` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.247&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 11 | `compassionate-heyrovsky.cfd` | `1984` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=compassionate-heyrovsky.cfd&port=1984&secret=ddc76b8cb6d99f20a7c1a3ef1b67bbb070) |
| 12 | `proxy.freetg.su` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.freetg.su&port=443&secret=f7a7d30a3a78dc160b43a8ed332477e1) |
| 13 | `107.150.34.102` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=107.150.34.102&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 14 | `204.168.153.162` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=204.168.153.162&port=8080&secret=dd104462821249bd7ac519130220c25d09) |
| 15 | `tg.plusonevpn.com` | `1984` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.plusonevpn.com&port=1984&secret=dd4c7671c23268cbcb7330ff7ee9ab0622) |
| 16 | `proxytg.fit` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxytg.fit&port=443&secret=eec8f164f338f20e2e3c7a0f4e0408a51270726f787974672e666974) |
| 18 | `195.254.165.252` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.252&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 19 | `45.128.235.219` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.128.235.219&port=443&secret=4ae50768d6cdfc8c708fb81c7e582072) |
| 20 | `freeroute.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=freeroute.online&port=443&secret=eed68360458af63073bac1394e8c7a48da66726565726f7574652e6f6e6c696e65) |


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
