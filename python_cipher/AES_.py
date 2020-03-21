from Crypto.Cipher import AES
from Crypto.Hash import SHA256 as SHA

class myAES():
    def __init__(self ,keytext ,ivtext):
        hash = SHA.new()
        hash.update(keytext)

        keytext = hash.digest()
        self.key = keytext[:16]

        hash.update(ivtext)
        ivtext = hash.digest()
        self.iv = ivtext[:16]

    def makeEnable(self, plaintext):
        fillersize = 0 #int
                        #plaintext = msg
        textsize = len(plaintext) #14
        if textsize%16 != 0:
            fillersize = 16-textsize #14
            #2
            #bytes(str(),'utf-8')
        filler ='0'*fillersize #fillersize=8 /filler = 00000000
        filler1 = bytes(filler, 'utf-8') #2

        header ='%d'%(fillersize) #  2  str
        gap = 16-len(header)  #gap =14

        header += '#'*gap #hedaer = 2 gap =14 + 16
        header1 = bytes(header, 'utf-8') # #8개

                #16      #14       #2
        return header1+plaintext+filler1


    def enc(self, plaintext):
        plaintext = self.makeEnable(plaintext)
        aes = AES.new(self.key , AES.MODE_CBC ,self.iv)
        encmsg = aes.encrypt(plaintext)
        return encmsg

    def dec(self, ciphertext):
        aes = AES.new(self.key , AES.MODE_CBC, self.iv)
        decmsg = aes.decrypt(ciphertext)

        header = decmsg[:16].decode()
        fillersize = int(header.split('#')[0])
        if fillersize != 0:
            decmsg = decmsg[16:-fillersize]

        return decmsg

def main():
    keytext = bytes('samsjang','utf-8')
    ivtext = bytes('1234','utf-8')

    msg = bytes('python','utf-8') #14

    cipherd = myAES(keytext,ivtext)
    encipherd = cipherd.enc(msg)
    decipherd = cipherd.dec(encipherd)

    print('%s'%encipherd)
    print('%s'%decipherd)

if __name__ == '__main__':
    main()


