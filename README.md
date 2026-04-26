# 📊 نتایج استخراج: (آخرین بروزرسانی: 10:59 06-02-1405)

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
| 1 | `204.168.226.57` | `8732` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=204.168.226.57&port=8732&secret=ee104462821249bd7ac519130220c25d0979616e6465782e7275) |
| 2 | `62.60.252.181` | `8000` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=62.60.252.181&port=8000&secret=dd3041b25c52eb89bf1489661f3322df76) |
| 3 | `proxy.proxymtproto.net` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.proxymtproto.net&port=443&secret=dd97caa3c6888366f26b12f994f02ecf1a) |
| 4 | `204.168.232.187` | `4312` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=204.168.232.187&port=4312&secret=ee104462821249bd7ac519130220c25d097362657262616e6b2e7275) |
| 5 | `tproxyru.live.` | `8980` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tproxyru.live.&port=8980&secret=ee104462821249bd7ac519130220c25d09617669746f2e7275) |
| 6 | `77.110.110.179` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=77.110.110.179&port=443&secret=ee72687e2188e615b214bffac01d399ee7766b2e636f6d) |
| 7 | `connect.tproxyru.live` | `8980` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=connect.tproxyru.live&port=8980&secret=ee104462821249bd7ac519130220c25d09617669746f2e7275) |
| 8 | `tproxyru.live.` | `8980` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tproxyru.live.&port=8980&secret=ee104462821249bd7ac519130220c25d09617669746f2e7275) |
| 9 | `s.rkn.tg` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s.rkn.tg&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 10 | `mtproxy.neverspy.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtproxy.neverspy.online&port=443&secret=dde8653d2faf392a302d829d79537abbe7) |
| 11 | `proxytg.fit` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxytg.fit&port=443&secret=eec8f164f338f20e2e3c7a0f4e0408a51270726f787974672e666974) |
| 12 | `3.hajrozbeh.onl` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3.hajrozbeh.onl&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 13 | `freeroute.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=freeroute.online&port=443&secret=eed68360458af63073bac1394e8c7a48da66726565726f7574652e6f6e6c696e65) |
| 14 | `158.220.96.243` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=158.220.96.243&port=443&secret=ee602404acdf5669aedf205691a613befd636c6f7564666c6172652e636f6d) |
| 15 | `65.109.30.209` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.30.209&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 16 | `147.45.103.62` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=147.45.103.62&port=443&secret=eec8f164f338f20e2e3c7a0f4e0408a51270726f787974672e666974) |
| 17 | `77.73.135.166` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=77.73.135.166&port=443&secret=ee41ab28a235a527f950facce3193ad74e766b2e636f6d) |
| 18 | `79.143.93.219` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.143.93.219&port=8443&secret=ee174f8ad75b1f66755d9fef2e7a02bc987777772e676f6f676c652e636f6d) |
| 19 | `172.65.117.172` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.65.117.172&port=22&secret=dd79e344818749bd7ac519130220c25d09) |
| 20 | `107.150.34.101` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=107.150.34.101&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |


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
