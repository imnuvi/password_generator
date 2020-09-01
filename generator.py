#main file that generates all codes

import random
import sys
import re
args = sys.argv

#dictionary to use, ("1","2","3") change variable to whatever you want if you have specific language requirements
# 2 and 3 are actually pretty small words but are slightly unintelligible. use 1 if you want to remember words
f_type = args[1]

# give length of password to be created as second argument
code_len = int(args[2])

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
		print(pattern)
		for line in line_list:
			if pattern in line:
				lst.append(line_list[line_no][6:-1])
			else:
				line_no += 1

generated_word = "".join(lst)
print(generated_word)