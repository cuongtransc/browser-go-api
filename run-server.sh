#!/bin/bash

source .venv/bin/activate

export CONFIGURATION_OBJECT=configuration.config.DevelopmentConfig
export DATABASE_URL=postgresql://dev:dev123@172.17.0.1/god_of_go
export ALLOWED_ORIGIN='*'

python manage.py runserver
