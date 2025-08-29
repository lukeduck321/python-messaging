import socket
import threading
from tkinter import *

host = "0.0.0.0"
port = 12345
server_ip = "192.168.8.112"
message = ""

#gui setup
window = Tk()
guiout = StringVar()


def send(server_ip, message):
    port = 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((server_ip, port))
        if message == "//es":
            pass
        else:
            message = "Ducky: " + message
        client_socket.send(message.encode())
        response = b""
        while True:
            part = client_socket.recv(1024)
            if not part:
                break
            response += part
        print("From server:\n", response.decode())
    except Exception as e:
        print("Send error:", e)
    finally:
        client_socket.close()

def rec():
    global message
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print("Client receiver listening on", host, port)
    while True:
        conn, addr = server_socket.accept()
        print(addr, "connected")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode()
            print("Received:", message)
            conn.send(b"message received")
        conn.close()

# Run receiver in background
threading.Thread(target=rec, daemon=True).start()

# Send establish signal
"""send(server_ip, "//es")

# Main loop
while True:
    message = input("Type message you want to send: ")
    send(server_ip, message)
"""

window.geometry("400x600+1520+480")

#enrties
ent1 = Entry(window, textvariable=guiout)
ent1.place(x=0,y=560)
#buttons

#text

#keybinds


window.mainloop()









