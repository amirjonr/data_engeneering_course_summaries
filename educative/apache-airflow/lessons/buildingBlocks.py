# ------------------------- DAG ---------------------------------------------------
# DAG defines how to execute the tasks (constraints and dependensies),
# but it does not say what a particular task will do.
# A DAG can be specified by instantiating an object of the
# airflow.models.dag.DAG class as follows:

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

dag = DAG('Example1', schedule_interval='@once', start_date=days_ago(1), )

# ------------------------- Operator ----------------------------------------------
# If DAG defines a workflow, operator defines a work. When operator is instantiated
# in Python, an operator is called a TASK. All operators are inherited from
# BaseOperator. For example: BashOperator, EmailOperator, PythonOperator, MySQL -
# operator and etc

# There are 3 main types of operators:
# 1.   Operators that perform an action or request another system to perform an action.
# 2.   Operators that transfer data from one system to another.
# 3.   Operators that run until a certain condition or criteria are met, e.g.,
#    a particular file lands in HDFS or S3, a Hive partition gets created, or a specific
#    time of the day is reached. These special kinds of operators are also known as
#    sensors and can allow part of your DAG to wait on some external system. All sensor
#    operators derive from the BaseSensorOperator class.

# ---------------------------------- Task ----------------------------------------------
# A task is an example of operator and can be defined as a unit of work. It represented
# as a NODE in DAG. It can be trivial or complex. (easy, hard)

# ---------------------------------- TaskInstance --------------------------------------
# A task instance represents an actual run of a task. Is has execution_date, and it is
# instantiable and runnable. It has states such as: running, success, failed, skipped
# and retry. It has life cycle, through which it moves from one state to another.

# ---------------------------------- DAG run -------------------------------------------
# A DAG when executed, is called DAG run. There could be multiple DAG runs associated
# with a DAG running at the same time.

# ---------------------------------- Relationships --------------------------------------
# Airflow excels at defining complex relationships between different tasks. For instance,
# we can specify that task t1 occurs before task t2 as follows:

t1 = BashOperator(task_id='t1', bash_command='pwd', start_date=days_ago(1))
t2 = BashOperator(task_id='t2', bash_command='ll', start_date=days_ago(1))

t2.set_upstream(t1)
t1.set_downstream(t2)
t1 >> t2
t2 << t1

# all of the above four statements define the same relationship between t1 and t2, t2
# executes only after t1
