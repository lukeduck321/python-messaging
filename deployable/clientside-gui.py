import socket
import threading
from tkinter import *

host = "0.0.0.0"
port = 12345
server_ip = "10.125.116.214"  #Replace with your actual server IP
message = "example \nnew line\nnew line\nnew line\nnew line"
out = str()
cwidth = str()
cheight = str()
chat_log = "" 
passn=True
change_check=str()
send_error = False


# GUI setup
window = Tk()
guiout = StringVar()
window.geometry("600x800+1520+480")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=0)
window.columnconfigure(2, weight=0)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=0)

def click():
    global message, guiout
    message = guiout.get() 
    print("Sending:", message)
    send(server_ip, message)
    e1.delete(0, END)
    refreshtwo()


def enter(event):
    click()

def refreshtwo():
    send(server_ip, "//es") 
    print("Refreshed")
def refresh(event):
    refreshtwo()

def send(server_ip, message):
    global out, chat_log, send_error
    port = 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((server_ip, port))
        if message != "//es":
            message = "Ducky: " + message
        client_socket.send(message.encode())
        response = b""
        while True:
            part = client_socket.recv(1024)
            if not part:
                break
            response += part
        decoded = response.decode()
        print("From server:\n", decoded)
        if message.strip() == "//es" or message.strip() == "Ducky: //es":
            chat_log = decoded
            send_error = False
    except Exception as e:
        print("Send error:", e)
        send_error = True
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

def update_window():
    global message, cwidth, cheight, c1, chat_log, change_check
    cheight = window.winfo_height() - 50
    cwidth = window.winfo_width() - 15
    

    if change_check != str(cwidth)+str(cheight):
        # Buttons
        b1 = Button(window, text="send", height=1, width=5, command=click)
        b1.grid(row=1, column=1,padx=5,pady=5)
        
        b2 = Button(window, text="refresh", height=1, width=5, command=refreshtwo)
        b2.grid(row=1, column=2,padx=5,pady=5)
                
        # Text entry
        e1 = Entry(window, textvariable=guiout, width=50)
        e1.grid(row=1, column=0, sticky="ew",padx=5,pady=5)
        
    else:
        pass
    change_check= str(cwidth)+str(cheight)
    
    error_message = "server not found\n\ncommon issues:\nthe server may currently be offline \nthe server ip in your app is incorrect\nyou may not be connected to the name network as the server\n\n please see your administrator"
    c1 = Canvas(window, width=cwidth, height=cheight-35)
    c1.place(x=15,y=15)
    if send_error == True:
            c1.create_text(5, 5, anchor="nw", text=error_message, fill="black", font=("Courier", 10), width=cwidth - 10)
    else:
        c1.create_text(5, 5, anchor="nw", text=chat_log, fill="black", font=("Courier", 10), width=cwidth - 10)

    window.after(1000, update_window)

b1 = Button(window, text="send", height=1, width=5, command=click)
b1.grid(row=1, column=1,padx=5,pady=5)

b2 = Button(window, text="refresh", height=1, width=5, command=refreshtwo)
b2.grid(row=1, column=2,padx=5,pady=5)
        
# Text entry
e1 = Entry(window, textvariable=guiout, width=50)
e1.grid(row=1, column=0, sticky="ew",padx=5,pady=5)

# Key bindings
window.bind('<Return>', enter)

# Initial GUI update
window.after(100, update_window)
window.mainloop()
