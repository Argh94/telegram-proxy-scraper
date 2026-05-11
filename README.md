# 📊 نتایج استخراج: (آخرین بروزرسانی: 07:00 21-02-1405)

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
| 1 | `s5.proxyru.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s5.proxyru.top&port=443&secret=eefe281d2bfa13f991ed6be43138e5e14c79612e7275) |
| 2 | `mtp.yard-tg-bot.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtp.yard-tg-bot.ru&port=443&secret=eef658bb6d89b284874149c13e7d27d9da79616e6465782e7275) |
| 3 | `khoda.hafez.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=khoda.hafez.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 4 | `tgobhod.forum` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tgobhod.forum&port=443&secret=ee1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d74676f62686f642e666f72756d) |
| 5 | `79.137.196.223` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.137.196.223&port=443&secret=eeee525b778775d1c3b1e2beb8af08e2017777772e636c6f7564666c6172652e636f6d) |
| 6 | `now.tproxyru.click` | `8980` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=now.tproxyru.click&port=8980&secret=ee104462821249bd7ac519130220c25d09617669746f2e7275) |
| 7 | `loly.etherealvpn.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=loly.etherealvpn.uk&port=443&secret=ee2e7799fb9db11363814b3191898b4822706574726f766963682e7275) |
| 8 | `i-love-femboys.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=i-love-femboys.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 9 | `194.50.94.65` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.50.94.65&port=443&secret=ee0c534d144bf266c6b7a09c532a2e529f79616e6465782e7275) |
| 10 | `y0u-found-a-way-ou7-of-gorphosts-lockd0wn.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=y0u-found-a-way-ou7-of-gorphosts-lockd0wn.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 11 | `tg2.uniqvpn.online` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg2.uniqvpn.online&port=4515&secret=ee2e1e044a0ee0ce3efbbd27ef6a65f5126170706c652e636f6d) |
| 12 | `proxy.nolags.pw` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.nolags.pw&port=443&secret=dde8f80bb2dbf4105c07ca7559599924c9) |
| 13 | `194.50.94.65` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.50.94.65&port=443&secret=ee0c534d144bf266c6b7a09c532a2e529f79616e6465782e7275) |
| 14 | `focus-ultimate.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=focus-ultimate.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 15 | `132.243.235.189` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.235.189&port=443&secret=ee580a561631a7217d4a0607bb2be8930e79616e6465782e7275) |
| 16 | `2.27.41.207` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.27.41.207&port=443&secret=9436fa39ab47ccb34f217ac6d06b4e58) |
| 17 | `132.243.235.188` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.235.188&port=443&secret=eecff01a06513433100e81c6eadff452e779616e6465782e7275) |
| 18 | `mtp.webvirt.cloud` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtp.webvirt.cloud&port=443&secret=ee938dd87467bc49301de2e9765cf20f4374656c2e776562766972742e636c6f7564) |
| 19 | `89.125.113.155` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.125.113.155&port=443&secret=ee67af7b545eb72c3c47fc2ccb74aa41c979616e6465782e7275) |
| 20 | `46.225.29.180` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.225.29.180&port=443&secret=ee636c6f7564666c6172652e636f6db6) |


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
