from hashlib import blake2b
import base64
import secrets
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes as hsh
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

h = blake2b()
a = str(input())
a = bytes(a,"utf-8")
# h.update(a)
# v = h.hexdigest()
# print(repr(v),"\n")
# v = bytes(v,"utf-8")

# waack = base64.urlsafe_b64encode(a)
# print(waack,"\n")

# key_64 = Fernet.generate_key()
# print(key_64,"\n")


salt = b'\xb0\x15\xc9\xa5:\x19\xe7\x14\x97\xc4\x86 \xfc\xe9\x9d\xb7'
print(salt)
kdf = PBKDF2HMAC(algorithm=hsh.SHA256(),length=32,salt=salt,iterations=0)

v = kdf.derive(a)
key = base64.urlsafe_b64encode(v)

print(key,"\n")


cipher = Fernet(key).encrypt(b"my darkest secret")

print(cipher,"\n")

decypher = Fernet(key).decrypt(cipher)

print(decypher)