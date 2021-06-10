# ETL for Song Play Analysis

This project aims to transform raw song play data and load them into traditional database, in this case, Postgres for later analysis. This is also used to satisfied with `Data Modeling with Postgres` project under [Data Engineer Nanodegree Program](https://www.udacity.com/course/data-engineer-nanodegree--nd027).

## Prerequisite
- conda
- Docker
- dataset gathered from [Million Song Dataset](https://labrosa.ee.columbia.edu/millionsong/)

## Local Setup
1. Bootstrap Python and dependencies
   ```bash
   $ ./bootstrap_env_via_conda.sh
   ```
2. Spin up localized instance of Postgres DB
   ```bash
   $ ./respawn_db.sh
   ```
3. Initialize related tables
   ```bash
   $ python ./create_tables.py
   ```
4. place dataset under `./data` directory

## Running ETL
```bash
$ python etl.py
```

## Verifying ETL Result
```bash
$ jupyter notebook

# then walk through `test.ipynb` notebook
```

## Note
- In case of something wrong in local database, use `respawn_db.sh` to re-initialize new one.
