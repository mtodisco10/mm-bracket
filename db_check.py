import sqlite3

con = sqlite3.connect('winners.db')
cur = con.cursor()

for row in cur.execute('select * from winners'):
	print(row)

# cursor =  cur.execute('select * from winners')
# names = list(map(lambda x: x[0], cursor.description))
# print(names)