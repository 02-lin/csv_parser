#!/bin/bash

SELF=$(readlink -e "$0")
DIR="${SELF%/*}"

python3 "${DIR}/csv_parser.py" "$@"
