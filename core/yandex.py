import time
from yandex_music import Client, Artist
from yandex_music.exceptions import TimedOutError
from typing import List
from .track import Track
from tqdm import tqdm


class YandexMusicExporter:
    def __init__(self, token: str):
        self.client = Client(token).init()

    def _fetch_with_retry(self, track, max_retries=5, base_delay=2):
        for attempt in range(max_retries):
            try:
                return track.fetch_track()
            except TimedOutError:
                if attempt < max_retries - 1:
                    delay = base_delay * (2 ** attempt)
                    time.sleep(delay)
                else:
                    raise

    def export_liked_tracks(self) -> List[Track]:
        tracks = self.client.users_likes_tracks().tracks

        result = []
        with tqdm(total=len(tracks), position=0, desc='Export tracks') as pbar:
            with tqdm(total=0, bar_format='{desc}', position=1) as trank_log:
                for track in tracks:
                    track = self._fetch_with_retry(track)
                    # Safely handle the case where there are no artists
                    if track.artists_name():
                        artist = track.artists_name()[0]
                    else:
                        artist = "Unknown Artist"
                    name = track.title
                    result.append(Track(artist, name))
                    pbar.update(1)
                    trank_log.set_description_str(f'{artist} - {name}')
        return result
