import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="school",
    user="postgres",
    password="password"
)

cursor = conn.cursor()
cursor.execute("SELECT name, grade FROM students ORDER BY grade DESC")
print(cursor.fetchall())
conn.close()




# https://learn.microsoft.com/en-us/windows/wsl/install