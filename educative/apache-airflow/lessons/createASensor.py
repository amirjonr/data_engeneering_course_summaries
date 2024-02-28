import logging
from os import path

from airflow.sensors.base import BaseSensorOperator
from airflow.utils.decorators import apply_defaults

log = logging.getLogger(__name__)


class HelloWorldSensor(BaseSensorOperator):
    @apply_defaults
    def __init__(self, pathToCheck, *args, **kwargs):
        super(HelloWorldSensor, self).__init__(*args, **kwargs)
        self.pathToCheck = pathToCheck

    def poke(self, context):
        exists = path.exists(self.pathToCheck)
        if exists:
            log.info("Sensor detected path exists!")
            return True
        else:
            log.info("Sensor did not find path, will try again later!")
            return False
