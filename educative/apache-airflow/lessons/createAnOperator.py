# ------------------------- Operator -----------------------------------
# Operators present a task or the actual work performed at each Node
# of Dag. All operators are derived from BaseOperator base class.
# Here I create a HelloWorldOperator with main logic in execute
# method, it must but idempotent, because we can retry it many times.

import logging

from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

log = logging.getLogger(__name__)


class HelloWorldOperator(BaseOperator):
    @apply_defaults
    def __init__(self, param1, param2, *args, **kwargs):
        self.param1 = param1
        self.param2 = param2
        super(HelloWorldOperator, self).__init__(*args, **kwargs)

    def execute(self, context):
        # Operator only prints a Hello World message
        log.info("Hello World : %s %s", self.param1)
