# DROP TABLES

songplay_table_drop = '''
  DROP TABLE IF EXISTS songplays
'''
user_table_drop = '''
  DROP TABLE IF EXISTS users
'''
song_table_drop = '''
  DROP TABLE IF EXISTS songs
'''
artist_table_drop = '''
  DROP TABLE IF EXISTS artists
'''
time_table_drop = '''
  DROP TABLE IF EXISTS times
'''

# CREATE TABLES

songplay_table_create = ('''
  CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL NOT NULL,
    start_time  BIGINT NOT NULL,
    user_id     TEXT   NULL,
    level       TEXT   NULL,
    song_id     TEXT   NULL, -- always null
    artist_id   TEXT   NULL, -- always null
    session_id  TEXT   NULL,
    location    TEXT   NULL,
    user_agent  TEXT   NULL,

    PRIMARY KEY (songplay_id),
    FOREIGN KEY (user_id)   REFERENCES users   (user_id),
    FOREIGN KEY (song_id)   REFERENCES songs   (song_id),
    FOREIGN KEY (artist_id) REFERENCES artists (artist_id)
  )
''')

user_table_create = ('''
  CREATE TABLE IF NOT EXISTS users (
    user_id    TEXT NOT NULL,
    first_name TEXT NULL,
    last_name  TEXT NULL,
    gender     TEXT NULL,
    level      TEXT NULL,

    PRIMARY KEY (user_id)
  )
''')

song_table_create = ('''
  CREATE TABLE IF NOT EXISTS songs (
    song_id   TEXT    NOT NULL,
    title     TEXT    NULL,
    artist_id TEXT    NOT NULL,
    year      INT     NULL,
    duration  NUMERIC NULL,

    PRIMARY KEY (song_id),
    FOREIGN KEY (artist_id) REFERENCES artists (artist_id)
  )
''')

artist_table_create = ('''
  CREATE TABLE IF NOT EXISTS artists (
    artist_id TEXT NOT NULL,
    name      TEXT,
    location  TEXT,
    latitude  TEXT, -- some null
    longitude TEXT, -- some null

    PRIMARY KEY (artist_id)
  )
''')

time_table_create = ('''
  CREATE TABLE IF NOT EXISTS times (
    start_time BIGINT NOT NULL,
    hour       INT,
    day        INT,
    week       INT,
    month      INT,
    year       INT,
    weekday    INT,

    PRIMARY KEY (start_time)
  )
''')

# INSERT RECORDS

songplay_table_insert = ('''
  INSERT INTO songplays (
    start_time,
    user_id,
    level,
    song_id,
    artist_id,
    session_id,
    location,
    user_agent
  ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
''')

user_table_insert = ('''
  INSERT INTO users (user_id, first_name, last_name, gender, level)
  VALUES (%s, %s, %s, %s, %s)
  ON CONFLICT (user_id)
  DO NOTHING
''')

song_table_insert = ('''
  INSERT INTO songs (song_id, title, artist_id, year, duration)
  VALUES (%s, %s, %s, %s, %s)
  ON CONFLICT (song_id)
  DO NOTHING
''')

artist_table_insert = ('''
  INSERT INTO artists (artist_id, name, location, latitude, longitude)
  VALUES (%s, %s, %s, %s, %s)
  ON CONFLICT (artist_id)
  DO NOTHING
''')

time_table_insert = ('''
  INSERT INTO times (start_time, hour, day, week, month, year, weekday)
  VALUES (%s, %s, %s, %s, %s, %s, %s)
  ON CONFLICT (start_time)
  DO NOTHING
''')

# FIND SONGS

song_select = ('''
  SELECT
    songs.song_id,
    artists.artist_id
  FROM songs
  JOIN artists
  ON
    songs.artist_id = artists.artist_id
  WHERE
    songs.title = %s
  AND
    artists.name = %s
  AND
    songs.duration = %s
''')

# QUERY LISTS

create_table_queries = [
  user_table_create,
  artist_table_create,
  time_table_create,
  song_table_create,
  songplay_table_create
]
drop_table_queries = [
  songplay_table_drop,
  song_table_drop,
  time_table_drop,
  artist_table_drop,
  user_table_drop
]