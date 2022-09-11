#!/bin/bash

set -e

if [ -z $JOB_CMD ]; then
  uvicorn src.main:app --reload --host=0.0.0.0 --port 8000
else
  python src/$JOB_CMD.py $JOB_PARAM
fi

exec "$@"
