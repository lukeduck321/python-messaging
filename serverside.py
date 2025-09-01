def send(server_ip, message):
    port = 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((server_ip, port))
        client_socket.send(message.encode())

        response = b""
        while True:
            part = client_socket.recv(1024)
            if not part:
                break
            response += part

        print("From server:", repr(response.decode()))
    except Exception as e:
        print("Error in send():", e)
    finally:
        client_socket.close()
