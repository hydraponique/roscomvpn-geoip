# 🌎 RoscomVPN GeoIP

### Генерирует самую актуальную базу данных **российских, белорусских и казахстанских IP-адресов** в формате `geoip.dat`, предназначенную для использования в **Xray-core** и **V2Ray-core**.

#### Добавлены диапазоны IP-адресов:
- **VK Company** (VK, Mail.Ru, OK, My.Games и т.д) - категория `direct`
- **Yandex** (Яндекс, Yandex.Cloud, Yandex.Disk и т.д) - категория `direct`
- **Discord** - категория `proxy`
- **Threema** - категория `proxy`

#### Удалено:
- Все остальные гео-категории из основной репы V2Ray.

## 📥 **Статические ссылки на latest версию**  
https://github.com/hydraponique/roscomvpn-geoip/releases/latest/download/geoip.dat

https://cdn.jsdelivr.net/gh/hydraponique/roscomvpn-geoip@release/geoip.dat

## 📅 Обновления
Файл **обновляется каждый четверг** и **при внесении любого изменения в данный репозиторий**

## 🛠 Использование с Xray/V2Ray
Добавьте правила `geoip:proxy` и `geoip:direct` в конфигурацию Xray/V2Ray, чтобы **направлять нужный трафик через прокси или напрямую**:

```json
{
  "routing": {
    "rules": [
      {
        "type": "field",
        "ip": [
          "geoip:direct"
        ],
        "outboundTag": "direct"
      },
      {
        "type": "field",
        "ip": [
          "geoip:proxy"
        ],
        "outboundTag": "proxy"
      }
    ]
  }
}
```
