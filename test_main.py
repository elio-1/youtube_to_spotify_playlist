import yt_to_spotify as p
import pytest

def test_create_playlist():
    assert(p.Sp.create_playlist('test playlist')) == "Playlist created"
    with pytest.raises(TypeError):
        p.Sp.create_playlist()

def test_add_songs():
    assert(p.Sp.add_songs(["7rt0kEDWRg3pgTZJKuszoE", "0I3q5fE6wg7LIfHGngUTnV"])) == 'Succes'

