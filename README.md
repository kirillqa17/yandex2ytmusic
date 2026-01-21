# yandex2ytmusic

**[English](README_EN.md)**

Перенос понравившихся треков из Yandex.Музыка в YouTube Music.

## Интерфейс программы

```bash
python main.py --help
usage: main.py [-h] [--yandex YANDEX] [--output OUTPUT] [--youtube YOUTUBE] [--client-secrets CLIENT_SECRETS]

Transfer tracks from Yandex.Music to YouTube Music

options:
  -h, --help            show this help message and exit
  --yandex YANDEX       Yandex Music token
  --output OUTPUT       Output json file
  --youtube YOUTUBE     Youtube Music credentials file. If file not exists, it will be created.
  --client-secrets CLIENT_SECRETS
                        Path to Google OAuth client secrets JSON file (required for first-time setup)
```

## Использование

### 1. Получить Yandex Music токен

[Получить Yandex Music token](https://yandex-music.readthedocs.io/en/main/token.html). Легче всего это сделать с помошью приложения.

### 2. Получить Google OAuth credentials

1. Перейти в [Google Cloud Console](https://console.cloud.google.com/)
2. Создать новый проект или выбрать существующий
3. Перейти в **APIs & Services** → **Library**
4. Найти **YouTube Data API v3** и нажать **Enable**
5. Перейти в **APIs & Services** → **OAuth consent screen**
   - Выбрать **External** и создать
   - Заполнить обязательные поля (название приложения, email)
   - В разделе **Test users** добавить email вашего Google аккаунта
6. Перейти в **APIs & Services** → **Credentials**
7. Нажать **Create Credentials** → **OAuth client ID**
8. Выбрать тип приложения: **TVs and Limited Input devices**
9. Скачать JSON файл с credentials

### 3. Запустить программу

```bash
pip install -r requirements.txt
python main.py --yandex <Yandex Music token> --client-secrets <path to Google OAuth JSON>
```

### 4. Авторизация в YouTube Music

При запуске программы перейти по предложенной ссылке, ввести код из терминала и разрешить доступ к аккаунту.
4. Дождаться завершения работы программы. Программа также экспортирует музыку Json в файл:

```json
{
    // понравившиеся треки в Yandex Music
    "liked_tracks":[
        {
            "artist": "Исполнитнль",
            "name": "Название трека"
        }
    ],
    // треки, которые не были найдены при переносе
    "not_found":[], 
    // треки, при переносе которых произошла ошибка
    "errors":[]
}
```

## Используемые ресурсы

- yandex-music - не официальное python API Yandex.Music
- ytmusicapi - не официальное python API YouTube Music

### P.s.

Написал этот скрипт, так как не нашел ничего подобного в сети.
Буду рад pull реквестам и звездочкам :-)

