import os
from flask import Flask, request
from lib.album_repository import AlbumRepository
from lib.artists_repository import ArtistsRepository
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"


@app.route('/albums', methods=['POST'])
def post_album():
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']

    connection = get_flask_database_connection(app)
    connection.connect()
    repo = AlbumRepository(connection)
    repo.add(title, release_year, artist_id)

    return ''


@app.route('/artists', methods=['GET'])
def get_artists():
    # artists_list = request.args['name']

    connection = get_flask_database_connection(app)
    #connection.connect() 
    repo = ArtistsRepository(connection)
    results = repo.all()
    # We need to turn object into sth readable eg string or list
    artists_names = []
    for result in results:
        artists_names.append(result.name)

    return ', '.join(artists_names)
    

@app.route('/artists', methods=['POST'])
def post_artists():
    
    connection = get_flask_database_connection(app)
    repo = ArtistsRepository(connection)
    
    name = request.form['name']
    genre = request.form['genre']
    repo.add(name, genre)
    return ''


@app.route('/add', methods=['GET'])
def add():
    predefined_names = ['Julia','Alice','Karim']
    names_list = request.args['names']
    names_list_split = names_list.split(',')
    predefined_names.extend(names_list_split)
    return ','.join(predefined_names)

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.


# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

