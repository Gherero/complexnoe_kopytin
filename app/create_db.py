__author__ = 'gherero'
import sqlite3

con = sqlite3.connect('users.db')
cur = con.cursor()
cur.execute('CREATE TABLE users1 (id INTEGER PRIMARY KEY, firstName VARCHAR(100), secondName VARCHAR(30))')
con.commit()
con.close()