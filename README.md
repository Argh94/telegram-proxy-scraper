# 📊 نتایج استخراج: (آخرین بروزرسانی: 22:33 11-01-1405)

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
| 1 | `tgobhod.forum` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tgobhod.forum&port=443&secret=e3b0c44298fc1c149afbf4c8996fb924) |
| 2 | `tg.towersflowerss.com` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=tg.towersflowerss.com&port=443&secret=90eba2e23b01f1cb32b4b9e29bbd7f80) |
| 3 | `mtp.vsemvpn.cc` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtp.vsemvpn.cc&port=443&secret=dd15992ff6e054e6b06faab3689633355c) |
| 4 | `hello-world.tg.engineer` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hello-world.tg.engineer&port=443&secret=d9e48875e76c21092c63e78050247929) |
| 5 | `195.254.165.249` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.249&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 6 | `107.150.34.102` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=107.150.34.102&port=443&secret=ee09db815a6d82a31fda76f872230c69d7706b676275696c642e6f7267) |
| 7 | `194.238.57.153` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=194.238.57.153&port=443&secret=ee2198b6ba0791e91cdbaf7c1fcb3ade9a706574726f766963682e7275) |
| 8 | `free.FCKRKNBOT.COM` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=free.FCKRKNBOT.COM&port=443&secret=ddf48f621b110f302e468756840c29f916) |
| 9 | `proxydlyavseh.sbs` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxydlyavseh.sbs&port=443&secret=2cf24dba5fb0a30e26e83b2ac5b9e29e) |
| 10 | `prxyhub.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=prxyhub.click&port=443&secret=9f27410725ab8ab84ed17daf14723236) |
| 11 | `rkn.tg` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rkn.tg&port=853&secret=ee54ce330e4690cc297d2b031ff3f288b06d742e616b656e61692e636c69636b) |
| 12 | `proxy.ciaowner.lol` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.ciaowner.lol&port=443&secret=ee1459dda62dc99782f8741f1ab0deb4f2706574726f766963682e7275) |
| 13 | `195.254.165.250` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.250&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 14 | `s2.neo-trading.org` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=s2.neo-trading.org&port=443&secret=ee50a0c99bdb7370565b7d74d4d362e27f79612e7275) |
| 16 | `185.237.95.231` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.237.95.231&port=443&secret=ee4571396297582727452bf660db01b789676f6f676c652e636f6d) |
| 17 | `ckopo.cheburnet.tech` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ckopo.cheburnet.tech&port=443&secret=ee79612e72750ce362c1d1f216781718) |
| 18 | `195.254.165.249` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.254.165.249&port=25565&secret=dd79e344818749bd7ac519130220c25d09) |
| 19 | `peyk.acharbashi.info` | `4515` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=peyk.acharbashi.info&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d) |
| 20 | `mt.hq-vpn.com` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mt.hq-vpn.com&port=8443&secret=dd77870ef8bdf3625b6eb083bc2f55877e) |


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
