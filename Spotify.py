import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = 'b3d0c498523741b2ad02f45477f3ee01'
secret = 'b0f61d30d74d4b039287f8af526e5fc5'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

artist_name = []
track_name = []
popularity = []
track_id = []
for i in range(0,50,50):
    track_results = sp.search(q='year:2018', type='track', limit=50,offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        print(t['artists'][0]['name'])
        print(t['name'])
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])
