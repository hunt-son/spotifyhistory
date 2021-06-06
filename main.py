import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime, timedelta
import os

''' GLOBALS '''
client_id = os.environ['SPOTIPY_CLIENT_ID']
client_secret = os.environ['SPOTIPY_CLIENT_SECRET']
redirect_uri = os.environ['SPOTIPY_REDIRECT_URI']

''' METHODS '''
def formatDate(played_at):
    date = datetime.strptime(played_at, "%Y-%m-%dT%H:%M:%S.%fZ")
    return str(date.month) + "/" + str(date.day) + "/" + str(date.year) + " at " + str(date.hour) + ":00"

def get_most_recently_played_tracks(sp):
    print('------Recently Played------')
    # TODO: this doesn't work yet
    # one_day_ago = datetime.timestamp(datetime.now() - timedelta(days=1))
    one_day_ago = '1622864258'
    results = sp.current_user_recently_played(limit=10, after=one_day_ago)
    for idx, item in enumerate(results['items']):
        track = item['track']
        trackName = track['name']
        artistName = track['artists'][0]['name']
        date = formatDate(item['played_at'])
        print(idx, trackName, " - ", artistName, " - ", date)
    print('---------------------------')

''' MAIN '''
if __name__ == "__main__":
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope="user-library-read user-read-private user-read-playback-state user-read-recently-played"))
    get_most_recently_played_tracks(sp)
