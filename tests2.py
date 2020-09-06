from hashlib import blake2b
import base64
import secrets
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes as hsh
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def encoded(pwd, msg):
    a = bytes(pwd, "utf-8")
    salt = b'\xb0\x15\xc9\xa5:\x19\xe7\x14\x97\xc4\x86 \xfc\xe9\x9d\xb7'
    # print(salt)
    kdf = PBKDF2HMAC(algorithm=hsh.SHA256(), length=32, salt=salt, iterations=0)

    v = kdf.derive(a)
    key = base64.urlsafe_b64encode(v)

    # print(key,"\n")
    msg = bytes(msg, "utf-8")

    cipher = Fernet(key).encrypt(msg)

    return cipher


def decoded(pwd, msg):
    a = pwd
    a = bytes(a, "utf-8")
    salt = b'\xb0\x15\xc9\xa5:\x19\xe7\x14\x97\xc4\x86 \xfc\xe9\x9d\xb7'
    # print(salt)

    kdf = PBKDF2HMAC(algorithm=hsh.SHA256(), length=32, salt=salt, iterations=0)

    v = kdf.derive(a)
    key = base64.urlsafe_b64encode(v)

    # print(cipher,"\n")

    decypher = Fernet(key).decrypt(msg)

    return decypher

# vals = encoded("hi","hello there")
# print(vals)
# phi = (vals).decode("utf-8")
# print(phi)
# print(phi.encode("utf-8"))
# vals = str(vals)
# print(repr(vals))
# ans = decoded("hi",vals)
# print(ans)