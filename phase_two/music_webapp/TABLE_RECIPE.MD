# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)


1. Extract nouns from the user stories or specification
albums, title, release_year, artist_id


2. Infer the Table Name and Columns
table name: albums
column names: title, release_year, artist_id


3. Decide the column types
id: SERIAL
title: text
release_year: int
artist_id: int


4. Write the SQL
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int,
    artist_id int
);


5. Create the table
psql -h 127.0.0.1 music_webapp < music_webapp.sql