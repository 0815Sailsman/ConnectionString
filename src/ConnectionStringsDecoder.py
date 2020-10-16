# Connection String Decoding
from connectionString import ConnectionString
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import sys
import os


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def pass_input():
    cs.go(e1.get("1.0", END), var1.get())


cs = ConnectionString()
master = Tk()
master.title("ConnectionStringsDecoder")

master.iconbitmap(resource_path("icon.ico"))
master.geometry("700x300")

input_label = Label(master, text="Input: ")
input_label.grid(row=0)
input_label.place(x=15, y=25)

e1 = ScrolledText(master)
e1.grid(row=0, column=1)
e1.place(x=75, y=25, width=550, height=160)

var1 = IntVar(value=1)
file_checkbox = Checkbutton(master, text="Export into file", variable=var1)
file_checkbox.grid(row=1, column=1, sticky=W, pady=4)
file_checkbox.place(x=40, y=200)

decode_button = Button(master, text='Decode', command=pass_input)
decode_button.grid(row=3, column=0, sticky=W, pady=4)
decode_button.place(x=25, y=250, width=150)

quit_button = Button(master, text='Quit', command=master.quit)
quit_button.grid(row=3, column=1, sticky=W, pady=4)
quit_button.place(x=200, y=250, width=150)

mainloop()
