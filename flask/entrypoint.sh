#!/bin/bash

if [[ "$FLASK_ENV" = "development" ]]
then
    echo $FLASK_ENV 
    # cd flask 
    flask run -h 0.0.0.0
elif [[ "$FLASK_ENV" = "production" ]]
then
    echo $FLASK_ENV 
    gunicorn --bind 0.0.0.0:5000 create_app:app # # name of module (-.py) and the callable within the app
fi

exec "$@"

