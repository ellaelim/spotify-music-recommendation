import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import matplotlib.pyplot as plt
import re
import requests
from bs4 import BeautifulSoup

REDIRECT_URI = "http://localhost:8080"
df = pd.read_csv('./keys.csv')
CLIENT_ID, CLIENT_SECRET = tuple(df[df['KEY'] == 'CLIENT_ID']['VALUE'])[0], tuple(df[df['KEY'] == 'CLIENT_SECRET']['VALUE'])[0]


api_settings = ('user-top-read', 5)
scope, limit = api_settings

def spotify_authenticate(client_id, client_secret, redirect_uri):
    return spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                     client_secret=client_secret,
                                                     redirect_uri=redirect_uri,
                                                     scope=scope))

# Replace with your Spotify app credentials
def print_track_details(track):
    print("Track Details:")
    # Print nice readable columns for track details
    print(f"Track ID: {track['id']}")
    print(f"Track Name: {track['name']}")
    print(f"Artist(s): {', '.join([artist['name'] for artist in track['artists']])}")
    print(f"Album: {track['album']['name']}")
    print(f"Popularity: {track['popularity']}")
    print(f"Duration: {track['duration_ms']} ms")

def extract_info_from_track_title(title):
    pattern = r'^(.*?) - (.*?)$'  # Pattern to extract 'song name - artist'
    match = re.search(pattern, title)
    if match:
        return match.groups()
    return title, "Unknown Artist"

def get_user_top_tracks(sp, limit=5):
    top_tracks = sp.current_user_top_tracks(limit=limit)['items']
    return [track['id'] for track in top_tracks]


def get_song_recommendations(sp, seed_tracks, limit=5):
    recommendations = sp.recommendations(seed_tracks=seed_tracks, limit=limit)['tracks']
    return [(track['name'], track['artists'][0]['name']) for track in recommendations]

def main():
    sp = spotify_authenticate(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)

    # Get the user's top tracks as seed tracks for recommendations
    seed_tracks = get_user_top_tracks(sp, limit=limit)  # using the limit from the tuple
    if not seed_tracks:
        print("No top tracks available for seed data.")
        return

    # Fetch and display recommendations
    recommendations = get_song_recommendations(sp, seed_tracks)
    
    # Create a Pandas DataFrame of recommendations
    df = pd.DataFrame(recommendations, columns=['Song', 'Artist'])
    print(df)

    # Example of using regex to extract info from the first track title (if available)
    if recommendations:
        song, artist = extract_info_from_track_title(recommendations[0][0])
        print(f"Extracted Info - Song: {song}, Artist: {artist}")

    # Iterating through a sample track's details (if available)
    if seed_tracks:
        sample_track = sp.track(seed_tracks[0])
        print_track_details(sample_track)

    # Create a bar chart of recommendation frequencies
    df['Artist'].value_counts().plot(kind='barh')
    plt.title('Artist Frequency in Recommendations')
    plt.xlabel('Frequency')
    plt.ylabel('Artist')
    plt.show()

if __name__ == "__main__":
    main()
