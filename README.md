# 📊 نتایج استخراج: (آخرین بروزرسانی: 13:14 28-12-1404)

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
| 1 | `185.117.0.248` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.117.0.248&port=443&secret=eed451f808fd60ed2c45f11d38fdbc87c57961686f6f2e636f6d) |
| 2 | `peyk.acharbashi.info` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=peyk.acharbashi.info&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |
| 3 | `general.irancell-ir.cfd` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=general.irancell-ir.cfd&port=443&secret=ee1603010200010001fc030386e24c3add626973636F7474692E79656B74616E65742E636F6D) |
| 4 | `195.254.165.244` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.244&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 5 | `general.irancell-ir.cfd` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=general.irancell-ir.cfd&port=443&secret=ee1603010200010001fc030386e24c3add626973636F7474692E79656B74616E65742E636F6D) |
| 6 | `collider.web-yektanet-com.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=collider.web-yektanet-com.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636F7474692E79656B74616E65742E636F6D) |
| 7 | `de.nerdpol.ovh` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=de.nerdpol.ovh&port=4515&secret=ee3177bef597bf8246bae855cee6fe0aa564652e6e657264706f6c2e6f7668) |
| 11 | `go.bolshevps.su` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=go.bolshevps.su&port=443&secret=ee617782cbbfb6dcc27b0e338f570da65f6164732e78352e7275) |
| 12 | `dowd.sportsmanship.steeplechaser.thy.urceolate.kapitoshka.info` | `15417` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dowd.sportsmanship.steeplechaser.thy.urceolate.kapitoshka.info&port=15417&secret=d6db8ab62ff9b9f70f6ca15ccb98c222) |
| 13 | `mix.road-digger.info.` | `61016` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mix.road-digger.info.&port=61016&secret=79e7010200010007f0030386e24c3add) |
| 14 | `147.125.130.47` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=147.125.130.47&port=2083&secret=ee1603010200010001fc030386e24c3add68656c702e737465616d706f77657265642e636f6d) |
| 16 | `proxy.ciaowner.lol` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.ciaowner.lol&port=443&secret=ee1459dda62dc99782f8741f1ab0deb4f2706574726f766963682e7275) |
| 17 | `dowd.sportsmanship.steeplechaser.thy.urceolate.kapitoshka.info` | `15417` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dowd.sportsmanship.steeplechaser.thy.urceolate.kapitoshka.info&port=15417&secret=d6db8ab62ff9b9f70f6ca15ccb98c222) |
| 18 | `147.125.130.64` | `2083` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=147.125.130.64&port=2083&secret=ee1603010200010001fc030386e24c3add68656c702e737465616d706f77657265642e636f6d) |
| 19 | `total.beyondeson-co.cfd` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=total.beyondeson-co.cfd&port=443&secret=ee1603010200010001fc030386e24c3add626973636F7474692E79656B74616E65742E636F6D) |
| 20 | `tg.vpnspacev.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.vpnspacev.com&port=443&secret=bc184fc14b62b9b1dc5f34edf9476421) |


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
