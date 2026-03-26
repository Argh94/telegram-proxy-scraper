# 📊 نتایج استخراج: (آخرین بروزرسانی: 16:46 06-01-1405)

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
| 1 | `aftermost.blastolation.dodging.dornoch.jeep.pinoyfilms.net` | `8450` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=aftermost.blastolation.dodging.dornoch.jeep.pinoyfilms.net&port=8450&secret=f2697137ca13fc2ad81a4b0d4ec2a3d1) |
| 3 | `195.254.165.247` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.247&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 4 | `195.254.165.252` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.252&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 5 | `bosnia.capture.misdeem.offcast.washerwoman.pinoyteleseryehd.net` | `8500` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bosnia.capture.misdeem.offcast.washerwoman.pinoyteleseryehd.net&port=8500&secret=82bb272c25579297178d08fff7dbb0d6) |
| 6 | `142.54.189.106` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=142.54.189.106&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 7 | `146.103.107.95` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=146.103.107.95&port=8443&secret=dd653799bd79e146d8e7558ebdeaf73dbd) |
| 8 | `he.67.mtproto.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=he.67.mtproto.ru&port=443&secret=ee2111222233334444555566667777888862726f777365722e79616e6465782e636f6d) |
| 9 | `5.39.250.20` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.39.250.20&port=443&secret=6356ebb33a57b6deda8a1c3cf2aee557) |
| 10 | `194.154.29.221` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.154.29.221&port=443&secret=993032016aa6265bcd952b0b0a871344) |
| 11 | `195.254.165.253` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.253&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 12 | `Fast.love-internet.xyz` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Fast.love-internet.xyz&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |
| 13 | `195.254.165.241` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.241&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 14 | `de.nerdpol.ovh` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=de.nerdpol.ovh&port=4515&secret=ee3177bef597bf8246bae855cee6fe0aa564652e6e657264706f6c2e6f7668) |
| 15 | `xfs1.gbird.top` | `6443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=xfs1.gbird.top&port=6443&secret=ddecad3d673e42dc10cae6fa9bcebcd5f6) |
| 16 | `mt.skadi.help` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.skadi.help&port=443&secret=dd382a00f48a0592ff49a30aa55017cc09) |
| 17 | `91.107.169.174` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.169.174&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 18 | `194.87.252.116` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.87.252.116&port=443&secret=6356ebb33a57b6deda8a1c3cf2aee557) |
| 19 | `tgwh.magproxy.com` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tgwh.magproxy.com&port=8443&secret=eeb30fc4df699024f7a5dec0b0e66524b16465762e6373373737372e766b2e7275) |
| 20 | `dedicated.love-internet.xyz` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dedicated.love-internet.xyz&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |


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
