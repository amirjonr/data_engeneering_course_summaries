import os
from datetime import datetime

from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profile import SnowflakeUserPasswordProfileMapping

profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_conn",
        profile_args={"database": "dbt_db", "schema": "dbt_schema"},
    )
)

dbt_snowflake_dag = DbtDag(
    project_config=ProjectConfig("/home/amirjon/data_engeneering_course_summaries/dbt/dbt_dag/data_pipeline", ),
    operator_args={"install deps": True},
    profile_config=profile_config,
    execution_config=ExecutionConfig(dbt_execution_path=f"{os.environ['AIRFLOW_HOME']}/venv/bin/activate"),
    schedule_interval="@daily",
    start_date=datetime(2023, 9, 10),
    catchup=False,
    dag_id="dbt_dag",
)