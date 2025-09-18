from tkinter import *

def account_setup():
    setup_window = Tk()
    setup_window.geometry("595x425")
    setup_window.title("Account Setup")

    username = StringVar()
    server_ip = StringVar()

    setup_window.columnconfigure(0, weight=1)
    setup_window.columnconfigure(1, weight=1)
    setup_window.columnconfigure(2, weight=1)
    
    try:
        with open("account/config.txt", "r") as f:
            lines = f.read().splitlines()
            if len(lines) >= 2:
                username.set(lines[0])
                server_ip.set(lines[1])
    except FileNotFoundError:
        pass 

    # Labels
    Label(setup_window, text="Display Name").grid(row=1, column=1)
    Label(setup_window, text="Server IP").grid(row=3, column=1)

    # Entry fields
    Entry(setup_window, textvariable=username).grid(row=2, column=1)
    Entry(setup_window, textvariable=server_ip).grid(row=4, column=1)

    # Connect function defined inside so it can access variables
    def connect():
        name = username.get()
        ip = server_ip.get()

        if name.strip() == "" or ip.strip() == "":
            error_label.config(text="Please enter both a username and server IP")
            return

        with open("account/config.txt", "w") as f:
            f.write(name + "\n" + ip)

        setup_window.destroy()

    # Connect button
    Button(setup_window, text="Connect", command=connect).place(x=500, y=370)

    # Error message label
    error_label = Label(setup_window, text="", fg="red")
    error_label.place(x=20, y=370)

    setup_window.mainloop()


