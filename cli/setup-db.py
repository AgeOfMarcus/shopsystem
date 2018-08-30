#!/usr/bin/python3

import sqlite3, sys

def setup(dbname):
	db = sqlite3.connect(dbname)
	cursor = db.cursor()
	cursor.execute("CREATE TABLE IF NOT EXISTS items (\
		ID INTEGER PRIMARY KEY NOT NULL, \
		NAME TEXT NOT NULL, \
		PRICE REAL NOT NULL);")
	cursor.execute("CREATE TABLE IF NOT EXISTS cards (\
		ID INTEGER PRIMARY KEY NOT NULL, \
		NAME TEXT NOT NULL, \
		BALANCE REAL NOT NULL, \
		PIN INTEGER NOT NULL);")
	db.commit()
	db.close()

if __name__ == "__main__":
	try:
		name = sys.argv[1]
	except:
		name = "database.db"
	setup(name)