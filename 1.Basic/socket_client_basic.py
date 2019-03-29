import socket
from threading import Thread

host = "127.0.0.1"
port = 4000

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((host,port))

while True:
    line = input("INPUT THE DATA : ")
    sock.sendall(line.encode())
    if not line:break

    data = sock.recv(1024)
    if not data: break
    print(data.decode())

sock.close()