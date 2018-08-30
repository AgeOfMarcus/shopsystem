#!/usr/bin/python3

import sqlite3, fire

class Manager(object):
	def select(self, id, dbname="database.db"):
		db = sqlite3.connect(dbname)
		cursor = db.cursor()
		res = cursor.execute("SELECT NAME,PRICE FROM items WHERE ID='%s'" % str(id)).fetchall()[0]
		db.close()
		rres = {'name':res[0],'price':res[1]}
		print(rres)
	def insert(self, id, name, price, dbname="database.db"):
		db = sqlite3.connect(dbname)
		cursor = db.cursor()
		cursor.execute("INSERT INTO items (ID,NAME,PRICE) VALUES (%s,'%s',%s)" % (
				str(id),
				name,
				str(price),
			))
		db.commit()
		db.close()
	def delete(self, id, dbname="database.db"):
		db = sqlite3.connect(dbname)
		cursor = db.cursor()
		cursor.execute("DELETE FROM items WHERE ID=%s" % str(id))

if __name__ == "__main__":
	fire.Fire(Manager)