# 📊 نتایج استخراج: (آخرین بروزرسانی: 12:19 01-04-1405)

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
| 1 | `link.mishkalapy.life` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=link.mishkalapy.life&port=443&secret=eeb6b2b376ea60c64410542c640dc2765e6c696e6b2e6d6973686b616c6170792e6c696665) |
| 3 | `subobdoa.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=subobdoa.co.uk.&port=443&secret=eef0eeb0bd9adc4fd4a93994ee3b2a216b63646e2e79656b74616e65742e636f6d) |
| 4 | `fast.garden-troll.life` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=fast.garden-troll.life&port=443&secret=eea3dc3cf5e6fb44c1e2f2cdd3e9bf9acb666173742e67617264656e2d74726f6c6c2e6c696665) |
| 5 | `persian.gulf.ir.olsjddhf.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=persian.gulf.ir.olsjddhf.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 6 | `31.41.33.114` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=31.41.33.114&port=443&secret=eee854b22396ba5a74f23b6f126108294a6972616e2e6d69642e7275) |
| 7 | `sv.just-money.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sv.just-money.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 8 | `go.pelmeshka.top` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=go.pelmeshka.top&port=443&secret=eed1f77690d4e79770a774d33db8dd834c676f2e70656c6d6573686b612e746f70) |
| 9 | `kala.imalz.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kala.imalz.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 10 | `For.you.ir.gdhbvjshjrf.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=For.you.ir.gdhbvjshjrf.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 13 | `portal.balalaika.click` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=portal.balalaika.click&port=443&secret=ee6d1c554e874ffba6252e1e36768eb5a4706f7274616c2e62616c616c61696b612e636c69636b) |
| 14 | `167.233.48.222` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.233.48.222&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 15 | `kha8shen.co.uk.` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=kha8shen.co.uk.&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 16 | `windows.old-balance.co.uk` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=windows.old-balance.co.uk&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 17 | `87.229.56.183` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.229.56.183&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 18 | `alo-alo.info.01-62.ir.` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=alo-alo.info.01-62.ir.&port=8443&secret=ee6321a38187495dfac59a030220c25d8e626973636f7474692e79656b74616e65742e636f6d) |
| 19 | `login.veltura.digital` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=login.veltura.digital&port=443&secret=ee4f5545c56e0ee3271606a2985459773e6c6f67696e2e76656c747572612e6469676974616c) |


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
