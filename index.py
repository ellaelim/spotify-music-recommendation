import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import matplotlib.pyplot as plt

CLIENT_ID = '4437a19c48044355847d517607224ab6'
CLIENT_SECRET = '9e16f92331294179a4d2d6b8bd48e26c'
URI = 'http://localhost:8080'

def spotify_authenticate(client_id, client_secret, redirect_uri):
    scope = "user-top-read"
    return spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                     client_secret=client_secret,
                                                     redirect_uri=redirect_uri,
                                                     scope=scope))

def get_user_top_tracks(sp, limit=5):
    top_tracks = sp.current_user_top_tracks(limit=limit)['items']
    return [track['id'] for track in top_tracks]


def get_song_recommendations(sp, seed_tracks, limit=5):
    recommendations = sp.recommendations(seed_tracks=seed_tracks, limit=limit)['tracks']
    return [(track['name'], track['artists'][0]['name']) for track in recommendations]

def main():
    sp = spotify_authenticate(CLIENT_ID, CLIENT_SECRET, URI)

    # Get the user's top tracks as seed tracks for recommendations
    seed_tracks = get_user_top_tracks(sp)
    if not seed_tracks:
        print("No top tracks available for seed data.")
        return

    # Fetch and display recommendations
    recommendations = get_song_recommendations(sp, seed_tracks)
    print("\nRecommended Songs:")
    for track, artist in recommendations:
        print(f"{track} by {artist}")



if __name__ == "__main__":
    main()
