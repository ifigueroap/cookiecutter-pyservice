"""
Main entry-point for {{cookiecutter.project_name}} API.

Run as a regular FastAPI application to access the documentation.
"""

import logging

from pydantic import BaseModel
from fastapi import FastAPI
from celery import Celery

from routers.health_router import router as health_router
from settings import settings

logging.basicConfig(level=settings.LOG_LEVEL)
logger = logging.getLevelName(__name__)

# Celery queue configuration
celery = Celery(
    "celery",
    backend=settings.CELERY_BROKER_URL,
    broker=settings.CELERY_RESULT_BACKEND
)


class Item(BaseModel):
    """Payload structure for Celery tasks."""
    name: str


app = FastAPI(title="{{cookiecutter.project_api_name}}")


@app.post("/hello")
def hello(item: Item):
    """Start sample Celery task."""
    task_name = "hello.task"
    task = celery.send_task(task_name, args=[item.name])
    logger.info(task.__dict__)
    return dict(id=task.id)


app.include_router(health_router)
