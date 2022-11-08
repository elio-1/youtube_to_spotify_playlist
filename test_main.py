import yt_to_spotify as p
import pytest

def test_create_playlist():
    assert(p.Sp.create_playlist('test playlist')) == "Playlist created"
    with pytest.raises(TypeError):
        p.Sp.create_playlist()

def test_add_songs():
    assert(p.Sp.add_songs(["1pAyyxlkPuGnENdj4g7Y4f", "7D2xaUXQ4DGY5JJAdM5mGP"])) == 'Succes'