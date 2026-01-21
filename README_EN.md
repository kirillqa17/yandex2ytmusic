# yandex2ytmusic

**[Русский язык](README.md)**

Transfer liked tracks from Yandex.Music to YouTube Music.

## Program Interface

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

## Usage

### 1. Get Yandex Music token

[Get Yandex Music token](https://yandex-music.readthedocs.io/en/main/token.html). It is easiest to do this with the application.

### 2. Get Google OAuth credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Go to **APIs & Services** → **Library**
4. Find **YouTube Data API v3** and click **Enable**
5. Go to **APIs & Services** → **OAuth consent screen**
   - Select **External** and create
   - Fill in required fields (app name, email)
   - In the **Test users** section, add your Google account email
6. Go to **APIs & Services** → **Credentials**
7. Click **Create Credentials** → **OAuth client ID**
8. Select application type: **TVs and Limited Input devices**
9. Download the JSON credentials file

### 3. Run the program

```bash
pip install -r requirements.txt
python main.py --yandex <Yandex Music token> --client-secrets <path to Google OAuth JSON>
```

### 4. YouTube Music authorization

When starting the program, follow the provided link, enter the code from the terminal, and allow access to the account.
4. Wait for the program to finish. The program will also export music data to a JSON file:

```json
{
    // liked tracks in Yandex Music
    "liked_tracks":[
        {
            "artist": "Artist",
            "name": "Track Name"
        }
    ],
    // tracks not found during transfer
    "not_found":[], 
    // tracks that encountered an error during transfer
    "errors":[]
}
```

## Resources Used

- yandex-music - unofficial python API for Yandex.Music
- ytmusicapi - unofficial python API for YouTube Music

### P.S.

I wrote this script because I couldn't find anything similar online.
I'll be happy with pull requests and stars :-)
