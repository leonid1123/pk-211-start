import sqlite3

conn = sqlite3.connect("pokupki.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS pokupki (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price INTEGER, kolichestvo INTEGER)")
#cur.execute("insert into pokupki(name, price, kolichestvo) values('яблоки',120, 2)")
#conn.commit()
cur.execute("SELECT price,name,kolichestvo FROM pokupki")
ans = cur.fetchall()
print(ans)