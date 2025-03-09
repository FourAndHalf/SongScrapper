#!/bin/bash

set -e

# Function to check if required environment variables are set
check_env_var() {
    if [ -z "${!1}" ]; then
        echo "Error: $1 environment variable is not set"
        exit 1
    fi
}

# Load environment variables
if [ -f .env ]; then
    echo "Loading environment variables from .env file..."
    set -a
    source .env
    set +a
else
    echo "Warning: .env file not found"
fi

# Default port if not set
PORT=${PORT:-8000}

# Check required environment variables
check_env_var "SECRET_KEY"
check_env_var "DATABASE_URL"

echo "Starting deployment process..."

# Install required packages
echo "Installing required packages..."
pip install -r requirements.txt

# Run database migrations
echo "Running database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start Gunicorn with proper configuration
echo "Starting Gunicorn server on port $PORT..."
exec gunicorn SpotifyDownloader.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 3 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - \
    --log-level info
