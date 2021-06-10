FROM postgres:latest

EXPOSE 5432

ENV POSTGRES_PASSWORD postgres_password

# used as `Initialization scripts` (https://hub.docker.com/_/postgres)
COPY ./init.sql /docker-entrypoint-initdb.d/
