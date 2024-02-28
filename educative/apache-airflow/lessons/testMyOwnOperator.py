from airflow import DAG
from airflow.utils.dates import days_ago

dag = DAG('Example1',
          schedule_interval='@once',
          start_date=days_ago(1),)

hello_task = HelloWorldOperator(param1='This is an example operator by', param2="DataJek",
                                task_id='hello_world_task', dag=dag)