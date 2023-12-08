from lib.artists import Artists

class ArtistsRepository:
    def __init__(self, connection):
        self.connection = connection
        pass

    def all(self):
        rows = self.connection.execute('SELECT * FROM artists')
        artists = [Artists(row['id'], row['name'], row['genre']) for row in rows]
        return artists 
    
    def add(self,name,genre):
        self.connection.execute('INSERT INTO artists (name, genre) VALUES (%s, %s)', [name, genre])