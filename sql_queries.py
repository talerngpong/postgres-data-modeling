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
    songplay_id INT,
    start_time  BIGINT,
    user_id     TEXT,
    level       TEXT,
    song_id     TEXT,
    artist_id   TEXT,
    session_id  TEXT,
    location    TEXT,
    user_agent  TEXT
  )
''')

user_table_create = ('''
  CREATE TABLE IF NOT EXISTS users (
    user_id    TEXT,
    first_name TEXT,
    last_name  TEXT,
    gender     TEXT,
    level      TEXT
  )
''')

song_table_create = ('''
  CREATE TABLE IF NOT EXISTS songs (
    song_id   TEXT,
    title     TEXT,
    artist_id TEXT,
    year      INT,
    duration  REAL
  )
''')

artist_table_create = ('''
  CREATE TABLE IF NOT EXISTS artists (
    artist_id  TEXT,
    name       TEXT,
    location   TEXT,
    latitude   TEXT,
    longitude  TEXT
  )
''')

time_table_create = ('''
  CREATE TABLE IF NOT EXISTS times (
    start_time BIGINT,
    hour       INT,
    day        INT,
    week       INT,
    month      INT,
    year       INT,
    weekday    INT
  )
''')

# INSERT RECORDS

songplay_table_insert = ('''
  INSERT INTO songplays (
    songplay_id,
    start_time,
    user_id,
    level,
    song_id,
    artist_id,
    session_id,
    location,
    user_agent
  ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
''')

user_table_insert = ('''
  INSERT INTO users (user_id, first_name, last_name, gender, level)
  VALUES (%s, %s, %s, %s, %s)
''')

song_table_insert = ('''
  INSERT INTO songs (song_id, title, artist_id, year, duration)
  VALUES (%s, %s, %s, %s, %s)
''')

artist_table_insert = ('''
  INSERT INTO artists (artist_id, name, location, latitude, longitude)
  VALUES (%s, %s, %s, %s, %s)
''')

time_table_insert = ('''
  INSERT INTO times (start_time, hour, day, week, month, year, weekday)
  VALUES (%s, %s, %s, %s, %s, %s, %s)
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

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]