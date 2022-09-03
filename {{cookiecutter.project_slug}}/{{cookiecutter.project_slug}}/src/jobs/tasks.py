from __future__ import absolute_import

import logging
import traceback
from time import sleep
from celery import states
from settings import settings

from {{cookiecutter.project_slug}}.src.jobs.celery import app

logging.basicConfig(
    level=settings.log_level.upper(),
    format="%(levelname)s in %(module)s: %(message)s",
)

logger = logging.getLogger(__name__)


@app.task(name="hello.task", bind=True)
def hello_world(self, name: str):
    try:
        if name == "error":
            k = 1 / 0
            print(k)
        for i in range(3):
            sleep(1)
            self.update_state(state="PROGRESS", meta={"done": i, "total": 60})
        return {"result": "hello {}".format(str(name))}
    except Exception as ex:
        self.update_state(
            state=states.FAILURE,
            meta={
                "exc_type": type(ex).__name__,
                "exc_message": traceback.format_exc().split("\n"),
            },
        )
        raise ex
