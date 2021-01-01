from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def readPEM():
    h = open("/mykey.pem",'r')
    key = RSA.importKey(h.read())
    h.close()
    return key

def rsa_enc(msg):
    private_key = PKCS1_OAEP.new(readPEM()) #개인키
    encdata =private_key.encrypt(bytes(msg,'utf-8'))
    return encdata

def rsa_dec(msg):
    private_key = PKCS1_OAEP.new(readPEM())
    decdata = private_key.decrypt(msg)
    return decdata

if __name__ == '__main__':
    msg = '' # input some string 
    ciphered = rsa_enc(msg)
    print(ciphered)
    deciphered = rsa_dec(ciphered)
    print(deciphered)
