import os
from celery import Celery
from celery.signals import worker_ready

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SpotifyDownloader.settings")

# Initialize Celery app
app = Celery("SpotifyDownloader")

# Load settings from Django settings.py using namespace CELERY
app.config_from_object("django.conf:settings", namespace="CELERY")

# Configure Celery for production
app.conf.update(
    worker_max_tasks_per_child=1000,  # Restart worker after 1000 tasks
    worker_prefetch_multiplier=1,      # Don't prefetch tasks
    task_time_limit=3600,              # 1 hour timeout for tasks
    task_soft_time_limit=3300,         # Soft timeout 55 minutes
    broker_connection_retry_on_startup=True,  # Retry broker connection on startup
)

# Auto-discover tasks from all installed apps
app.autodiscover_tasks()

@worker_ready.connect
def at_start(sender, **kwargs):
    print("Celery worker is ready!")
    
@app.task
def debug_task():
    """Debug task to verify Celery is working"""
    print("Celery is working - Debug task executed")
    return True