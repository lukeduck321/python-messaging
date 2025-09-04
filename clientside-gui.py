import socket
import threading
from tkinter import *


host = "0.0.0.0"
port = 12345
server_ip = "10.125.116.216"
message = "example \nnew line\nnew line\nnew line\nnew line"
out = str()
cwidth = str()
cheight = str()

#gui setup
window = Tk()
guiout = StringVar()



def click():
    global message, guiout
    messsage = guiout.get()
    print(guiout.get())
    #send(server_ip,message)
    e1.delete(0,END)
    #send(server_ip,"//es")
        
def enter(event):
    click()

def refreshtwo():
    print("refreshed")
    #send(server_ip,"//es")

def refresh(event):
    refreshtwo()

def send(server_ip, message):
    global out
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
    cheight = window.winfo_height()
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
            out =+ "\n" + data.decode()
            print("Received:", message)
            conn.send(b"message received")
        conn.close()

def update_window():
    global message,cwidth,cheight,c1
    cwidth = window.winfo_width() - 15
    c1 = Canvas(window, width=cwidth, height=cheight, bg="blue")
    c1.place(x=0, y=15)
    print(cwidth, cheight)

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


#buttons
b1 = Button(window, text="send",height=1,width=5,command=click)
b1.grid(row = 0, column = 1,)
b2 = Button(window, text="refresh",height=1,width=5,command=refreshtwo)
b2.grid(row = 0, column = 2)
#text
#c1 = Canvas(window,width=cwidth,height=cheight,bg="blue")
#c1.place(x=0,y=15)
#enrties
e1 = Entry(window, textvariable=guiout,width=50)
e1.grid(row = 0, column = 0)
#keybinds
window.bind('<Return>',enter)
#window.bind('<r>',refresh)
#window.bind('<R>',refresh)
window.after(100,update_window)
window.mainloop()
