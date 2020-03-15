from threading import Thread
import socket

host = "127.0.0.1"
port = 4000


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port))

def echo(sock):
    """
    클라이언트로 부터 오는 정보를 체크하는 코드
    sock 로부터 정보를 계속 받음
    """
    while True:
        data = sock.recv(1024)
        if not data:break # data False 값이면 break
        else: print("==>",data) # #data가 False가 아니면 출력
        sock.sendall(data) # 받은 데이터를 다시 돌려줌
    sock.close() # sock 종료

while True:
    sock.listen(1)
    conn,addr = sock.accept()
    #클라이언트로부터 오는 정보를 스레드화 시킴
    t = Thread(target=echo,args=(conn,)) # 접속된 클라이언트 정보로 스레드화
    t.start()

