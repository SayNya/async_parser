#!/bin/bash

celery -A src.celery.celery beat --loglevel=INFO
