import sqlite3

#Open database
conn = sqlite3.connect('database.db')

conn.execute('''CREATE TABLE details
		(
		fname TEXT,
		lname TEXT,
		email TEXT,
		comment TEXT
		)''')

conn.close()

