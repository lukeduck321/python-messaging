import socket

host = "0.0.0.0"
port = 12345

def start():
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
        print("recived:",data.decode())
        conn.send(b"message received")
    
    conn.close()
    server_socket.close()

start()