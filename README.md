# 📊 نتایج استخراج: (آخرین بروزرسانی: 14:39 06-05-1405)

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License" />
  <img src="https://img.shields.io/badge/python-3.9-blue" alt="Python 3.11" />
  <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions Welcome" />
  <img src="https://img.shields.io/badge/Proxy%20Scraper-Running-green" alt="Proxy Scraper" />
  <img src="https://github.com/Argh94/telegram-proxy-scraper/actions/workflows/main.yml/badge.svg" alt="Proxy Scraper Workflow" />
  <img src="https://img.shields.io/github/last-commit/Argh94/telegram-proxy-scraper" alt="GitHub Last Commit" />
  <img src="https://img.shields.io/github/issues/Argh94/telegram-proxy-scraper" alt="GitHub Issues" />
</p>

این پروژه یک اسکریپت پایتون برای جمع‌آوری خودکار پروکسی‌های MTProto تلگرام از منابع متنی و کانال‌های تلگرام است. پروکسی‌ها در فایل `proxy.txt` ذخیره می‌شوند و هر 3 ساعت به‌صورت خودکار به‌روزرسانی می‌شوند.

## ✨ درباره پروژه

این اسکریپت با استفاده از `requests` برای منابع متنی و کانال‌های تلگرام، پروکسی‌های MTProto را جمع‌آوری می‌کند. پروکسی‌های تکراری حذف شده و نتایج در فایل `proxy.txt` ذخیره می‌شوند. این فرآیند به‌صورت خودکار با **GitHub Actions** هر 3 ساعت اجرا می‌شود.

## 🚀 ویژگی‌ها
- 🌐 جمع‌آوری پروکسی از منابع متنی و کانال‌های تلگرام
- 🔄 به‌روزرسانی خودکار هر 3 ساعت
- 🗑 حذف پروکسی‌های تکراری
- 🔑 بدون نیاز به API تلگرام
- 📱 مناسب برای کاربران در جستجوی پروکسی‌های فعال MTProto

## 📋 پیش‌نیازها
- 🐍 پایتون 3.9
- 📦 کتابخانه‌های مورد نیاز: `requests`, `beautifulsoup4`, `pytz`, `jdatetime`
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
| 1 | `bala.hastim.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bala.hastim.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 2 | `class.ir.masnavi.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=class.ir.masnavi.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 3 | `cdn.savelyev.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cdn.savelyev.click&port=443&secret=ee47db8cfb73a38af6c54d8976432e265863646e2e736176656c7965762e636c69636b) |
| 4 | `mirror.balalaika.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mirror.balalaika.click&port=443&secret=ee82514fa3e992fa79f3fd3bff4db750116d6972726f722e62616c616c61696b612e636c69636b) |
| 6 | `host.mizbanonline.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=host.mizbanonline.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 7 | `chat.avacloud.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=chat.avacloud.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 8 | `ma.hastim.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ma.hastim.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 9 | `New1.ugtd8sxxcyt.co.uk` | `4455` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=New1.ugtd8sxxcyt.co.uk&port=4455&secret=dd104462821249bd7ac519130220c25d09) |
| 10 | `secure.gorbushkin.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=secure.gorbushkin.click&port=443&secret=ee2566052eb7f98d9601ca0b656f9032177365637572652e676f72627573686b696e2e636c69636b) |
| 11 | `ad5.arixo.shop` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ad5.arixo.shop&port=443&secret=ee995469d4d5a3221f69a1cc24d1cafa506164322e617269786f2e73686f70) |
| 12 | `super.sub-ploter.co.uk` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=super.sub-ploter.co.uk&port=25565&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 13 | `sisu.proxytales.life` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sisu.proxytales.life&port=443&secret=ee6a0333c1db3f8eaba5c76731a44203b6617669746f2e7275) |
| 14 | `178.105.141.172` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.105.141.172&port=443&secret=ee8db761231b91c7c07ac0a6e7323ad41b676f6f676c65617069732e636f6d) |
| 15 | `rudomain.info.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=rudomain.info.&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 16 | `b.sub-ploter.co.uk` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=b.sub-ploter.co.uk&port=22&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 18 | `runpy.estakhr.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=runpy.estakhr.info&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 19 | `kpu00lllll.ir.meli-n13.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kpu00lllll.ir.meli-n13.info&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 20 | `googel.alo-otp.info.` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=googel.alo-otp.info.&port=25565&secret=ee104462821249bd7ac519130220c25d0963646e2e79656b74616e65742e636f6d) |


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
