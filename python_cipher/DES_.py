from Crypto.Cipher import DES3
from Crypto.Hash import SHA256 as SHA

class des():
    def __init__(self, keytext,ivtext):
        hash = SHA.new()
        hash.update(keytext)
        key = hash.digest()
        self.key = key[:24]

        hash.digest(ivtext)
        iv = hash.digest()
        self.iv = iv[:8]

    def enc(self,plaintext):
        des3 = DES3.new(self.key ,DES3.MODE_CBC,self.iv)
        encmsg = des3.encrypt(plaintext)
        return encmsg

    def dec(self,ciphertext):
        enc = DES3.new(self.key,DES3.MODE_CBC,self.iv)
        decmsg = enc.decrypt()
        return decmsg


def main():
    keytext = "jians123"
    ivtext = "1234"
    msg = "python35"

    Cipher = des(keytext,ivtext)
    ciphered = Cipher.enc(msg)
    dcipherd = Cipher.dec(ciphered)
    print(msg)
    print(ciphered)
    print(dcipherd)

if __name__ == '__main__':
    main()
