import re
from urllib.parse import unquote
import sys
from datetime import datetime
import os


class ConnectionString:
    def __init__(self):
        self.connectionString = ""
        self.parts = list()
        self.sendParts = dict()
        self.receiveParts = dict()

    def get_string(self):
        self.connectionString = input("Enter the string you want to decode:\n")

    def split(self):
        self.connectionString = self.connectionString\
            .replace('{', '')\
            .replace('}', '')\
            .replace('\"', '')\
            .replace("//", '')
        self.parts = self.connectionString.split(',')
        for i in range(len(self.parts)):
            self.parts[i] = re.split('[@/:]', self.parts[i])

        for i in range(len(self.parts)):
            dif = 0
            for a in range(len(self.parts[i])):
                if self.parts[i][a-dif] == "amqps":
                    self.parts[i].pop(a-dif)
                    dif = 1

        temp = ""
        for i in self.parts[1]:
            if self.parts[1].index(i) > 3:
                temp = temp + i + "/"
        temp = temp[:-1]
        del self.parts[1][5:]
        self.parts[1][4] = temp

    def decode_key(self):
        for i in self.parts:
            i[2] = unquote(i[2])

    def label(self):
        for i in self.parts:
            if i[0] == "queueConnectionString":
                self.sendParts["sendKeyName"] = i[1]
                self.sendParts["sendKey"] = i[2]
                self.sendParts["host"] = i[3]
                self.sendParts["sendName"] = i[4]
            elif i[0] == "topicConnectionString":
                self.receiveParts["receiveKeyName"] = i[1]
                self.receiveParts["receiveKey"] = i[2]
                self.receiveParts["host"] = i[3]
                self.receiveParts["receiveName"] = i[4]

    def export(self, do_file_export=1, do_quit=0):
        if do_file_export == 1:
            now = datetime.now()
            # Check if the exported Files directory exists and create it if necessary
            if not os.path.exists("exportedFiles"):
                os.mkdir("exportedFiles")

            datetime_string = now.strftime("%d-%m-%Y--%H-%M-%S")
            f = open("exportedFiles/SortedConnectionString" + datetime_string + ".txt", "w")
            f.write("SEND PARTS:\n")
            for key in self.sendParts:
                f.write(key + "  ->  " + self.sendParts[key] + "\n")
            f.write("\n\nRECEIVE PARTS:\n")
            for key in self.receiveParts:
                f.write(key + "  ->  " + self.receiveParts[key] + "\n")
            f.close()
        if do_quit == 1:
            sys.exit()

    def go(self, input_text, do_file_export, do_quit):
        self.connectionString = input_text
        self.split()
        self.decode_key()
        self.label()
        self.export(do_file_export, do_quit)
        return self.sendParts, self.receiveParts
