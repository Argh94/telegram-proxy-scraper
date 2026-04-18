# 📊 نتایج استخراج: (آخرین بروزرسانی: 22:23 29-01-1405)

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
| 1 | `49.13.35.164` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=49.13.35.164&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 2 | `oneproxys.best` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=oneproxys.best&port=443&secret=eed68360458af63073bac1394e8c7a48da6f6e6570726f7879732e62657374) |
| 3 | `compassionate-heyrovsky.cfd` | `1984` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=compassionate-heyrovsky.cfd&port=1984&secret=ddc76b8cb6d99f20a7c1a3ef1b67bbb070) |
| 4 | `how.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=how.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 5 | `poll1704.mtproxygram.lol` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=poll1704.mtproxygram.lol&port=443&secret=eec39eef5b0ab34eb882b893c156b4c14a62726f777365722e79616e6465782e636f6d) |
| 6 | `178.156.131.76` | `1080` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.156.131.76&port=1080&secret=dd104462821249bd7ac519130220c25d09) |
| 7 | `94.130.190.170` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=94.130.190.170&port=443&secret=dd104462821249bd7ac519130220c25d09) |
| 8 | `6161627.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=6161627.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 9 | `195.254.165.249` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.249&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 10 | `27289292.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=27289292.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 11 | `rkn.tg` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rkn.tg&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 12 | `195.254.165.252` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.252&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 13 | `2A.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2A.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 14 | `195.254.165.247` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.247&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 15 | `news1704.mtproxygram.lol` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=news1704.mtproxygram.lol&port=443&secret=ee608248722a8f45103ed03c7994abf9b062726f777365722e79616e6465782e636f6d) |
| 16 | `zoomit.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=zoomit.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 17 | `172.65.117.172` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=172.65.117.172&port=22&secret=dd79e344818749bd7ac519130220c25d09) |
| 18 | `cz.ciaowner.lol` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cz.ciaowner.lol&port=443&secret=ee3bde6d51d22cf4b0b48127147ca830f869642e766b2e636f6d) |
| 19 | `proxystepa.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxystepa.site&port=443&secret=eed68360458af63073bac1394e8c7a48da70726f787973746570612e73697465) |
| 20 | `3.hajrozbeh.onl` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3.hajrozbeh.onl&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |


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
