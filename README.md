# 📊 نتایج استخراج: (آخرین بروزرسانی: 13:53 27-02-1405)

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
| 1 | `195.254.165.143` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.143&port=4455&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d) |
| 2 | `lovevesper.zoryx.tech` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=lovevesper.zoryx.tech&port=853&secret=ee2a43151ca1c75d56a2f8f63c87bfaae374726176656c6c696e652e7275) |
| 3 | `185.117.0.248` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.117.0.248&port=443&secret=eed451f808fd60ed2c45f11d38fdbc87c57961686f6f2e636f6d) |
| 4 | `194.120.230.199` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.120.230.199&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 5 | `femboy.arixo.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=femboy.arixo.shop&port=443&secret=eec11798ab008831b474066c9e1ebf5c99617669746f2e7275) |
| 6 | `185.182.82.73` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.182.82.73&port=443&secret=ee586cb8c65dc8c78f50bd4e573ae25f4873332e616d617a6f6e6177732e636f6d) |
| 7 | `87.120.108.38` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.120.108.38&port=443&secret=f212b4ee21a6f1026aadae4ce0b08f98) |
| 8 | `tp.ascel.la` | `543` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tp.ascel.la&port=543&secret=eec1f71e1f27f7169fff4d48d2d03ca39e7777772e7472656c6c6f2e636f6d) |
| 9 | `now.tproxyru.click` | `8980` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=now.tproxyru.click&port=8980&secret=ee104462821249bd7ac519130220c25d09617669746f2e7275) |
| 10 | `89.125.113.155` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.125.113.155&port=443&secret=ee67af7b545eb72c3c47fc2ccb74aa41c979616e6465782e7275) |
| 11 | `tyan.arixo.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tyan.arixo.shop&port=443&secret=eec11798ab008831b474066c9e1ebf5c99617669746f2e7275) |
| 12 | `89.125.113.189` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.125.113.189&port=443&secret=ee19835aa301cd9a6ceb68ad8d5ad9e0ac79616e6465782e7275) |
| 13 | `mt.corph.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.corph.ru&port=443&secret=ee2ed7517b077ef414e24b106e0729335d6d742e636f7270682e7275) |
| 14 | `138.124.127.157` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=138.124.127.157&port=443&secret=ee776ed6e05e7099a53f923bdcc99f659e766b2e636f6d) |
| 15 | `37.27.38.205` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=37.27.38.205&port=443&secret=ee9d659fc2ae43e0b8323c082960233d7b7777772e636c6f7564666c6172652e636f6d) |
| 16 | `ethereal.arixo.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ethereal.arixo.shop&port=443&secret=eed9fd89062ab62abcbf1bd82dfe914004617669746f2e7275) |
| 17 | `y0u-found-a-way-ou7-of-gorphosts-lockd0wn.top` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=y0u-found-a-way-ou7-of-gorphosts-lockd0wn.top&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 18 | `91.107.189.181` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.107.189.181&port=8443&secret=dd104462821249bd7ac519130220c25d09) |
| 19 | `dealer5-nl.dealer.ac` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dealer5-nl.dealer.ac&port=8443&secret=ee4562bb45c8f3ea3dc772811fb97d0e897477656e7475722e636f6d) |
| 20 | `hot.proxytg.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hot.proxytg.space&port=443&secret=ee12ff13d128ef99c8565ff9b580577959686f742e70726f787974672e7370616365) |


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
