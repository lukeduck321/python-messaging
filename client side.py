import socket

def start(server_ip):
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))

    message = "hello from client"
    client_socket.send(message.encode())
    
    data = client_socket.recv(1024)
    print("from server:",data.decode())

    client_socket.close()

start("192.168.1.135")