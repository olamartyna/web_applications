1. Extract nouns from the user stories or specification
artists, name, genre


2. Infer the Table Name and Columns
table name: artists
column names: name, genre


3. Decide the column types
id: SERIAL
name: text
genre: text


4. Write the SQL
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name text,
    genre text
);


5. Create the table
psql -h 127.0.0.1 artists < seeds/artists.sql