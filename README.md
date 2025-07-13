# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Argh94/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 13 July 2025, 18:35 UTC (به وقت ایران: 22:05)

این پروژه یه اسکریپت پایتون برای جمع‌آوری خودکار پروکسی‌های MTProto تلگرام از منابع متنی و کانال‌های تلگرامه. پروکسی‌ها تو فایل `proxy.txt` ذخیره می‌شن و هر 6 ساعت به‌صورت خودکار به‌روزرسانی می‌شن.

## درباره پروژه

این اسکریپت با استفاده از `requests` برای منابع متنی و `selenium` برای صفحات وب کانال‌های تلگرام (`t.me/s/...`) پروکسی‌های MTProto رو جمع‌آوری می‌کنه. پروکسی‌های تکراری حذف می‌شن و نتیجه تو فایل `proxy.txt` ذخیره می‌شه. فرآیند به‌صورت خودکار با **GitHub Actions** هر 6 ساعت اجرا می‌شه.

## ویژگی‌ها
- جمع‌آوری پروکسی از منابع متنی و کانال‌های تلگرام
- به‌روزرسانی خودکار هر 6 ساعت
- حذف پروکسی‌های تکراری
- بدون نیاز به API تلگرام
- مناسب برای کاربرانی که به دنبال پروکسی‌های MTProto فعال هستن

## پیش‌نیازها
- پایتون 3.9
- کتابخونه‌های مورد نیاز: `requests`, `beautifulsoup4`, `selenium`, `pytz`
- فایل `requirements.txt` شامل تمام وابستگی‌هاست.

## نحوه استفاده
1. فایل `proxy.txt` رو از [اینجا](proxy.txt) دانلود کنید.
2. لینک‌های پروکسی (با فرمت `tg://proxy?...` یا `https://t.me/proxy?...`) رو تو کلاینت تلگرام خودتون وارد کنید.
3. برای کپی کردن پروکسی‌های زیر، روی لینک تو ستون "لینک پروکسی" لمس طولانی کنید و گزینه "Copy" رو انتخاب کنید، سپس تو تلگرام پیست کنید.
4. برای به‌روزرسانی دستی، به تب **Actions** تو مخزن برید و روی **Run workflow** کلیک کنید.

## منابع پروکسی
- **منابع متنی**:
  - [MahsaNetConfigTopic](https://raw.githubusercontent.com/MahsaNetConfigTopic/proxy/main/proxies.txt)
  - [ALIILAPRO/MTProtoProxy](https://raw.githubusercontent.com/ALIILAPRO/MTProtoProxy/main/proxy-list.txt)
  - [MhdiTaheri/ProxyCollector](https://raw.githubusercontent.com/MhdiTaheri/ProxyCollector/main/proxy.txt)
- **کانال‌های تلگرام**:
  - iporoto, HiProxy, iproxy, iRoProxy, proxyforopeta, IRN_Proxy, MProxy_ir, ProxyHagh, PyroProxy, ProxyMTProto, MTPro_XYZ, vpns, mtmvpn

## نمونه پروکسی‌ها
جدول زیر 20 پروکسی نمونه از فایل `proxy.txt` رو نشون می‌ده. برای کپی کردن لینک پروکسی، روی متن تو ستون "لینک پروکسی" لمس طولانی کنید و "Copy" رو انتخاب کنید:

| #  | سرور (Server)       | پورت (Port) | وضعیت     | لینک پروکسی                     |
|----|---------------------|-------------|-----------|---------------------------------|
| 1 | 185.253.1.22 | 333 | فعال | `tg://proxy?server=185.253.1.22&port=333&secret=7rXpXsHm4qJ_nKJvoq_oq_ptZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 2 | wait.fiziotr.info | 443 | فعال | `tg://proxy?server=wait.fiziotr.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d` |
| 3 | 95.216.22.207 | 443 | فعال | `tg://proxy?server=95.216.22.207&port=443&secret=iORid5lJ237IiBMGYMQMdw` |
| 4 | 62.60.177.164 | 8443 | فعال | `tg://proxy?server=62.60.177.164&port=8443&secret=FgMBAgABAAfwAwOG4kw63Q` |
| 5 | 193.3.190.71 | 85 | فعال | `tg://proxy?server=193.3.190.71&port=85&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 6 | 88.99.103.117 | 443 | فعال | `tg://proxy?server=88.99.103.117&port=443&secret=104462821249bd7ac519130220c25d09` |
| 7 | 91.84.109.244 | 443 | فعال | `tg://proxy?server=91.84.109.244&port=443&secret=ee00ff000fffff00fff5555ffffffffff56d656469612e737465616d706f77657265642e636f6d` |
| 8 | new-pio-iran-ck-uk-ir.zx2hgujoiah-xy1xutr021-2tk.com | 8443 | فعال | `tg://proxy?server=new-pio-iran-ck-uk-ir.zx2hgujoiah-xy1xutr021-2tk.com&port=8443&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0=` |
| 9 | 195.201.240.32 | 404 | فعال | `tg://proxy?server=195.201.240.32&port=404&secret=eeNEgYdJvXrFGRMCIMJdCQ==` |
| 10 | 87.248.132.96 | 200 | فعال | `tg://proxy?server=87.248.132.96&port=200&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 11 | 87.248.132.37 | 70 | فعال | `tg://proxy?server=87.248.132.37&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 12 | 157.180.32.24 | 888 | فعال | `tg://proxy?server=157.180.32.24&port=888&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 13 | 62.60.176.188 | 443 | فعال | `tg://proxy?server=62.60.176.188&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 14 | 62.60.178.195 | 443 | فعال | `tg://proxy?server=62.60.178.195&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)|` |
| 15 | 91.99.79.124 | 443 | فعال | `tg://proxy?server=91.99.79.124&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 16 | 167.235.169.138 | 443 | فعال | `tg://proxy?server=167.235.169.138&port=443&secret=7gffffffff` |
| 17 | 8.217.25.47 | 443 | فعال | `tg://proxy?server=8.217.25.47&port=443&secret=ee52b986ec192f5e0d25d7e2ee6fdeffcc617a7572652e6d6963726f736f66742e636f6d` |
| 18 | 87.248.132.57 | 200 | فعال | `tg://proxy?server=87.248.132.57&port=200&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 19 | 109.104.154.230 | 443 | فعال | `tg://proxy?server=109.104.154.230&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 20 | 51.159.149.220 | 8000 | فعال | `tg://proxy?server=51.159.149.220&port=8000&secret=eee72cf91a4fee7902896720b31c3c14e27777772e736974652e636f6d` |


> **توجه**: این جدول فقط برای نمایش نمونه‌ست. برای دسترسی به همه پروکسی‌های به‌روز، فایل [proxy.txt](proxy.txt) رو دانلود کنید.

## مشارکت
از مشارکت شما استقبال می‌کنیم! اگه ایده‌ای برای بهبود اسکریپت دارید یا می‌خواید منابع جدیدی اضافه کنید:
1. یه **Issue** تو مخزن باز کنید.
2. یا یه **Pull Request** با تغییرات پیشنهادی بفرستید.

## لایسنس
این پروژه تحت [لایسنس MIT](LICENSE) منتشر شده.

## لینک‌های مفید
- 📄 [لیست پروکسی‌ها](proxy.txt)
- 🚀 [وضعیت GitHub Actions](https://github.com/Argh94/telegram-proxy-scraper/actions)
- ⭐ [ما رو ستاره بدید!](https://github.com/Argh94/telegram-proxy-scraper)

## Stargazers در گذر زمان
[![Stargazers over time](https://starchart.cc/Argh94/telegram-proxy-scraper.svg?variant=adaptive)](https://starchart.cc/Argh94/telegram-proxy-scraper)

---

سپاس از استفاده از **Telegram Proxy Scraper**! اگه سؤالی دارید، تو بخش Issues مطرح کنید. 🌟
