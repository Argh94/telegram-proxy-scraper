# 📊 نتایج استخراج: (آخرین بروزرسانی: 02:26 26-03-1405)

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
| 1 | `87.248.129.102` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.102&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 2 | `1.vak1l.ir` | `22` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=1.vak1l.ir&port=22&secret=dd79e7010200010007f0030386e24c3add) |
| 3 | `87.248.129.16` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.16&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 4 | `87.248.129.217` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.217&port=443&secret=eea44ea5e1b8331727a895b81e8c43c59e7777772e617276616e636c6f75642e6972) |
| 5 | `bolt.proxyonline.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bolt.proxyonline.online&port=443&secret=ee98741a4df96ee86a25ca542a538a3484626f6c742e70726f78796f6e6c696e652e6f6e6c696e65) |
| 6 | `87.248.129.202` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.202&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 7 | `data.proxyvpn.site` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=data.proxyvpn.site&port=443&secret=ee7d75b7a3d02eefad99691681a534c1fe646174612e70726f787976706e2e73697465) |
| 8 | `iran.protocolsix.info` | `25565` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=iran.protocolsix.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 10 | `apex.proxym.world` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=apex.proxym.world&port=443&secret=ee4459d77ba2b570d1a593a478d3cd94a4617065782e70726f78796d2e776f726c64) |
| 11 | `142.132.167.80` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=142.132.167.80&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 12 | `87.248.129.49` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.49&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d) |
| 13 | `node.prx.today` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=node.prx.today&port=443&secret=ee4fc23f27cad414e0ca758692e060323a6e6f64652e7072782e746f646179) |
| 14 | `mtp.nowabst.net` | `853` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtp.nowabst.net&port=853&secret=ee82ce1f84af4033cc7e7b021069be3d5b6164732e78352e7275) |
| 15 | `Gengbeng.etherealvpn.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Gengbeng.etherealvpn.uk&port=443&secret=eec3332fab3d82ff009bc26822e5b7dc84617669746f2e7275) |
| 16 | `billing.mizbanonline.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=billing.mizbanonline.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 17 | `Ehsgh.kon.khoshgele.ir.biobarmesh.info.` | `88` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=Ehsgh.kon.khoshgele.ir.biobarmesh.info.&port=88&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 18 | `get.utkanos.life` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=get.utkanos.life&port=443&secret=ee9657c0f5d3500ab1649000fcd8a0ad816765742e75746b616e6f732e6c696665) |
| 19 | `167.235.201.11` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=167.235.201.11&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b) |
| 20 | `87.248.129.211` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.129.211&port=443&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |


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
