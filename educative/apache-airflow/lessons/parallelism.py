# -------------------------- parallelism -------------------------------
# The parallelism configuration parameter limits the number of tasks
# that are actively being executed across the entire system. By default,
# this value is set to 16 in airflow.cfg.


# -------------------------- pools -------------------------------
# Pools are one of the ways to limit the number of tasks that run at
# any given time. A pool exists by default and is named the default
# pool, consisting of 128 worker slots. Each slot can be used to run
# a task. We can change the number of slots for a given pool and also
# create new pools, e.g., using the UI. A task can be assigned to a
# specific pool using the pool parameter.

# -------------------------- dag_concurrency -------------------------------
# Another parameter that is defined in the airflow.cfg configuration
# file determines how many tasks for a given DAG can execute simultaneously.
# By default, this is set to 16. This is a per DAG concurrency parameter.

# -------------------------- worker_concurrency -------------------------------
# The configuration parameter, worker_concurrency, determines how many tasks
# a single worker can execute at the same time. This parameter only affects
# the Celery executor. Increasing worker_concurrency may require providing
# more resources to the workers to handle the load.

# -------------------------- relationship -------------------------------
# The knobs and levers Airflow exposes to control parallelism in the system
# can be confusing, but they are all related to each other. For instance, if
# we set the parallelism parameter to 2 and dag_concurrency to 10, we’ll only
# be able to run two tasks simultaneously for a given DAG. Similarly, if we
# change dag_concurrency to 10 but parallelism to 5, then we’ll only be able
# to execute five tasks in parallel for a DAG even though we are allowed to run
# ten tasks for a DAG concurrently.
