#encoding with symmetric key testing

import base64
import struct
from Crypto.Cipher import AES


def pad16(s):
    t = struct.pack('>I', len(s)) + s
    return t + b'\x00' * ((16 - len(t) % 16) % 16)


def unpad16(s):
    n = struct.unpack('>I', s[:4])[0]
    return s[4:n + 4]


class Crypt(object):
    def __init__(self, password):
        password = pad16(password)
        self.cipher = AES.new(password, AES.MODE_ECB)

    def encrypt(self, s):
        s = pad16(s)
        return self.cipher.encrypt(s)

    def decrypt(self, s):
        t = self.cipher.decrypt(s)
        return unpad16(t)


def encrypt(s, p):
    c = Crypt(p)
    return c.encrypt(s)


def decrypt(s, p):
    c = Crypt(p)
    return c.decrypt(s)

msg = (b" trapezoidviewablecavalier")
secret_key = b"derived"
x = encrypt(msg,secret_key)
y = decrypt(x,secret_key)
print(len(x),y)

# msg = (b"hello loo there thereeeeeeee")
# msg1 = (b"whatthefuckisgoinon")
# msg3 = (b"WhattheAtualF")
# print(msg)
# secret_key = b"keykeykey"
#
# x = encrypt(msg,secret_key)
# y = decrypt(x,secret_key)
# x1 = encrypt(msg1,secret_key)
# x2 =  encrypt(msg3,secret_key)
# y1 = decrypt(x1,secret_key)
# y2 = decrypt(x2,secret_key)
# print(len(x),y)
# print(len(x1),y1)
# print(len(x2),y2)