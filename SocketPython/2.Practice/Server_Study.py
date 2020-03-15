#-*- coding:utf-8 -*-

import socket
import sys
import time
import threading
import os

now = time.localtime()
s = "%d년 %d월 %d일 %d시 %d분 %d초"\
    %(now.tm_year, now.tm_mon ,now.tm_mday ,now.tm_hour, now.tm_min ,now.tm_sec)


#연결된 클라이언트에게 보낼 메세지
def sendMsg():
    while True:

        str1 = ''
        msg = input("Send To MSG=>")

        if (msg != 'quit') and (msg != ''):
            str1 = str1+' '+msg
            client_socket.send(str1.encode())

        elif msg == '':
            client_socket.send(msg.encode())
            continue

        elif msg == 'quit':
            sock.close()
            sys.exit()

#연결된 클라이언트로 부터 받는 메세지
def printMSG():
    while True:
        data = client_socket.recv(65535)
        #time.sleep(0)
        s = "<=%d시 %d분"% (now.tm_hour, now.tm_min)
        print("\n                   ",data.decode(),'☜client','<',s,'>')
        del data

if __name__ == '__main__':
    host = socket.gethostname()
    S_host = socket.gethostbyname(host)
    port = 4044

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))  # 서버 ip와 port
    client_socket, addr = sock.accept()
    print("[+]SERVER Running!")
    print("==================================")

    try:

        threading._start_new_thread(sendMsg, ())
        threading._start_new_thread(printMSG,())

    except ConnectionRefusedError:
        print("Exit CLIENT!")
    while 1:
        pass
