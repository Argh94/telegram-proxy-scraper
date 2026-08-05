# 📊 نتایج استخراج: (آخرین بروزرسانی: 04:59 14-05-1405)

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
| 1 | `a.red-eyes.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=a.red-eyes.co.uk&port=443&secret=ee3d452ace1dc3eba3f6064fe8291dfd59612e7265642d657965732e636f2e756b) |
| 2 | `googel.alo-otp.info.` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=googel.alo-otp.info.&port=25565&secret=ee104462821249bd7ac519130220c25d0963646e2e79656b74616e65742e636f6d) |
| 3 | `adieu.shmelproxy.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=adieu.shmelproxy.top&port=443&secret=ee6a0333c1db3f8eaba5c76731a44203b6617669746f2e7275) |
| 4 | `super.sub-ploter.co.uk` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=super.sub-ploter.co.uk&port=25565&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 5 | `web.utkanos.life` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=web.utkanos.life&port=443&secret=ee331ae197830a753bd9afd0c956fac4f37765622e75746b616e6f732e6c696665) |
| 7 | `app.what-ever.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=app.what-ever.co.uk.&port=443&secret=eeddffffffc5a1168b2ff3eba31cbfffff7765622e62616c652e6169) |
| 8 | `79.137.196.223` | `10443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=79.137.196.223&port=10443&secret=ee63fccdeb9951e5f99d66d274148278b97777772e636c6f7564666c6172652e636f6d) |
| 9 | `hub.savelyev.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=hub.savelyev.click&port=443&secret=ee609a2ad7e277c6eb2dd39767e12777b86875622e736176656c7965762e636c69636b) |
| 11 | `06dgvasl22jka013377.ir.meli-n13.info` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=06dgvasl22jka013377.ir.meli-n13.info&port=8443&secret=104462821249bd7ac519130220c25d09) |
| 13 | `Speed-speed.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Speed-speed.co.uk.&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 15 | `Hel-hi.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Hel-hi.co.uk.&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 16 | `logs.jinxandjack.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=logs.jinxandjack.co.uk.&port=443&secret=eeddffffffc5a1168b2ff3eba31cbfffff7765622e62616c652e6169) |
| 18 | `wave.savelyev.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=wave.savelyev.click&port=443&secret=eeba2e1341a08483c2cede6818498348ff776176652e736176656c7965762e636c69636b) |
| 19 | `yektanet.iranbetter.site` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=yektanet.iranbetter.site&port=8443&secret=ee26b5d67e69dc5cad703076a2e6967cb863646e2e79656b74616e65742e636f6d) |
| 20 | `soh5.goooalir.co.uk` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=soh5.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09) |


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
