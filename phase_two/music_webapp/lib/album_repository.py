from lib.album import Album

class AlbumRepository:
    def __init__(self, connection):
        self.connection = connection
        pass

    def all(self):
        rows = self.connection.execute('SELECT * FROM albums')
        albums = [Album(row['id'], row['title'], row['release_year'], row['artist_id']) for row in rows]
        return albums
    
    def add(self, title, release_year, artist_id):
        self.connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [title, int(release_year), int(artist_id)])