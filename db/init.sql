-- This prepares default database and credentials refered to `create_tables.py` script

DROP DATABASE IF EXISTS studentdb;
CREATE DATABASE studentdb;

CREATE USER student WITH SUPERUSER PASSWORD 'student';
