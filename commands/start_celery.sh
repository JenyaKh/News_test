#!/bin/sh

celery -A main_news worker -l info -c $CELERY_NUM_WORKERS
