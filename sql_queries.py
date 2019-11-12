# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL,
    start_time TIMESTAMP,
    user_id INT REFERENCES users(user_id),
    level VARCHAR,
    song_id VARCHAR REFERENCES songs(song_id),
    artist_id VARCHAR REFERENCES artists(artist_id),
    session_id INT,
    location VARCHAR,
    user_agent VARCHAR,
    PRIMARY KEY(songplay_id)
)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id INT,
    first_name VARCHAR,
    last_name VARCHAR,
    gender VARCHAR(1),
    level VARCHAR,
    PRIMARY KEY(user_id)
)
""")


# This should be the songs table. artist_id should be a foreign key referencing the artsits TABLE. However, it would cause a problem since the ETL templete inserts rows into the songs table before the artists table. 
# song_table_create = ("""
# CREATE TABLE IF NOT EXISTS songs (
#     song_id VARCHAR,
#     title VARCHAR,
#     artist_id VARCHAR REFERENCES artists(artist_id),
#     year INT,
#     duration FLOAT,
#     PRIMARY KEY(song_id)
# )
# """)

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id VARCHAR,
    title VARCHAR,
    artist_id VARCHAR,
    year INT,
    duration FLOAT,
    PRIMARY KEY(song_id)
)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id VARCHAR,
    name VARCHAR,
    location VARCHAR,
    longitude FLOAT,
    latitude FLOAT,
    PRIMARY KEY(artist_id)
)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time TIMESTAMP,
    hour SMALLINT NOT NULL,
    day SMALLINT NOT NULL,
    week SMALLINT NOT NULL,
    month SMALLINT NOT NULL,
    year SMALLINT NOT NULL,
    weekday SMALLINT NOT NULL,
    PRIMARY KEY(start_time)
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level
""")

song_table_insert = ("""
INSERT INTO songs VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""
INSERT INTO artists VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
""")


time_table_insert = ("""
INSERT INTO time VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT(start_time) DO NOTHING
""")

# FIND SONGS

song_select = ("""
SELECT S.song_id, S.artist_id FROM songs S JOIN artists A ON S.artist_id = A.artist_id WHERE title = %s AND name = %s AND duration = %s 
""")

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]