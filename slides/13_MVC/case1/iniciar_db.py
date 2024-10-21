import sqlite3

SQL = 'database/database.sql'
DATABASE = 'database/database.db'

with open(SQL) as f:
    conn = sqlite3.connect(DATABASE)
    conn.executescript(f.read())
    conn.commit()
    conn.close()
    