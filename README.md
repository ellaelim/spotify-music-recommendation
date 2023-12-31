# Spotify Music Recommendation and Analysis 

## Description
This Python application uses the Spotify API to offer personalized music recommendations and analyzes users' listening habits. It allows users to get their top tracks from Spotify and get recommendations for new songs based on their music preferences.

## Features
- Retrieve and display the user's top tracks from Spotify.
- Provide song recommendations based on the user's top tracks.
- Basic data analysis and visualization of the user's music preferences.

## Installation

### Prerequisites
- Python 3.x
- A Spotify account and Spotify Developer credentials (Client ID, Client Secret, and Redirect URI).

### Setup
1. Clone or download this repository to your computer.
2. Install required Python packages:
3. Set up your Spotify Developer credentials:
- Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
- Create a new application to obtain your Client ID and Client Secret.
- Set the Redirect URI in your application settings.

### Configuration
- Open `keys.csv` in a text editor.
- Replace `'CLIENT_ID'` and `'CLIENT_SECRET'` with your actual Spotify Developer credentials.

## Usage
Run the script from the command line:
```
python index.py
```
Follow the on-screen instructions to authenticate and view your top tracks and song recommendations.

## License
[MIT License](LICENSE)
