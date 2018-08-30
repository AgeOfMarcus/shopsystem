#!/usr/bin/python3

import sqlite3, fire

class Manager(object):
	def select(self, id, dbname="database.db"):
		db = sqlite3.connect(dbname)
		cursor = db.cursor()
		res = cursor.execute("SELECT NAME,BALANCE FROM cards WHERE ID=%s" % str(id)).fetchall()[0]
		rres = {'name':res[0],'balance':res[1]}
		db.close()
		print(rres)
	def insert(self, id, name, balance=0.00, dbname="database.db"):
		db = sqlite3.connect(dbname)
		cursor = db.cursor()
		cursor.execute("INSERT INTO cards (ID,NAME,BALANCE) VALUES (%s,'%s',%s)" % (
				str(id),
				name,
				str(balance),
			))
		db.commit()
		db.close()
	def delete(self, id, dbname="database.db"):
		db = sqlite3.connect(dbname)
		cursor = db.cursor()
		cursor.execute("DELETE FROM cards WHERE ID=%s" % str(id))
		db.commit()
		db.close()

if __name__ == "__main__":
	fire.Fire(Manager)