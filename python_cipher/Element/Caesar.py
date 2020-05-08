# 카이사르 암호문 소스코드

def MakeDiskKey(k):
    """
    :param k 는 알파벳 인덱스
    :return: 복호화 된 문자열 키
    """

    dec_disk = {}
    for i in range(1,26):
        alp = (i+k)%26 + 65
        dec_disk[chr(alp)] = chr(i+65)
    return dec_disk

def caesar(msg,key):
    ret = ''
    msg= msg.upper()
    disk = MakeDiskKey(key)
    for c in msg:
        if c in disk:
            ret += disk[c]
        else:
            ret += c
    return ret

def attack(msg):
    for key in range(26):
        decmsg = caesar(msg,key)
        print(key,decmsg)

if __name__ == '__main__':
    msg = 'UGAMKZMBSMGQAVCUJMZBP'
    attack(msg)