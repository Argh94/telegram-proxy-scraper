# 📊 نتایج استخراج: (آخرین بروزرسانی: 22:34 20-02-1405)

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
| 1 | `getfastlink.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=getfastlink.click&port=443&secret=ee47e3a8b2c1f4e9d0a6b5c8d7e4f3a2b1676574666173746c696e6b2e636c69636b) |
| 2 | `132.243.235.201` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.235.201&port=443&secret=ee9e0de647c5d593c800e577d6cc16f41d79616e6465782e7275) |
| 3 | `5hu7-up-4nd-sell-me-mor3-th353-chocol47e5.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5hu7-up-4nd-sell-me-mor3-th353-chocol47e5.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 4 | `185.117.0.248` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.117.0.248&port=443&secret=eed451f808fd60ed2c45f11d38fdbc87c57961686f6f2e636f6d) |
| 5 | `free-nl.kimt.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=free-nl.kimt.space&port=443&secret=ee3efced182e68e689a17d58c71ff6fafe667265652d6e6c2e6b696d742e7370616365) |
| 6 | `reboot.tikla.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=reboot.tikla.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 7 | `tg.fi.coconutstrip.co` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.fi.coconutstrip.co&port=443&secret=ee6d2863461800ee99ef94c7ddcc761d0e79612e7275) |
| 8 | `s.qcold.online` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s.qcold.online&port=853&secret=eea65967b55fdb60e0b3ac69aa46abc3de732e71636f6c642e6f6e6c696e65) |
| 9 | `rkn.lat` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rkn.lat&port=443&secret=eed33cc1365fef45292c52736f6695df6f6d61782e7275) |
| 10 | `46.225.29.180` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.225.29.180&port=443&secret=ee636c6f7564666c6172652e636f6db6) |
| 11 | `132.243.235.189` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.235.189&port=443&secret=ee580a561631a7217d4a0607bb2be8930e79616e6465782e7275) |
| 12 | `89.125.113.8` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.125.113.8&port=443&secret=ee5b99cc79c1fe095be478df4111e00b6379616e6465782e7275) |
| 13 | `132.243.235.143` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.235.143&port=443&secret=ee1a043ca04520458fe7fc96309b095f3679616e6465782e7275) |
| 14 | `mtp.fsoc-app.online` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtp.fsoc-app.online&port=853&secret=ee1d49946a9bd11022149e2c68f1d75f6774656c2e66736f632d6170702e6f6e6c696e65) |
| 15 | `132.243.235.187` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.235.187&port=443&secret=ee89db719934b04d0875b8a84c948e57fa79616e6465782e7275) |
| 16 | `195.254.165.250` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.250&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 17 | `own.telbet.lol` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=own.telbet.lol&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 18 | `132.243.235.190` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=132.243.235.190&port=443&secret=ee157938a8c2f93afd4880d5bc6a1c8da279616e6465782e7275) |
| 19 | `tavakalta-alalah.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tavakalta-alalah.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 20 | `one.turboproxy.pro` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=one.turboproxy.pro&port=443&secret=ee74e2e117f2160c55370f68df7381d5d361657a612e7275) |


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
