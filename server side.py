import socket
from time import sleep

host = "0.0.0.0"
port = 12345
message = str()

def rec():
    global message
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()  
    print("server listening on", host,port)
    conn, addr = server_socket.accept()

    while True:
        conn, addr = server_socket.accept()
        print(addr, "connected")

        data = conn.recv(1024)
        if not data:
            conn.close()
            continue

        message = data.encode()
        print("recived:", message)

        if message.strip() == "//es":
            try:
                f = open("log.txt", "r")
                file_data = f.read()
                conn.sendall(file_data.encode())
            except FileNotFoundError:
                conn.sendall(b"file not found")
        else:
            conn.sendall(b"message recived")

        conn.close()

def send():
    global message
    port = 12345
    server_ip = "255.255.255.255"

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    sock.sendto(message.encode(), (server_ip, port))
    
    data = sock.recv(1024)
    print(data.decode())

    sock.close()

    if message == "//es":
        message = str()

while True:
    sleep(1)
    if message == "//es":
        file = open("log.txt", "r")
        message = file.read()
        print(message)
        send()
        rec()
    rec()