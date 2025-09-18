import socket
import threading
from time import sleep
from tkinter import *
from tkinter import ttk
import splash_screen
import account

host = "0.0.0.0"
port = 12345
message = ""
out = ""
cwidth = ""
cheight = ""
chat_log = ""
passn = True
change_check = ""
send_error = False

account.account_setup()
sleep(0.5)
splash_screen.start_load()

# GUI setup
window = Tk()
window.title("Chat Client")
window.geometry("700x800")
window.configure(bg="#f2f2f2")

# Global tkinter variables
server_ip = StringVar()
username = StringVar()
guiout = StringVar()

try:
    with open("account/config.txt", "r") as f:
        lines = f.read().splitlines()
        if len(lines) >= 2:
            username.set(lines[0])
            server_ip.set(lines[1])
            username = username.get()
            server_ip = server_ip.get()
except FileNotFoundError:
    pass


# define functions
def click():
    global message, guiout
    message = guiout.get()
    print("Sending:", message)
    send(server_ip, message)
    entry_message.delete(0, END)
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
            message = username + ": " + message
        client_socket.send(message.encode())
        response = b""
        while True:
            part = client_socket.recv(1024)
            if not part:
                break
            response += part
        decoded = response.decode()
        print("From server:\n", decoded)
        if message.strip() == "//es" or message.strip() == f"{username}: //es":
            chat_log = decoded
            send_error = False
    except Exception as e:
        print("Send error:", e)
        send_error = True
    finally:
        client_socket.close()


#Threaded Receiver (optional)
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

# threading.Thread(target=rec, daemon=True).start()


# GUI parts
frame_top = Frame(window, bg="#f2f2f2")
frame_top.pack(fill=BOTH, expand=True, padx=10, pady=10)

chat_canvas = Canvas(frame_top, bg="white", highlightthickness=1, relief=RIDGE)
chat_scrollbar = Scrollbar(frame_top, orient=VERTICAL, command=chat_canvas.yview)
chat_frame = Frame(chat_canvas, bg="white")

chat_frame.bind(
    "<Configure>",
    lambda e: chat_canvas.configure(scrollregion=chat_canvas.bbox("all"))
)

chat_canvas.create_window((0, 0), window=chat_frame, anchor="nw")
chat_canvas.configure(yscrollcommand=chat_scrollbar.set)

chat_canvas.pack(side=LEFT, fill=BOTH, expand=True)
chat_scrollbar.pack(side=RIGHT, fill=Y)

frame_bottom = Frame(window, bg="#e6e6e6")
frame_bottom.pack(fill=X, side=BOTTOM, padx=10, pady=10)

entry_message = Entry(frame_bottom, textvariable=guiout, font=("Arial", 12), width=50)
entry_message.pack(side=LEFT, padx=5, pady=5, fill=X, expand=True)
entry_message.bind('<Return>', enter)

btn_send = Button(frame_bottom, text="Send", width=10, bg="#4CAF50", fg="white", command=click)
btn_send.pack(side=LEFT, padx=5)

btn_refresh = Button(frame_bottom, text="Refresh", width=10, bg="#2196F3", fg="white", command=refreshtwo)
btn_refresh.pack(side=LEFT, padx=5)

error_label = Label(frame_top, text="", fg="red", bg="white", font=("Arial", 10), justify=LEFT)
error_label.pack(pady=5, anchor=W)


#Update Canvas
def update_window():
    global chat_log, send_error
    for widget in chat_frame.winfo_children():
        widget.destroy()

    if send_error:
        error_text = (
            "⚠ Server not found\n\n"
            "Common issues:\n"
            "• Server is offline\n"
            "• IP is incorrect\n"
            "• Not on the same network\n\n"
            "Please contact your administrator."
        )
        Label(chat_frame, text=error_text, font=("Arial", 11), fg="red", bg="white", justify=LEFT).pack(padx=10, pady=10, anchor="w")
    else:
        lines = chat_log.strip().split("\n")
        for line in lines:
            Label(chat_frame, text=line, font=("Courier", 11), anchor="w", bg="white", wraplength=650, justify=LEFT).pack(padx=10, anchor="w")

    window.after(3000, update_window)


# Start UI
window.after(100, update_window)
window.mainloop()
