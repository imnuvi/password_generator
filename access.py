import struct
import encoder
import getpass

a = getpass.getpass(prompt="enter your password")


with open("./secure/password.len","r") as l:
    thelen = l.readlines()

with open("./secure/password.codes","rb") as f:
    v = 0
    data = f.read()
    print(len(data))
    for i in range(len(thelen)):
        # print(v)
        byt = data[v:v+int(thelen[i].strip("\n"))]
        print(v,int(thelen[i].strip("\n")))
        print(encoder.decrypt(byt,bytes(a,"utf-8")))
        v = int(thelen[i].strip("\n"))
        # print(v)

