#!/bin/sh

# Wait for database to be available (if using DB)
#while ! nc -z $DB_HOST $DB_PORT; do
#  sleep 0.1
#done

# Run migrations
python manage.py makemigrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput


# Create superuser if credentials are provided
if [ "$DJANGO_SUPERUSER_USERNAME" ] && [ "$DJANGO_SUPERUSER_EMAIL" ] && [ "$DJANGO_SUPERUSER_PASSWORD" ]; then
    python manage.py createsuperuser \
        --noinput \
        --username "$DJANGO_SUPERUSER_USERNAME" \
        --email "$DJANGO_SUPERUSER_EMAIL"
    echo "Superuser created"
fi

# Start server
exec "$@"
