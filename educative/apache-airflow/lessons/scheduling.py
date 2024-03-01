# ------------------------- Scheduling ---------------------------------
# When creating a DAG, we can specify the start_date and a
# schedule_interval as parameters to the constructor. Let’s see an
# example:
from datetime import datetime

from airflow import DAG

dag = DAG(
    dag_id='scheduling_dag',
    # default_args=default_args,
    description='Example of scheduling',
    schedule='@daily',
    start_date=datetime(2020, 9, 5)
)


# Airflow will also schedule DAG runs for the previous days even
# though we are running the DAG now. Each DAG run will be associated
# with an execution date and a start date. The execution date is the
# date that the DAG should have run, and the start date is when
# Airflow actually runs it. Please don’t confuse the start_date that
# we pass into the DAG constructor with the start date associated
# with a DAG run; both are distinct.

# Finally, you may note that a DAG doesn’t execute at exactly
# the time it is supposed to run, e.g., a DAG run may start
# at 10:01 p.m. when its schedule asks it to run at 10:00 p.m.
# There may be a delay of a few seconds or so. There’s a
# configuration parameter, scheduler_heartbeat_sec, defined 
# in airflow.cfg that controls how often the Airflow scheduler
# runs. The scheduler runs and looks for tasks to trigger,
# and there may be a delay in when a task becomes due and when
# the scheduler is able to run it. Making the scheduler run
# at a higher frequency can put pressure on the database,
# so any tweaks should be done cautiously.
