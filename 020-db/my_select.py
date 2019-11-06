import sqlite3

conn = sqlite3.connect('students.db')

# sql = 'SELECT * FROM student'

user_name = input('name: ')

cursor = conn.execute('SELECT * FROM student WHERE name = ?', (user_name,))
for row in cursor:
    print(row)
    
conn.close()