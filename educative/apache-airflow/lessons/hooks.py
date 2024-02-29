# ---------------------- Hooks -----------------------------------------
# Hooks are meant as an interface for interacting with external systems.
# Popular hook implementations, such as MySqlHook, HiveHook, and
# PigHook return objects, can handle the connection and interaction
# to specific instances of these systems and expose consistent methods
# to interact with them. Base class is BaseHook. There are logic how to
# connect on hooks, not how to execute. With hooks, we don’t need to
# store authentication parameters within the DAG.


# ---------------------- Connections --------------------------------------
# Hooks allow us to connect to external systems, and the information needed
# to make the connection, such as hostname, port and other credentials is
# stored in a connection.
# Connections can be stored in any one of the following ways:
#
#     Metastore database
#     Environment variables
#     Custom secrets store


