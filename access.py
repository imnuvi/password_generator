import getpass
import encoder
import binascii

password = getpass.getpass(prompt="enter your password")


print("\n\n\n")
with open("password.codes","r") as p_file:
	lst = p_file.readlines()

for i in lst:
	print(i,type(i))
	z = i.encode("utf-8")
	print(encoder.decoded("pointy",z))

# a = binascii.a2b_qp("hello")
# print(type(a))
# b = binascii.b2a_qp(a)
# print(type(b))\


# with open("password.codes","r") as p_file:
# 	a = p_file.read()
# 	print(a)