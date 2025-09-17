from tkinter import *
from time import sleep

loading_image_path = "images/loading_image.png"

load_window = None
load_graphic = None

def start_load():
    load_window = Tk()
    load_window.geometry("595x425")
    load_window.title("Loading...")

    
    load_graphic = PhotoImage(file=loading_image_path)
    label = Label(load_window, image=load_graphic)
    label.pack()

    load_window.after(5000, load_window.destroy)
    
    load_window.mainloop()

#load_window.mainloop()
