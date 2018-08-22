import MySQLdb

conn = MySQLdb.connect("localhost", "root", "guozhi", "test")

cur = conn.cursor()
#name = raw_input()
sql = "select * from test3"
insert_sql = "insert into test3 (id, name) value ( 12,'mlia')"

cur.execute(insert_sql)

conn.commit()
cur.execute(sql)
result = cur.fetchall()

for row in result:
	print row[0]
	print row[1]
conn.close()