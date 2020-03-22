import sqlite3

conn = sqlite3.connect("C:\\Users\\user\\Desktop\\analysisfile\\History.db")
cur = conn.cursor()

sql = "SELECT url,title,visit_count, last_visit_time from urls"

cur.execute(sql)
rows = cur.fetchall()

for row in rows:
    print(row)


