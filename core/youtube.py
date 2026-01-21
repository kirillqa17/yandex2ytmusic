import os
import json

from tqdm import tqdm
from ytmusicapi import YTMusic, setup_oauth
from ytmusicapi.auth.oauth import OAuthCredentials
from typing import List, Tuple
from .track import Track


class YoutubeImoirter:
    def __init__(self, token_path: str, client_secrets_path: str = None):
        if not client_secrets_path or not os.path.exists(client_secrets_path):
            raise FileNotFoundError(
                "Client secrets file required. "
                "Use --client-secrets to provide path to Google OAuth credentials JSON."
            )

        with open(client_secrets_path, 'r') as f:
            secrets = json.load(f)['installed']

        oauth_credentials = OAuthCredentials(secrets['client_id'], secrets['client_secret'])

        if not os.path.exists(token_path):
            token = setup_oauth(secrets['client_id'], secrets['client_secret']).as_json()
            with open(token_path, 'w') as f:
                f.write(token)

        self.ytmusic = YTMusic(token_path, oauth_credentials=oauth_credentials)

    def import_liked_tracks(self, tracks: List[Track]) -> Tuple[List[Track], List[Track]]:
        not_found: List[Track] = []
        errors: List[Track] = []

        with tqdm(total=len(tracks), position=0, desc='Import tracks') as pbar:
            with tqdm(total=0, bar_format='{desc}', position=1) as trank_log:
                for track in tracks:
                    query = f'{track.artist} {track.name}'

                    try:
                        results = self.ytmusic.search(query, filter='songs')
                    except Exception as e:
                        errors.append(track)
                        pbar.write(f'Search error: {query}, {e}')
                        pbar.update(1)
                        continue

                    if not results:
                        not_found.append(track)
                        pbar.update(1)
                        continue

                    result = self._get_best_result(results, track)
                    try:
                        self.ytmusic.rate_song(result['videoId'], 'LIKE')
                    except Exception as e:
                        errors.append(track)
                        pbar.write(f'Error: {track.artist} - {track.name}, {e}')

                    pbar.update(1)
                    trank_log.set_description_str(f'{track.artist} - {track.name}')

        return not_found, errors
    
    def _get_best_result(self, results: List[dict], track: Track) -> dict:
        songs = []
        for result in results:
            if 'videoId' not in result.keys():
                continue
            if result['category'] == 'Top result':
                return result
            if result['title'] == track.name:
                return result
            songs.append(result)
        if len(songs) == 0:
            return results[0]
        return songs[0]
        
