#-* coding:utf-8 -*-
import socket
import sys
import time
import threading

#Name =socket.gethostname()
#ipAddress = socket.gethostbyname(Name)

def send_TO():
    while True:
        str1 =''
        msg = input("Send TO MSG=>")

        if (msg != 'quit') and (msg != ''):
            str1 = str1+''+msg
            sock.send(str1.encode())

        elif msg  == '':
           continue
        elif msg == 'quit':
            sock.close()
            sys.exit()

def print_MSG():
    while True:
        time.sleep(0)
        data = sock.recv(65535)
        print("\n                     ",data.decode(),"☜SERVER MSG")
        del data

if __name__ == '__main__':

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #host = input("연결할 서버 IP:")
    sock.connect(('10.27.185.125', 4044))

    try:
        print("[+]통신 시작 <==> [-]'quit' 입력 시 통신 종료")

        threading._start_new_thread(send_TO,())
        threading._start_new_thread(print_MSG,())
    except:
        pass
    while 1:
        pass