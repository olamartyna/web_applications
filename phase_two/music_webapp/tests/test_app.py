from lib.album_repository import AlbumRepository
from lib.album import Album

from lib.artists_repository import ArtistsRepository
from lib.artists import Artists
# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===


def test_post_album(web_client, db_connection):
    db_connection.seed('seeds/music_webapp.sql')
    response = web_client.post("/albums", data={'title': 'Voyage', 'release_year': '2022', 'artist_id': '2'})
    
    assert response.status_code == 200

    album_repo = AlbumRepository(db_connection)
    albums = album_repo.all()

    assert albums == [Album(1, 'Voyage', 2022, 2)]



def test_get_artists(web_client, db_connection):
    db_connection.seed('seeds/artists.sql')
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == 'Pixies, ABBA, Taylor Swift, Nina Simone'


def test_post_artist(web_client, db_connection):
    db_connection.seed('seeds/artists.sql')
    response = web_client.post('/artists', data={'name': 'Wild nothing', 'genre': 'Indie'})
    assert response.status_code == 200    
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == 'Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing' 



def test_get_add_names_with_list_of_names(web_client):
    response = web_client.get('/add?names=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia,Alice,Karim,Eddie'