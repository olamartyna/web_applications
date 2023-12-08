DROP TABLE IF EXISTS artists;
DROP SEQUENCE IF EXISTS artists_id_seq;

CREATE SEQUENCE IF NOT EXISTS artists_id_seq;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name text,
    genre text
);

-- Finally, we add any artists that are needed for the tests to run
INSERT INTO artists(name, genre) VALUES ('Pixies', 'Rock');
INSERT INTO artists(name, genre) VALUES ('ABBA', 'Pop');
INSERT INTO artists(name, genre) VALUES ('Taylor Swift', 'Rap');
INSERT INTO artists(name, genre) VALUES ('Nina Simone', 'Jazz');