#-*- coding:utf-8 -*-
from Crypto.PublicKey import RSA

# PK_Key File Generate 

private_key = RSA.generate(1024)
f = open("./my.key" ,'wb+')
f.write(private_key.exportKey('PEM'))
f.close()
