import threading
import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",8888))
server.listen()

def handle_client(client_sock):
    request=client_sock.recv(1024).decode('utf-8')
    print(request)
    client_sock.send("Message Received".encode('utf-8'))

while True:
    client_socket,address=server.accept()
    conn=threading.Thread(target=handle_client,args=(client_socket,))
    conn.start()

