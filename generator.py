#main file that generates all codes

import encoder

import binascii
import random
import sys
import os
import re
import base64, hashlib
import getpass
from hashlib import blake2b

args = sys.argv

f_type = args[1]
code_len = int(args[2])
hasher = "hi"

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
if os.path.exists("./secure/password.codes"):
	# passer = open("./secure/master.key","r").read()
	ye = 1
	while ye:
		h = blake2b()
		entered_pass = getpass.getpass(prompt="please enter your main password: ")
		by = bytes(entered_pass,"utf-8")
		h.update(by)
		hasher = h.hexdigest()
		# passer = str(input("enter your main password to continue.."))
		if passer == hasher:
			ye = 0
			print(" generated code is \n")
			code = gen_password(f_type,code_len)
			cypher_code = (encoder.encrypt(bytes(code,"utf-8"),by))
			# cypher_code = cypher_code.decode("utf-8")
			with open("./secure/password.len","a+") as len_file:
				len_file.write(str(len(cypher_code)) + "\n")
			with open("./secure/password.codes","a+b") as code_file:
				code_file.write(cypher_code)
			print("\n "+code)
			print("\n the cypher of code has been added to password.codes file, and won't be available without master password")
		else:
			print("sorry wrong password, try again")
			continue

#this is to create the master.key and the password.codes file anew
else:
	open("./secure/password.codes","w+")
	code = gen_password(f_type,code_len)
	h = blake2b()
	by = bytes(code,"utf-8")
	h.update(by)
	with open("./secure/master.key","w+") as key:
		key.write(h.hexdigest())
	print(code)
	print("Since this is the first time you are running this generator"+"This is the master password,\n Remember this because without this all your passwords are lost and unretrievable")
	print("\n from now on you will need to type your password to generate or save and encode them")
