def makeCodebook():
    #암호화 시킬 Pattern
    # Dictionary Key:Value
    decbook={'5':'a' ,'2':'b' ,'#':'d' ,'8':'e' ,'1':'f' ,'3':'g' ,'4':'h' ,'6':'i'
                 ,'0':'1' ,'9':'m' ,'*':'n' ,'%':'o' ,'(':'r' ,')':'s' ,';':'t' ,'?':'u'
                 ,'@':'v' ,':':'y' ,'7':' '}

    encbook = {}

    for k in decbook: # k = Key
        val = decbook[k] # val = Value
        encbook[val] = k # decbook의 key:Value를 Value:key로 만듬

    return encbook, decbook  # And Return encbook ,decbook

def encrypt(msg, encbook): # Param -> 문자열 , encbook
    for c in msg: # 문자열 반복
        if c in encbook: # 반복된 문자열의 인덱스중 하나 encbook에 있다면
            msg = msg.replace(c, encbook[c]) # 문자열 중  c 는 encbook[c]번째에서 찾아 대체(replace)

    return msg

def decrypt(msg, decbook):
    for c in msg:
        if c in decbook:
            msg = msg.replace(c, decbook[c])

    return msg


if __name__ == '__main__':
    plaintext  = 'I love you with all my heart'

    encbook, decbook = makeCodebook()
    ciphertext = encrypt(plaintext, encbook)
    print(ciphertext)

    deciphertext = decrypt(ciphertext, decbook)
    print(deciphertext)
