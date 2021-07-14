import psycopg2

connection = psycopg2.connect(
    user = 'Admin',
    password = '7343891',
    host = '127.0.0.1',
    port = '5432',
    database = 'myChat'
)
cursor = connection.cursor()
query = 'SELECT * FROM "Channels"'
cursor.execute(query)
registers = cursor.fetchall()
print(registers)

cursor.close()
connection.close()