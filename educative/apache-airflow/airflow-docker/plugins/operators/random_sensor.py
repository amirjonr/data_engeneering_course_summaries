import logging
from random import randrange

from airflow.sensors.base import BaseSensorOperator, PokeReturnValue
from airflow.utils.context import Context


class RandomSensor(BaseSensorOperator):
    """
    Sensor waits, when rand number from range(0, range_number) returns 0
    """

    def __init__(self, range_number: int = 10, **kwargs) -> None:
        super().__init__(**kwargs)
        self.range_number = range_number

    def poke(self, context: Context) -> bool | PokeReturnValue:
        """
        :param context:
        :return:
        """
        poke_num = randrange(0, self.range_number)
        logging.info(f"poke: {poke_num}")
        return poke_num == 0
