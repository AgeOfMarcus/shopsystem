#!/usr/bin/python3

import barcode, fire # fire for easy CLI
from barcode.writer import ImageWriter # So we can save it to PNG

class Generator(object):
	def ean13(self, code, name="barcode"):
		code = str(code)
		if (not code.isnumeric()) or (not len(str(code)) == 12):
			return False
		EAN = barcode.get_barcode_class("ean13")
		ean = EAN(code,writer=ImageWriter())
		print(ean.save(name))

if __name__ == "__main__":
	fire.Fire(Generator)