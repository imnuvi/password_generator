import struct
import tests2

a = input("enter password")

with open("password.len","r") as l:
    thelen = l.readlines()

with open("password.codes","rb") as f:
    v = 0
    data = f.read()
    print(len(data))
    for i in range(len(thelen)):
        # print(v)
        byt = data[v:v+int(thelen[i].strip("\n"))]
        print(v,int(thelen[i].strip("\n")))
        print(tests2.decrypt(byt,bytes(a,"utf-8")))
        v = int(thelen[i].strip("\n"))
        # print(v)

