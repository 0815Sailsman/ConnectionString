import re
from urllib.parse import unquote
import sys
from datetime import datetime
import os
import json


class ConnectionString:
    def __init__(self):
        self.connectionString = ""
        self.decoded_string = dict()
        self.parts = list()
        self.sendParts = dict()
        self.receiveParts = dict()

    # This is the main method of the script. It takes the JSON-String entered and
    # stores the split and decoded values contained in two dictionaries.
    def json_decode(self):
        # Do a json decode
        self.decoded_string = json.loads(self.connectionString)

        # Transfer the already split values from the dictionary into a list
        for key in self.decoded_string:
            self.parts.append(re.split('[@/:]', self.decoded_string[key][8:]))

        # Decode the URL-Encoding in the Keys
        self.parts[0][1] = unquote(self.parts[0][1])
        self.parts[1][1] = unquote(self.parts[1][1])

        # Concatenate the last URL part we split earlier
        for i in range(len(self.parts)):
            for a in range(len(self.parts[i])):
                if a >= 4:
                    self.parts[i][3] = self.parts[i][3] + "/" + self.parts[i][a]

        # Remove the entries we just appended to the 4th index
        del self.parts[0][4:]
        del self.parts[1][4:]

        # Put all of the values into dictionaries
        self.sendParts["sendKeyName"] = self.parts[0][0]
        self.sendParts["sendKey"] = self.parts[0][1]
        self.sendParts["host"] = self.parts[0][2]
        self.sendParts["sendName"] = self.parts[0][3]

        self.receiveParts["receiveKeyName"] = self.parts[1][0]
        self.receiveParts["receiveKey"] = self.parts[1][1]
        self.receiveParts["host"] = self.parts[1][2]
        self.receiveParts["receiveName"] = self.parts[1][3]

    # This method exports the sorted values into a txt-file if the user wants this and may terminate the application.
    def export(self, do_file_export=1, do_quit=0):
        # If the checkbox for file-exports is ticked
        if do_file_export == 1:

            # Check if the exported Files directory exists and create it if necessary
            if not os.path.exists("exportedFiles"):
                os.mkdir("exportedFiles")

            # Create a string out of the current datetime for the filename.
            now = datetime.now()
            datetime_string = now.strftime("%d-%m-%Y--%H-%M-%S")

            # Creates a txt-file named with the datetime and opens it in write-mode.
            f = open("exportedFiles/SortedConnectionString" + datetime_string + ".txt", "w")

            # Writes every value with its key into the text file and flushes the data instantly.
            f.write("SEND PARTS:\n")
            for key in self.sendParts:
                f.write(key + "  ->  " + self.sendParts[key] + "\n")
            f.write("\n\nRECEIVE PARTS:\n")
            for key in self.receiveParts:
                f.write(key + "  ->  " + self.receiveParts[key] + "\n")
            f.close()

        # If the checkbox for quit after-decode is ticked
        if do_quit == 1:
            sys.exit()

    # This is the go-to method called by the GUI to start the whole process.
    def go(self, input_text, do_file_export, do_quit):
        self.connectionString = input_text
        self.json_decode()
        self.export(do_file_export, do_quit)
        return self.sendParts, self.receiveParts
