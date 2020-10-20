# Connection String Decoding
from connectionString import ConnectionString
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.font import BOLD
import sys
import os


# noinspection PyProtectedMember
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# noinspection PyAttributeOutsideInit
class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.cs = ConnectionString()

        self.master.title("ConnectionStringsDecoder")
        self.master.iconbitmap(resource_path("src/icon.ico"))
        self.master.geometry("700x600")

        self.sp_keyname_var = StringVar()
        self.sp_key_var = StringVar()
        self.sp_host_var = StringVar()
        self.sp_name_var = StringVar()
        self.rp_keyname_var = StringVar()
        self.rp_key_var = StringVar()
        self.rp_host_var = StringVar()
        self.rp_name_var = StringVar()

        self.file_checkbox_var = IntVar(value=1)
        self.exit_checkbox_var = IntVar(value=0)

        self.create_widgets()

    def create_widgets(self):
        # Text input label
        self.input_label = Label(self.master, text="Input: ")
        self.input_label.grid(row=0)
        self.input_label.place(x=15, y=25)

        # Text input
        self.textbox = ScrolledText(self.master)
        self.textbox.grid(row=0, column=1)
        self.textbox.place(x=75, y=25, width=550, height=160)

        # SendParts stuff
        self.sp_title_label = Label(self.master, text="Send Parts: ", font=BOLD)
        self.sp_title_label.grid(row=0)
        self.sp_title_label.place(x=15, y=200, width=150)

        self.sp_keyname_button = Button(self.master, text="sendKeyName: ",
                                        command=lambda: self.clipboard(self.sp_keyname_var.get()))
        self.sp_keyname_button.grid(row=0)
        self.sp_keyname_button.place(x=15, y=225, width=150)

        self.sp_keyname_label = Label(self.master, textvariable=self.sp_keyname_var, relief="ridge", anchor="w")
        self.sp_keyname_label.grid(row=0)
        self.sp_keyname_label.place(x=165, y=225, width=500)

        self.sp_key_button = Button(self.master, text="sendKey: ",
                                    command=lambda: self.clipboard(self.sp_key_var.get()))
        self.sp_key_button.grid(row=0)
        self.sp_key_button.place(x=15, y=250, width=150)

        self.sp_key_label = Label(self.master, textvariable=self.sp_key_var, relief="ridge", anchor="w")
        self.sp_key_label.grid(row=0)
        self.sp_key_label.place(x=165, y=250, width=500)

        self.sp_host_button = Button(self.master, text="Host: ",
                                     command=lambda: self.clipboard(self.sp_host_var.get()))
        self.sp_host_button.grid(row=0)
        self.sp_host_button.place(x=15, y=275, width=150)

        self.sp_host_label = Label(self.master, textvariable=self.sp_host_var, relief="ridge", anchor="w")
        self.sp_host_label.grid(row=0)
        self.sp_host_label.place(x=165, y=275, width=500)

        self.sp_name_button = Button(self.master, text="sendName: ",
                                     command=lambda: self.clipboard(self.sp_name_var.get()))
        self.sp_name_button.grid(row=0)
        self.sp_name_button.place(x=15, y=300, width=150)

        self.sp_name_label = Label(self.master, textvariable=self.sp_name_var, relief="ridge", anchor="w")
        self.sp_name_label.grid(row=0)
        self.sp_name_label.place(x=165, y=300, width=500)

        # ReceiveParts label
        self.rp_title_label = Label(self.master, text="Receive Parts: ", font=BOLD)
        self.rp_title_label.grid(row=0)
        self.rp_title_label.place(x=15, y=350, width=150)

        self.rp_keyname_button = Button(self.master, text="receiveKeyName: ",
                                        command=lambda: self.clipboard(self.rp_keyname_var.get()))
        self.rp_keyname_button.grid(row=0)
        self.rp_keyname_button.place(x=15, y=375, width=150)

        self.rp_keyname_label = Label(self.master, textvariable=self.rp_keyname_var, relief="ridge", anchor="w")
        self.rp_keyname_label.grid(row=0)
        self.rp_keyname_label.place(x=165, y=375, width=500)

        self.rp_key_button = Button(self.master, text="receiveKey: ",
                                    command=lambda: self.clipboard(self.rp_key_var.get()))
        self.rp_key_button.grid(row=0)
        self.rp_key_button.place(x=15, y=400, width=150)

        self.rp_key_label = Label(self.master, textvariable=self.rp_key_var, relief="ridge", anchor="w")
        self.rp_key_label.grid(row=0)
        self.rp_key_label.place(x=165, y=400, width=500)

        self.rp_host_button = Button(self.master, text="Host: ",
                                     command=lambda: self.clipboard(self.rp_host_var.get()))
        self.rp_host_button.grid(row=0)
        self.rp_host_button.place(x=15, y=425, width=150)

        self.rp_host_label = Label(self.master, textvariable=self.rp_host_var, relief="ridge", anchor="w")
        self.rp_host_label.grid(row=0)
        self.rp_host_label.place(x=165, y=425, width=500)

        self.rp_name_button = Button(self.master, text="receiveName: ",
                                     command=lambda: self.clipboard(self.rp_name_var.get()))
        self.rp_name_button.grid(row=0)
        self.rp_name_button.place(x=15, y=450, width=150)

        self.rp_name_label = Label(self.master, textvariable=self.rp_name_var, relief="ridge", anchor="w")
        self.rp_name_label.grid(row=0)
        self.rp_name_label.place(x=165, y=450, width=500)

        # File Export checkbox
        self.file_checkbox = Checkbutton(self.master, text="Export into file", variable=self.file_checkbox_var)
        self.file_checkbox.grid(row=1, column=1, sticky=W, pady=4)
        self.file_checkbox.place(x=40, y=500)

        # Quit checkbox
        self.exit_checkbox = Checkbutton(self.master, text="Quit after decode", variable=self.exit_checkbox_var)
        self.exit_checkbox.grid(row=1, column=1, sticky=W, pady=4)
        self.exit_checkbox.place(x=175, y=500)

        # Decode Button
        self.decode_button = Button(self.master, text='Decode', command=self.pass_input)
        self.decode_button.grid(row=3, column=0, sticky=W, pady=4)
        self.decode_button.place(x=25, y=550, width=150)

        # Quit Button
        self.quit_button = Button(self.master, text='Quit', command=self.master.quit)
        self.quit_button.grid(row=3, column=1, sticky=W, pady=4)
        self.quit_button.place(x=200, y=550, width=150)

    def clipboard(self, text):
        self.master.clipboard_clear()
        self.master.clipboard_append(text)
        self.master.update()

    def pass_input(self):
        send_parts, receive_parts = self.cs.go(self.textbox.get("1.0", END),
                                               self.file_checkbox_var.get(), self.exit_checkbox_var.get())
        self.sp_keyname_var.set(send_parts["sendKeyName"])
        self.sp_key_var.set(send_parts["sendKey"])
        self.sp_host_var.set(send_parts["host"])
        self.sp_name_var.set(send_parts["sendName"])

        self.rp_keyname_var.set(receive_parts["receiveKeyName"])
        self.rp_key_var.set(receive_parts["receiveKey"])
        self.rp_host_var.set(receive_parts["host"])
        self.rp_name_var.set(receive_parts["receiveName"])


# General GUI settings
root = Tk()
app = Application(master=root)
app.mainloop()
