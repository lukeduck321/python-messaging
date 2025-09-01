import socket

host = "0.0.0.0"
port = 12345
message = ""

def rec():
    global message
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print("Server listening on", host, port)

    while True:
        conn, addr = server_socket.accept()
        print(addr, "connected")

        data = conn.recv(1024)
        if not data:
            conn.close()
            continue

        message = data.decode().strip()
        print("Received:", message)

        if message == "//es":
            try:
                with open("log.txt", "r") as f:
                    file_data = f.read()
                    conn.sendall(file_data.encode())
            except FileNotFoundError:
                conn.sendall(b"file not found")
        else:
            with open("log.txt", "a") as f:
                f.write("\n" + message)
            conn.sendall(b"message received")

        conn.close()

rec()
