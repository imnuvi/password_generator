#main file that generates all codes

import random
import sys
import os
import re
from cryptography.fernet import Fernet
args = sys.argv

f_type = args[1]
code_len = int(args[2])


def gen_password(f_type,code_len):
	#f_type is the dictionary to use, ("1","2","3") change variable to whatever you want if you have specific language requirements
	# 2 and 3 are actually pretty small words but are slightly unintelligible. use 1 if you want to remember words
	
	# code_len gives the length of password to be created as second argument

	filename = "./dictionaries/wordlist_" + f_type + ".txt"
	lst = []

	def roller():
		patt = ""
		# die roll
		for i in range(5):
			roll = str(random.randint(1,6))
			patt += roll
		return patt

	with open(filename) as f:
		line_list = f.readlines()
		for i in range(code_len):
			pattern = roller()
			line_no = 0
			print(pattern,end=" ")
			for line in line_list:
				if pattern in line:
					print(line_list[line_no][6:-1])
					lst.append(line_list[line_no][6:-1])
				else:
					line_no += 1

	generated_word = "".join(lst)
	return (generated_word)


# this adds the password to the codes file
if os.path.exists("./password.codes"):
	print(" generated code is \n")
	code = gen_password(f_type,code_len)
	with open("./password.codes","a+") as code_file:
		code_file.seek(0)
		data = code_file.read(100)
		if len(data) > 0:
			code_file.write("/n")
		code_file.write(code)
	print("\n "+code)
	print("\n code has been added to password.codes file, and wont be available without master password")


#this is to create the master.key and the password.codes file anew
else:
	open("password.codes","w+")
	code = gen_password(f_type,code_len)
	print(code)
	print("This is the master password, Remember this because without this all your passwords are lost and unretrievable")