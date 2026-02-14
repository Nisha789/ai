import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "*****",
    database = "sample_db_ai")

cursor = conn.cursor()

cursor.execute("select * from tasks")

for row in cursor.fetchall():
    print(row)
    
cursor.close()
conn.close()