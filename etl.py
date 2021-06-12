import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *
from datetime import datetime as dt


def process_song_file(cur, filepath):
    '''
    Process a song file by reading and inserting data to song and artist tables

        Parameters:
            cur (psycopg2.extensions.cursor): active DB cursor
            filepath (str): file path pointing to a song file
        
        Returns:
            None
    '''
    # open song file
    df = pd.DataFrame([pd.read_json(filepath, typ='series')])

    # insert artist record
    for artist_data in df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']].values:
        cur.execute(artist_table_insert, artist_data)

    # insert song record
    for song_data in df[['song_id', 'title', 'artist_id', 'year', 'duration']].values:
        cur.execute(song_table_insert, song_data)


def process_log_file(cur, filepath):
    '''
    Process a log file by reading and inserting data to time, user and songplay tables

        Parameters:
            cur (psycopg2.extensions.cursor): active DB cursor
            filepath (str): file path pointing to a log file
        
        Returns:
            None
    '''
    def get_lines_from_file(internal_filepath):
        lines = []
        with open(internal_filepath) as j_file:
            lines = j_file.readlines()
        return lines

    # open log file
    df = pd.DataFrame([
        pd.read_json(line, typ='series')
        for line
        in get_lines_from_file(filepath)
    ])

    # filter by NextSong action
    df = df[df['page'] == 'NextSong']

    # convert timestamp column to datetime
    t = df['ts'].map(
        lambda timestamp: dt.fromtimestamp(timestamp / 1000.0)
    )
    
    # insert time data records
    time_data = zip(
        df['ts'],
        t.dt.hour,
        t.dt.day,
        t.dt.isocalendar().week,
        t.dt.month,
        t.dt.year,
        t.dt.weekday
    )
    column_labels = ['start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday']
    time_df = pd.DataFrame(time_data, columns=column_labels)

    for _, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_data = zip(
        df['userId'],
        df['firstName'],
        df['lastName'],
        df['gender'],
        df['level']
    )
    user_column_labels = ['user_id', 'first_name', 'last_name', 'gender', 'level']
    user_df = pd.DataFrame(user_data, columns=user_column_labels)

    # insert user records
    for _, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for _, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            song_id, artist_id = results
        else:
            song_id, artist_id = None, None

        # insert songplay record
        songplay_data = (
            row['ts'],
            row['userId'],
            row['level'],
            song_id,
            artist_id,
            row['sessionId'],
            row['location'],
            row['userAgent']
        )
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    '''
    Process files on a target path

        Parameters:
            cur (psycopg2.extensions.cursor): active DB cursor
            conn (psycopg2.extensions.connection): active DB connection
            filepath (str): path pointing to a directory storing files to be processed
            func (typing.Callable[[psycopg2.extensions.cursor, str], None]): callback to process one file
        
        Returns:
            None
    '''
    # get all files matching extension from directory
    all_files = []
    for root, _, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    '''
    - Process muliple song_data files by reading and inserting data into song and artist tables
    - Process muliple log_data files by reading and inserting data into time, user and songplay tables
    '''
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
