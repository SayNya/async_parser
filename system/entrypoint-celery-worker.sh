#!/bin/bash

celery -A src.celery.celery worker --loglevel=INFO
