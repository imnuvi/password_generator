import struct
import tests2

a = input("enter password")

with open("password.codes","rb") as f:
    thelen = len(f.read())
    print(thelen)
    # for i in range(thelen//32):
    #     byt = thelen[i:i+32]
    #     print(tests2.decrypt(i,a))

