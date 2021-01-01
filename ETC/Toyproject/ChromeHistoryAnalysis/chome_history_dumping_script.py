import os
import sqlite3
# 이 스크립트는 chomre history file을 분석합니다
# 스크립트를 실행 시킬 떄는 chrome이 종료되어있어야 합니다.
save_data_dir = os.getcwd()

path = os.getenv("APPDATA")
os.chdir(path)
os.chdir('../')
os.chdir('.//Local//Google//Chrome//User Data//Default')

conn = sqlite3.connect("History")
cur = conn.cursor()

sql = "SELECT url,title,visit_count,datetime( (last_visit_time/1000000)-11644473600, 'unixepoch' ,'localtime') as time from urls"
cur.execute(sql)
rows = cur.fetchall()

os.chdir(save_data_dir)
with open("getLog","w",encoding="utf8") as f :
    for row in rows:
        parsing = "".join(str(row))
        parsing += "\n"
        f.write(parsing)
conn.close()