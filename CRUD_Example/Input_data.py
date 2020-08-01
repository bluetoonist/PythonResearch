import sqlite3
from random import randint

# connect data base sqlite3
conn = sqlite3.connect("test.db")
cur = conn.cursor()

# INSERT Query
"""
Example
insert into table (col1, col2, col3)
values (value1,value2,value3)
"""
# 2
cur.execute("insert into customer (name,category,region) VALUES ('Apple',2,'MOUNT')")
# 3
cur.execute("insert into customer (name,category,region) VALUES ('pear',3,'kor')")
# 4
cur.execute("insert into customer (name,category,region) VALUES ('chestnut',4,'jap')")
# 5
cur.execute("insert into customer (name,category,region) VALUES ('pine nut',5,'America')")
# 6
cur.execute("insert into customer (name,category,region) VALUES ('tangerine',6,'Russia')")

cur.fetchall()
conn.commit()
conn.close()

