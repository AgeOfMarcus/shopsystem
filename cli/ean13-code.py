#!/usr/bin/python3

import fire # handy CLI
from uuid import uuid4

class Generator(object):
	def gen(self):
		done = False
		while not done:
			code = str(uuid4())
			nums = ''
			for i in code:
				if i.isnumeric():
					nums += i
			if len(nums) > 12:
				fin = nums[0:12]
				done = True
		print(fin)

if __name__ == "__main__":
	fire.Fire(Generator)