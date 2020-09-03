import getpass
import encoder

password = getpass.getpass(prompt="enter your password")


print("\n\n\n")
with open("password.codes","r") as p_file:
	lst = p_file.readlines()

for i in lst:
	print(i,type(i))
	print(i.decode("utf-8"))
# 	print(encoder.decoded("pointy",i))
