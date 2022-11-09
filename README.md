# Youtube to Spotify Playlist


Export a Youtube playlist to a Spotify playlist

## Installation

This program uses Spotipy (https://github.com/spotipy-dev/spotipy/tree/2.19.0) and google api (https://developers.google.com/apis-explorer/)

```sh
pip install spotipy --upgrade
pip install --upgrade google-api-python-client
```

You're going to need a SPOTIPY_CLIENT_ID, a SPOTIPY_CLIENT_SECRET and a youtube api key
In the program I used a reference to another file containing the keys so that I didn't had to put them for the world to see and so I didn't had to set up environnement variable everytime.


```python
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=env.Env.spotipy_client_id, # CHANGE THIS with your SPOTIPY_CLIENT_ID
        client_secret=env.Env.spotipy_client_secret, # CHANGE THIS with your SPOTIPY_CLIENT_SECRET
        redirect_uri="https://localhost:8888/callback",
        scope=scope,
    )
)
```
You can also set them up in you environement variable. More at https://spotipy.readthedocs.io/en/2.19.0/#quick-start

For the youtube key replace the value

```python
DEVELOPER_KEY = env.Env.youtube_api_key # CHANGE THIS with your youtube api key
```
Set up your api key https://console.cloud.google.com/apis/credentials


## Usage example

This program is designed to be used with the cli, but I would like to implement it in a web app later.
To use it once you've met the requirement run
```sh
python yt_to_spotify.py
```

Then you are going to get prompt for a playlist link and a playlist name. Make sure you're on the playlist page and not in a song in the playlist.

For exemple:
```sh
Youtube Playlist link: https://www.youtube.com/playlist?list=PLUPHnZCcc6vnJiWOT3DNVA4Uj_VMXWP9T
Playlist name: My Playlist
```