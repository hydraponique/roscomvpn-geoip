# RoscomVPN GeoIP

Генерирует актуальный `geoip.dat` и рулсеты для Mihomo/sing-box с "хирургической" фильтрацией всех нужных CIDR РФ/РБ.

Три категории: **direct** (маршрутизация напрямую), **whitelist** (белый список), **private** (приватные адреса).

---

## Из чего состоит `geoip:direct`

**Добавлено (ADD):**
- GeoLite2 + IPinfo + DB-IP — три независимые геобазы всех RU/BY CIDR-диапазонов (IPv4)
- Кастомный список CIDR — VK Company/Mail.Ru, Yandex, CDNVideo (Билайн), включая зарубежные активы
- Apple Push Notifications — решение проблем с доставкой пушей на iOS

**Исключено (DIFF):**
- Re:filter + Antifilter.Network — списки РКН для разблокировки забаненного сегмента
- Community-списки — Re:filter + Antifilter.Network + Antifilter.Download (проблемные сервисы: 4pda, CloudFlare и др.)
- Зарубежные CDN + Hetzner — резолвинг из множества геобаз + оф. информация CDN-провайдеров
- `0.0.0.0/8` из private — предотвращение утечки DNS на некоторых устройствах

## `geoip:whitelist`

- [russia-whitelist](https://github.com/escapingworm/russia-whitelist) — белый список, CIDR
- Кастомный CUSTOM-WHITELIST.txt — IP-диапазоны, которые собраны вручную

---

## Форматы и скачивание

### geoip.dat (V2Ray/Xray)

| Источник | Ссылка |
|----------|--------|
| GitHub Releases | https://github.com/hydraponique/roscomvpn-geoip/releases/latest/download/geoip.dat |
| jsDelivr CDN | `https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip/release/geoip.dat` |

### Текстовый формат (CIDR-списки)

| Файл | Описание |
|------|----------|
| `release/text/direct.txt` | ~15 000+ CIDR для прямой маршрутизации |
| `release/text/whitelist.txt` | ~4 000+ CIDR белого списка, обязательная категория |
| `release/text/private.txt` | Приватные адреса |

### Mihomo (.mrs рулсеты)

| Файл | CDN |
|------|-----|
| `direct.mrs` | `https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip/release/mihomo/direct.mrs` |
| `whitelist.mrs` | `https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip/release/mihomo/whitelist.mrs` |
| `private.mrs` | `https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip/release/mihomo/private.mrs` |

### sing-box (.srs рулсеты)

| Файл | CDN |
|------|-----|
| `direct.srs` | `https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip/release/sing-box/direct.srs` |
| `whitelist.srs` | `https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip/release/sing-box/whitelist.srs` |
| `private.srs` | `https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip/release/sing-box/private.srs` |

---

## Обновления

Файлы обновляются **ежедневно в 03:10 UTC** и **при любом изменении в репозитории**.

---

## Использование с Xray/V2Ray

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

## Источники данных

| Источник | Что дает |
|----------|----------|
| [GeoLite2](https://github.com/sapics/ip-location-db/tree/main/geolite2-country) | RU/BY CIDR из MaxMind |
| [IPinfo](https://github.com/Davoyan/ipinfo) | RU/BY CIDR из IPinfo |
| [DB-IP + GeoFeed + afrinic, apnic, arin, lacnic, ripe ncc](https://github.com/sapics/ip-location-db/tree/main/dbip-geo-whois-asn-country) | RU/BY CIDR из DB-IP |
| [Re:filter](https://github.com/1andrevich/Re-filter-lists) | Списки РКН |
| [Antifilter.Network](https://antifilter.network) | Списки РКН |
| [Antifilter.Download](https://antifilter.download) | Community-списки |
| [CDN-RuleSet](https://github.com/PentiumB/CDN-RuleSet) | CIDR зарубежных CDN |
| [cdn-ip-database](https://github.com/mansourjabin/cdn-ip-database) | Парсинг оф. данных CIDR зарубежных CDN |
| [russia-whitelist](https://github.com/escapingworm/russia-whitelist) | Белый список CIDR |

## Связанные проекты

- [roscomvpn-geosite](https://github.com/hydraponique/roscomvpn-geosite) — доменные списки
- [roscomvpn-routing](https://github.com/hydraponique/roscomvpn-routing) — готовые конфиги роутинга

---

> **Ставь ⭐** и не пропусти регулярные обновления для поддержания актуальности списков и оптимальной производительности

##### USDT TRC20: TMu3N2ZjK5omJ7n3WAj5MNCSM5querBXsR

##### Спасибо Всем за поддержку!
###### Сделано с ❤️ к свободному интернету!
