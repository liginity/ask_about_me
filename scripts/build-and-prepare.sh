#!/bin/bash

## run the script at the project root with
## bash ./scripts/build-and-prepare.sh

CURRENT_UID=$(id -u):$(id -g) docker-compose -f local_dev.yml build
