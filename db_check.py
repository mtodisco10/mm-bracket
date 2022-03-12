#import sqlite3
import psycopg2

#con = sqlite3.connect('winners.db')
conn = psycopg2.connect(
   database="d50p3glj8p4gtu",
   user='nlavwjdwgcxeyg',
    password='0d2d99ddbae0886aec120f4239222d15aee55f2b2cf48f4a19d663c443fe6c49',
    host='ec2-54-158-26-89.compute-1.amazonaws.com',
    port= '5432'
)
cur = con.cursor()

for row in cur.execute('select * from winners'):
	print(row)

# cursor =  cur.execute('select * from winners')
# names = list(map(lambda x: x[0], cursor.description))
# print(names)