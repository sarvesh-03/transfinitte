#!/bin/sh
until nc -z -v -w30 selenium 4444
do
  echo "Waiting for selenium connection..."
  # wait for 5 seconds before check again
  sleep 5
done

uvicorn src.main:server --host 0.0.0.0 --reload
