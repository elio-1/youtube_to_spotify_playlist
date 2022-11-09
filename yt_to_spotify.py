import spotipy
from spotipy.oauth2 import SpotifyOAuth
import env


class Sp:
    scope = "playlist-modify-public"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=env.Env.spotipy_client_id, client_secret=env.Env.spotipy_client_secret, redirect_uri="https://localhost:8888/callback",scope=scope
        ))

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
        """ Search for a song. Return the first value matching the artist name of track name """
        return cls.sp.search(q=song, type="track", limit=1)['tracks']['items'][0]['id']

    def playlist_id(cls):
        return cls.sp.current_user_playlists()["items"][0]["id"]

    def user(cls):
        return cls.sp.current_user()["id"]


def main():
    search_list = manual_input_search()     
    Sp.create_playlist("test playlist")
    tracks = []
    for song in search_list:
        tracks.append(Sp.search_song(song))
    Sp.add_songs(tracks)


def manual_input_search():
    search_list=[]
    while True:
        user_input = str(input('Search for songs: '))
        if user_input == '-stop':
            break
        search_list.append(user_input)
        esign = '=' * 8
        blank = ' ' * 4
        print('\n' + esign + blank + "Song added to the list" + blank + esign)
        print(esign + blank + 'Current list:' + blank + esign + '\n')
        for item in search_list:
            print(item)
        print('\ntype "-stop" to end the list\n')
    return search_list


if __name__ == "__main__":
    main()
