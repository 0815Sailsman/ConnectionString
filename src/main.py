# Connection String Decoding
from connectionString import ConnectionString
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.font import BOLD
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
    sendParts, receiveParts = cs.go(e1.get("1.0", END), var1.get(), var2.get())
    sp_keyname_var.set(sendParts["sendKeyName"])
    sp_key_var.set(sendParts["sendKey"])
    sp_host_var.set(sendParts["host"])
    sp_name_var.set(sendParts["sendName"])

    rp_keyname_var.set(receiveParts["receiveKeyName"])
    rp_key_var.set(receiveParts["receiveKey"])
    rp_host_var.set(receiveParts["host"])
    rp_name_var.set(receiveParts["receiveName"])


def clipboard(master, text):
    master.clipboard_clear()
    master.clipboard_append(text)
    master.update()


# General GUI settings
cs = ConnectionString()
master = Tk()
master.title("ConnectionStringsDecoder")
master.iconbitmap(resource_path("src/icon.ico"))
master.geometry("700x600")

# Text input label
input_label = Label(master, text="Input: ")
input_label.grid(row=0)
input_label.place(x=15, y=25)

# Text input
e1 = ScrolledText(master)
e1.grid(row=0, column=1)
e1.place(x=75, y=25, width=550, height=160)

# SendParts stuff
sp_title_label = Label(master, text="Send Parts: ", font=BOLD)
sp_title_label.grid(row=0)
sp_title_label.place(x=15, y=200, width=150)


sp_keyname_button = Button(master, text="sendKeyName: ", command=lambda: clipboard(master, sp_keyname_var.get()))
sp_keyname_button.grid(row=0)
sp_keyname_button.place(x=15, y=225, width=150)

sp_keyname_var = StringVar()

sp_keyname_label = Label(master, textvariable=sp_keyname_var, relief="ridge", anchor="w")
sp_keyname_label.grid(row=0)
sp_keyname_label.place(x=165, y=225, width=500)


sp_key_button = Button(master, text="sendKey: ", command=lambda: clipboard(master, sp_key_var.get()))
sp_key_button.grid(row=0)
sp_key_button.place(x=15, y=250, width=150)

sp_key_var = StringVar()

sp_key_label = Label(master, textvariable=sp_key_var, relief="ridge", anchor="w")
sp_key_label.grid(row=0)
sp_key_label.place(x=165, y=250, width=500)


sp_host_button = Button(master, text="Host: ", command=lambda: clipboard(master, sp_host_var.get()))
sp_host_button.grid(row=0)
sp_host_button.place(x=15, y=275, width=150)

sp_host_var = StringVar()

sp_host_label = Label(master, textvariable=sp_host_var, relief="ridge", anchor="w")
sp_host_label.grid(row=0)
sp_host_label.place(x=165, y=275, width=500)


sp_name_button = Button(master, text="sendName: ", command=lambda: clipboard(master, sp_name_var.get()))
sp_name_button.grid(row=0)
sp_name_button.place(x=15, y=300, width=150)

sp_name_var = StringVar()

sp_name_label = Label(master, textvariable=sp_name_var, relief="ridge", anchor="w")
sp_name_label.grid(row=0)
sp_name_label.place(x=165, y=300, width=500)


# ReceiveParts label
rp_title_label = Label(master, text="Receive Parts: ", font=BOLD)
rp_title_label.grid(row=0)
rp_title_label.place(x=15, y=350, width=150)


rp_keyname_button = Button(master, text="receiveKeyName: ", command=lambda: clipboard(master, rp_keyname_var.get()))
rp_keyname_button.grid(row=0)
rp_keyname_button.place(x=15, y=375, width=150)

rp_keyname_var = StringVar()

rp_keyname_label = Label(master, textvariable=rp_keyname_var, relief="ridge", anchor="w")
rp_keyname_label.grid(row=0)
rp_keyname_label.place(x=165, y=375, width=500)


rp_key_button = Button(master, text="receiveKey: ", command=lambda: clipboard(master, rp_key_var.get()))
rp_key_button.grid(row=0)
rp_key_button.place(x=15, y=400, width=150)

rp_key_var = StringVar()

rp_key_label = Label(master, textvariable=rp_key_var, relief="ridge", anchor="w")
rp_key_label.grid(row=0)
rp_key_label.place(x=165, y=400, width=500)


rp_host_button = Button(master, text="Host: ", command=lambda: clipboard(master, rp_host_var.get()))
rp_host_button.grid(row=0)
rp_host_button.place(x=15, y=425, width=150)

rp_host_var = StringVar()

rp_host_label = Label(master, textvariable=rp_host_var, relief="ridge", anchor="w")
rp_host_label.grid(row=0)
rp_host_label.place(x=165, y=425, width=500)


rp_name_button = Button(master, text="receiveName: ", command=lambda: clipboard(master, rp_name_var.get()))
rp_name_button.grid(row=0)
rp_name_button.place(x=15, y=450, width=150)

rp_name_var = StringVar()

rp_name_label = Label(master, textvariable=rp_name_var, relief="ridge", anchor="w")
rp_name_label.grid(row=0)
rp_name_label.place(x=165, y=450, width=500)


# File Export checkbox
var1 = IntVar(value=1)
file_checkbox = Checkbutton(master, text="Export into file", variable=var1)
file_checkbox.grid(row=1, column=1, sticky=W, pady=4)
file_checkbox.place(x=40, y=500)

# Quit checkbox
var2 = IntVar(value=0)
exit_checkbox = Checkbutton(master, text="Quit after decode", variable=var2)
exit_checkbox.grid(row=1, column=1, sticky=W, pady=4)
exit_checkbox.place(x=175, y=500)

# Decode Button
decode_button = Button(master, text='Decode', command=pass_input)
decode_button.grid(row=3, column=0, sticky=W, pady=4)
decode_button.place(x=25, y=550, width=150)

# Quit Button
quit_button = Button(master, text='Quit', command=master.quit)
quit_button.grid(row=3, column=1, sticky=W, pady=4)
quit_button.place(x=200, y=550, width=150)

mainloop()
