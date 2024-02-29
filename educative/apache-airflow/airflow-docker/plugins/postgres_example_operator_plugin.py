from airflow.plugins_manager import AirflowPlugin

from postgres_example_operator import PostgresExampleOperator


class PostgresExampleOperatorPlugin(AirflowPlugin):
    name = "postgres_example_operator_plugin"
    operators = [PostgresExampleOperator]
