# 🌎 RoscomVPN GeoIP

### Генерирует самую актуальную базу данных **российских, белорусских и казахстанских IP-адресов** в формате `geoip.dat`, предназначенную для использования в **Xray-core** и **V2Ray-core**.

#### Добавлены диапазоны IP-адресов:
- **VK Company** (VK, Mail.Ru, OK, My.Games и т.д) - обновлены категории "ru", "by", "kz"
- **Yandex** (Яндекс, Yandex.Cloud, Yandex.Disk и т.д) - обновлены категории "ru", "by", "kz"
- **Discord** (добавлять в proxy, ибо заблокирован в РФ) - добавлена новая категория "discord"
- **Threema** (добавлять в proxy, ибо заблокирован в РФ) - добавлена новая категория "threema"

#### Удалено:
- Все остальные гео-категории, отличные от: "ru", "by", "kz", "discord", "threema", "private", "test".

## 📥 **Скачать последнюю версию**  
[**geoip.dat (cтатическая ссылка)**](https://github.com/hydraponique/roscomvpn-geoip/releases/latest/download/geoip.dat)

## 📅 Обновления
Файл **обновляется каждый четверг** и **при внесении любого изменения в данный репозиторий**

## 🛠 Использование с Xray/V2Ray
Добавьте правило в конфигурацию Xray/V2Ray, чтобы **направлять нужный трафик через определённый прокси или напрямую**:

```json
{
  "routing": {
    "rules": [
      {
        "type": "field",
        "ip": [
          "geoip:ru",
          "geoip:by",
          "geoip:kz"
        ],
        "outboundTag": "direct"
      },
      {
        "type": "field",
        "ip": [
          "geoip:discord",
          "geoip:threema"
        ],
        "outboundTag": "proxy"
      }
    ]
  }
}
```
