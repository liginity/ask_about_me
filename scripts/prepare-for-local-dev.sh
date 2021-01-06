#!/bin/bash

## after starting the container using `docker-compose`, run this with
## `docker exec -it askaboutmeweb bash scripts/prepare-for-local-dev.sh`
python3 manage.py makemigrations askaboutme \
    && python3 manage.py migrate \
    && python3 manage.py collectstatic --no-input

python3 manage.py createsuperuser
