#!/bin/bash

# There is no `set -e` since this script allow us to continue to next commands in case of abnormal exit code of previous commands.

docker compose down
docker compose up -d --build
