<div align="center">

<table width="100%">
<tr>
<td align="center"><a href="https://github.com/hydraponique/roscomvpn-geoip"><b>🌎 RoscomVPN GeoIP</b></a></td>
<td align="center"><a href="https://github.com/hydraponique/roscomvpn-geosite">RoscomVPN GeoSite</a></td>
<td align="center"><a href="https://github.com/hydraponique/roscomvpn-routing">RoscomVPN Routing</a></td>
</tr>
<tr>
<td align="center"><img src="https://img.shields.io/github/downloads/hydraponique/roscomvpn-geoip/total.svg" alt="Downloads"> <img src="https://data.jsdelivr.com/v1/package/gh/hydraponique/roscomvpn-geoip/badge" alt="jsDelivr"></td>
<td align="center"><img src="https://img.shields.io/github/downloads/hydraponique/roscomvpn-geosite/total.svg" alt="Downloads"> <img src="https://data.jsdelivr.com/v1/package/gh/hydraponique/roscomvpn-geosite/badge" alt="jsDelivr"></td>
<td align="center"><img src="https://img.shields.io/github/stars/hydraponique/roscomvpn-routing.svg" alt="Stars"> <img src="https://img.shields.io/badge/Happ-blue.svg" alt="Happ"> <img src="https://img.shields.io/badge/Mihomo-grey.svg" alt="Mihomo"> <img src="https://img.shields.io/badge/Incy-darkgreen.svg" alt="Incy"></td>
</tr>
</table>

# 🌎 RoscomVPN GeoIP

**Генерирует актуальный `geoip.dat` и рулсеты для Mihomo/sing-box**
**с "хирургической" фильтрацией всех нужных CIDR РФ/РБ**

Три категории: `direct` · `whitelist` · `private`

</div>

---

## 📥 Форматы и скачивание

<details open>
<summary><b>geoip.dat (V2Ray/Xray)</b></summary>

<table width="100%">
<thead><tr><th align="left">Источник</th><th align="left">Ссылка</th></tr></thead>
<tbody>
<tr><td>🔗 GitHub Releases</td><td><a href="https://github.com/hydraponique/roscomvpn-geoip/releases/latest/download/geoip.dat">https://github.com/hydraponique/roscomvpn-geoip/releases/latest/download/geoip.dat</a></td></tr>
<tr><td>⚡ jsDelivr CDN</td><td><a href="https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip/release/geoip.dat">https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip/release/geoip.dat</a></td></tr>
</tbody>
</table>

</details>

<details>
<summary><b>📄 Текстовый формат (CIDR-списки)</b></summary>

<table width="100%">
<thead><tr><th align="left">Файл</th><th align="left">Описание</th></tr></thead>
<tbody>
<tr><td><a href="https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip/release/text/direct.txt">release/text/direct.txt</a></td><td>~15 000+ CIDR для прямой маршрутизации</td></tr>
<tr><td><a href="https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip/release/text/whitelist.txt">release/text/whitelist.txt</a></td><td>~4 000+ CIDR белого списка, обязательная категория</td></tr>
<tr><td><a href="https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip/release/text/private.txt">release/text/private.txt</a></td><td>Приватные адреса</td></tr>
</tbody>
</table>

</details>

<details>
<summary><b>🔶 Mihomo (.mrs рулсеты)</b></summary>

<table width="100%">
<thead><tr><th align="left">Файл</th><th align="left">CDN</th></tr></thead>
<tbody>
<tr><td>direct.mrs</td><td><a href="https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip/release/mihomo/direct.mrs">https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip/release/mihomo/direct.mrs</a></td></tr>
<tr><td>whitelist.mrs</td><td><a href="https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip/release/mihomo/whitelist.mrs">https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip/release/mihomo/whitelist.mrs</a></td></tr>
<tr><td>private.mrs</td><td><a href="https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip/release/mihomo/private.mrs">https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip/release/mihomo/private.mrs</a></td></tr>
</tbody>
</table>

</details>

<details>
<summary><b>🟣 sing-box (.srs рулсеты)</b></summary>

<table width="100%">
<thead><tr><th align="left">Файл</th><th align="left">CDN</th></tr></thead>
<tbody>
<tr><td>direct.srs</td><td><a href="https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip/release/sing-box/direct.srs">https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip/release/sing-box/direct.srs</a></td></tr>
<tr><td>whitelist.srs</td><td><a href="https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip/release/sing-box/whitelist.srs">https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip/release/sing-box/whitelist.srs</a></td></tr>
<tr><td>private.srs</td><td><a href="https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip/release/sing-box/private.srs">https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip/release/sing-box/private.srs</a></td></tr>
</tbody>
</table>

</details>

---

## 🧬 Из чего состоит `geoip:direct`

> [!TIP]
> **Добавлено (ADD):**
> - GeoLite2 + IPinfo + DB-IP — три независимые геобазы всех RU/BY CIDR-диапазонов (IPv4)
> - Кастомный список CIDR — VK Company/Mail.Ru, Yandex, CDNVideo (Билайн), включая зарубежные активы
> - Apple Push Notifications — решение проблем с доставкой пушей на iOS

> [!WARNING]
> **Исключено (DIFF):**
> - Re:filter + Antifilter.Network — списки РКН для разблокировки забаненного сегмента
> - Community-списки — Re:filter + Antifilter.Network + Antifilter.Download (проблемные сервисы: 4pda, CloudFlare и др.)
> - Зарубежные CDN + Hetzner — резолвинг из множества геобаз + оф. информация CDN-провайдеров
> - `0.0.0.0/8` из private — предотвращение утечки DNS на некоторых устройствах

## 🛡 `geoip:whitelist`

- [russia-whitelist](https://github.com/escapingworm/russia-whitelist) — белый список, CIDR
- Кастомный CUSTOM-WHITELIST.txt — IP-диапазоны, которые собраны вручную

---

## 🛠 Использование с Xray/V2Ray

```json
{
  "routing": {
    "rules": [
      {
        "type": "field",
        "ip": ["geoip:direct"],
        "outboundTag": "direct"
      }
    ]
  }
}
```

---

## 📅 Обновления

> Файлы обновляются **ежедневно в 03:10 UTC** и **при любом изменении в репозитории**

---

## 📊 Источники данных

<details open>
<summary><b>Геобазы и списки</b></summary>

<table width="100%">
<thead><tr><th align="left">Источник</th><th align="left">Что дает</th></tr></thead>
<tbody>
<tr><td><a href="https://github.com/sapics/ip-location-db/tree/main/geolite2-country">GeoLite2</a></td><td>RU/BY CIDR из MaxMind</td></tr>
<tr><td><a href="https://github.com/Davoyan/ipinfo">IPinfo</a></td><td>RU/BY CIDR из IPinfo</td></tr>
<tr><td><a href="https://github.com/sapics/ip-location-db/tree/main/dbip-geo-whois-asn-country">DB-IP + GeoFeed + afrinic, apnic, arin, lacnic, ripe ncc</a></td><td>RU/BY CIDR из DB-IP</td></tr>
<tr><td><a href="https://github.com/1andrevich/Re-filter-lists">Re:filter</a></td><td>Списки РКН</td></tr>
<tr><td><a href="https://antifilter.network">Antifilter.Network</a></td><td>Списки РКН</td></tr>
<tr><td><a href="https://antifilter.download">Antifilter.Download</a></td><td>Community-списки</td></tr>
<tr><td><a href="https://github.com/PentiumB/CDN-RuleSet">CDN-RuleSet</a></td><td>CIDR зарубежных CDN</td></tr>
<tr><td><a href="https://github.com/mansourjabin/cdn-ip-database">cdn-ip-database</a></td><td>Парсинг оф. данных CIDR зарубежных CDN</td></tr>
<tr><td><a href="https://github.com/escapingworm/russia-whitelist">russia-whitelist</a></td><td>Белый список CIDR</td></tr>
</tbody>
</table>

</details>

---

## 🔗 Связанные проекты

- [roscomvpn-geosite](https://github.com/hydraponique/roscomvpn-geosite) — доменные списки
- [roscomvpn-routing](https://github.com/hydraponique/roscomvpn-routing) — готовые конфиги роутинга

---

<div align="center">

> **Ставь ⭐** и не пропусти регулярные обновления для поддержания актуальности списков и оптимальной производительности

##### USDT TRC20: TMu3N2ZjK5omJ7n3WAj5MNCSM5querBXsR

##### Спасибо Всем за поддержку!
###### Сделано с ❤️ к свободному интернету!

</div>
