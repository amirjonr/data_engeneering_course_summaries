# --------------------- Branching ---------------------------------
# As we write more complex workflows, a need arises to create
# branches within our workflows. Depending on the evaluation
# of some user-specified conditions, the workflow may execute
# a different set of tasks. Airflow provides operators to
# enable branching in workflows.
# Branching is a condition for completing tasks and its order.
# One task can run only after other task. For ex:
# Run task2 if task1 is done, or any other similar example
