from .celery import app
from time import sleep

@app.task
def add(x, y):
    sleep(5)
    """Add two numbers."""
    print(f"Adding {x} + {y}")
    return x + y
