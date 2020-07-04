import sqlite3
"""
table create
sqlite> create table customer (
   ...> id integer primary key autoincrement,
   ...> name text not null,
   ...> category integer,
   ...> region text);

insert value
sqlite> INSERT INTO customer (name,category, region) VALUES('Alex',1,'SEA');   
   
"""

# connect data base sqlite3
conn = sqlite3.connect("test.db")

cur = conn.cursor()
#INSERT
cur.execute("insert into customer (name,category,region) VALUES ('Apple',2,'MOUNT')")

# READ
cur.execute('select * from customer where id= 1')

rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()

