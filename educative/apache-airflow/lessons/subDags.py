# -------------------- SubDAGs ---------------------------------
# Picture:
# task1->task2->task6->[task4, task5, task3] -> task7
#
# Let’s assume that the task3, task4, task5, and task6
# tasks are all related and may be reused in other DAGs.
# We can create a SubDAG out of these four tasks and plug
# the SubDAG anywhere that it is required. This reduces
# maintenance and duplication of code. With SubDAG,
# the DAG above should look like this:
#
# task1->task2->SubDAG->task7
# for this we need to use SubDAGOperator
