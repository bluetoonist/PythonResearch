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
conn = sqlite3.connect("test.db")

cur = conn.cursor()

cur.execute('select * from customer where id= ? and name=?',(str(1)+'update customer set name=A where name=Alex', "Alex"))
cur.execute('select * from customer')
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()

