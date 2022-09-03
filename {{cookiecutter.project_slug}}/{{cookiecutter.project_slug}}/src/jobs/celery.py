from settings import settings

from celery import Celery

app = Celery(
    "jobs",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
    include=["jobs.tasks"],
)
app.conf.update(
    result_expires=60,
)

celery = app

if __name__ == "__main__":
    app.start()
