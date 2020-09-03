from hashlib import blake2b

h = blake2b()
a = str(input(""))
a = bytes(a,"utf-8")
h.update(a)
print(h.hexdigest())