#!/bin/sh
celery -A main_news beat -l info -S django
