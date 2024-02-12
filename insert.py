import sqlite3

conn = sqlite3.connect('afternoon.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (1,'FAITH KARIMI',34,34000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (2,'JANE KARIMI',31,25000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (3,'JOHN KIGOGA',36,32000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (4,'SARA SEREM',28,50000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (5,'JANET KARIMI',30,60000.00)")

conn.commit()
print("Employee inserted successfully")
conn.close()