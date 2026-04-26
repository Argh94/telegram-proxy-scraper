# 📊 نتایج استخراج: (آخرین بروزرسانی: 09:10 06-02-1405)

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
| 1 | `204.168.232.187` | `4312` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=204.168.232.187&port=4312&secret=ee104462821249bd7ac519130220c25d097362657262616e6b2e7275) |
| 2 | `connect.tproxyru.live` | `8980` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=connect.tproxyru.live&port=8980&secret=ee104462821249bd7ac519130220c25d09617669746f2e7275) |
| 3 | `2.26.125.172` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.26.125.172&port=443&secret=667161e1e8616dd33fdf8e43e40784d9) |
| 4 | `158.220.96.243` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=158.220.96.243&port=443&secret=ee602404acdf5669aedf205691a613befd636c6f7564666c6172652e636f6d) |
| 5 | `connect.0xl1r.cfd` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=connect.0xl1r.cfd&port=853&secret=eea1f31ce5039ccb8331e906d5ab00a31777622e7275) |
| 6 | `168.222.254.235` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=168.222.254.235&port=443&secret=094873899b09916d9cbf2d97bad72be1) |
| 8 | `45.128.235.218` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.128.235.218&port=443&secret=78aef637c95a4c9b730f2ec43e8ddd9c) |
| 9 | `195.254.165.249` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.249&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 10 | `win.sosproxy.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=win.sosproxy.space&port=443&secret=ee477ccce74a28c13a2ef6ec9e01510c3164726976652e676f6f676c652e636f6d) |
| 11 | `85.192.61.4` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=85.192.61.4&port=443&secret=eeb0e9ec264c0e3e4d375a447217f2100a766b2e636f6d) |
| 13 | `mtproxy.neverspy.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtproxy.neverspy.online&port=443&secret=dde8653d2faf392a302d829d79537abbe7) |
| 14 | `open.smartrix-check.sbs` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=open.smartrix-check.sbs&port=443&secret=ee3c8aca6230c6c86af97f897dd8c6fa046f70656e2e736d6172747269782d636865636b2e736273) |
| 15 | `147.45.103.62` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=147.45.103.62&port=443&secret=eec8f164f338f20e2e3c7a0f4e0408a51270726f787974672e666974) |
| 16 | `paitakht.arasto.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=paitakht.arasto.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 17 | `195.254.165.252` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.252&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 18 | `204.168.226.57` | `8732` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=204.168.226.57&port=8732&secret=ee104462821249bd7ac519130220c25d0979616e6465782e7275) |
| 19 | `204.168.153.162` | `8080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=204.168.153.162&port=8080&secret=dd104462821249bd7ac519130220c25d09) |
| 20 | `107.150.34.100` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=107.150.34.100&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |


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
