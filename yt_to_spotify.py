import spotipy
from spotipy.oauth2 import SpotifyOAuth
import env
import googleapiclient.discovery
import re



class Sp:
    scope = "playlist-modify-public"
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    except spotipy.oauth2.SpotifyOauthError:
        sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=env.Env.spotipy_client_id,
                client_secret=env.Env.spotipy_client_secret,
                redirect_uri="https://localhost:8888/callback",
                scope=scope,
            )
        )

    @classmethod
    def create_playlist(cls, name):
        """Create a playlist with a given name"""
        cls.sp.user_playlist_create(Sp.user(cls), name)
        return "Playlist created"

    @classmethod
    def add_songs(cls, tracks):
        """Add a song or a list of songs to the playlist"""
        cls.sp.playlist_add_items(Sp.playlist_id(cls), tracks, position=None)
        return "Succes"

    @classmethod
    def search_song(cls, song):
        """Search for a song. Return the first value matching the artist name of track name"""
        return cls.sp.search(q=song, type="track", limit=1)["tracks"]["items"][0]["id"]

    def playlist_id(cls):
        return cls.sp.current_user_playlists()["items"][0]["id"]

    def user(cls):
        return cls.sp.current_user()["id"]


def main():
    search_list = list_of_playlist(user_playlist_link())
    Sp.create_playlist(ask_user_playlist_name())
    tracks = []
    for song in search_list:
        tracks.append(Sp.search_song(song))
    Sp.add_songs(tracks)


def user_playlist_link():
    url = input('Youtube Playlist link:')
    match = re.search(
    # r"(?:http:|https:)*?\/\/(?:www\.|)(?:youtube\.com|m\.youtube\.com|youtu\.|youtube-nocookie\.com).*(?:v=|v%3D|v\/|(?:a|p)\/(?:a|u)\/\d.*\/|watch\?|vi(?:=|\/)|\/embed\/|oembed\?|be\/|e\/)([^&?%#\/\n]*)", # credit: https://github.com/rodrigoborgesdeoliveira
    r"(?:http:|https:)*?\/\/(?:www\.|)(?:youtube\.com|m\.youtube\.com|youtu\.|youtube-nocookie\.com).*(?:list=|v%3D|v\/|(?:a|p)\/(?:a|u)\/\d.*\/|list\?|vi(?:=|\/)|\/embed\/|oembed\?|be\/|e\/)([^&?%#\/\n]*)",
    url,
    )
    return match.group(1)


def ask_user_playlist_name():
    return input('Playlist name: ')


def list_of_playlist(playlist_id):
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = env.Env.youtube_api_key

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY
    )

    request = youtube.playlistItems().list(
        part="snippet,contentDetails", 
        maxResults=200,
        playlistId=playlist_id
    )
    response = request.execute()
    playlist_songs = []
    for item in response["items"]:
        if item["snippet"]['title'] != 'Deleted video':
            playlist_songs.append(item["snippet"]['title'])
    return playlist_songs 

if __name__ == "__main__":
    main()