from airflow.plugins_manager import AirflowPlugin

from createAnOperator import HelloWorldOperator


class HelloWorldPlugin(AirflowPlugin):
    name = 'hello_world_plugin'
    operators = [HelloWorldOperator]
