__author__ = 'gherero'
import sqlite3

con = sqlite3.connect('users.db')
cur = con.cursor()
cur.execute('CREATE TABLE time_log ('
            'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, '
            'username VARCHAR(100), '
            'status integer, '
            'sqltime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL)')
con.commit()
con.close()