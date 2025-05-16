#!/bin/bash


if [ -f .env ]; then
  source .env
fi

echo "Database host is: ${DB_HOST}"

# Exit immediately if a command exits with a non-zero status
set -e

		# Function to log messages with timestamps
log() {
    echo "$(date +"%Y-%m-%d %H:%M:%S") - $1"
}

# Wait for the database to be ready
log "Checking database readiness..."
while ! nc -z ${DB_HOST} ${DB_PORT}; do
    log "Database is not ready. Retrying in 2 seconds..."
    sleep 2
done
log "Database is ready!"


log "Running makemigrations for specified apps..."
python manage.py makemigrations accounts notify business transaction manager 

log "Running migrate to apply database changes..."
python manage.py migrate

# Collect static files
log "Collecting static files..."
python manage.py collectstatic --noinput


log "Starting server..."
# exec uvicorn config.asgi:application \
#     --host ${APP_HOST} \
#     --port ${APP_PORT} \
#     --workers ${GUNICORN_WORKERS} \
#     --timeout-keep-alive ${GUNICORN_TIMEOUT} \
#     --reload

python manage.py runserver ${APP_HOST}:${APP_PORT}
