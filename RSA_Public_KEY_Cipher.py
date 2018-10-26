from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5

def rsa_encrypt(msg):
    private_key = RSA.generate(1024)
    public_key = private_key.publickey()

    key = PKCS1_OAEP.new(public_key)
    encdata = key.encrypt(msg)
    print(encdata)

    prkey = PKCS1_OAEP.new(private_key)
    decdata =prkey.decrypt(encdata)
    print(decdata)

if __name__ =='__main__':
    msg = '' # input some string
    rsa_encrypt(msg.encode('utf-8'))
