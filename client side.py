import socket
from time import sleep


host = "0.0.0.0"
port = 12345
message = str()

def send(server_ip, message):
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))

 
    client_socket.send(message.encode())
    
    response = b""
    while True:
        part = client_socket.recv(1024)
        if not part:
            break
        response += part
    
    print("From server:", response.decode())
    client_socket.close()

def rec():
    global message
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()  
    print("server listening on", host,port)
    conn, addr = server_socket.accept()
    print(addr,"connected")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        message = data.decode()
        conn.send(b"message received")

    conn.close()
    server_socket.close()

def establish():
    global message
    message = "//es"
    send("192.168.1.135", message)
    rec()

establish()
while True:
    message = input("type message you want to send: ")
    send("192.168.1.135", message)