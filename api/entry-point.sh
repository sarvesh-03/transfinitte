#!/bin/sh

uvicorn src.main:server --host 0.0.0.0 --reload
