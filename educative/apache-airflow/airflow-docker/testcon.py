import psycopg2

# Подключение к PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="airflow",
    user="airflow",
    password="airflow"
)

# Теперь можно выполнять запросы к базе данных с использованием этого соединения

print(conn)

# Закрытие соединения
conn.close()
