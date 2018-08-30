#!/usr/bin/python3

import cv2, fire # CLI
from pyzbar import pyzbar

class Reader(object):
	def read(self, image):
		image = cv2.imread(image)
		barcodes = pyzbar.decode(image)
		res = []
		for barcode in barcodes:
			(x, y, w, h) = barcode.rect
			cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
			barcodeData = barcode.data.decode("utf-8")
			barcodeType = barcode.type
			res.append(barcodeData)
		try:
			print(res[0])
		except:
			return False

if __name__ == "__main__":
	fire.Fire(Reader)