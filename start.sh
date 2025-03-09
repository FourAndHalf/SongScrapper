#!/bin/bash

set -e

# Function to check if required environment variables are set
check_env_var() {
    if [ -z "${!1}" ]; then
        echo "Error: $1 environment variable is not set"
        exit 1
    fi
}

# Function to cleanup child processes
cleanup() {
    echo "Stopping all processes..."
    kill $(jobs -p) 2>/dev/null || true
    exit 0
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
check_env_var "CELERY_BROKER_URL"

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

# Setup signal handler
trap cleanup SIGTERM SIGINT

# Start Celery worker with better heartbeat handling
echo "Starting Celery worker..."
celery -A SpotifyDownloader worker \
    --loglevel=info \
    --concurrency=2 \
    --max-tasks-per-child=1000 \
    --time-limit=3600 \
    --soft-time-limit=3300 \
    --broker-heartbeat=10 \
    --broker-connection-timeout=30 \
    --broker-connection-retry \
    --broker-connection-max-retries=3 &

# Start Gunicorn
echo "Starting Gunicorn server on port $PORT..."
gunicorn SpotifyDownloader.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 3 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - \
    --log-level info &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?
