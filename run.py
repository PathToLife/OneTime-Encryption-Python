import time
from datetime import datetime

class OneTimeEncryption:
    def __init__(self):
        print("Created")

    def makeOneTimePad(self,fileName):
        file_open = open(fileName + datetime.now().strftime("-%d-%m-%y") + ".txt","w")
        file_open.write("test")
        file_open.close()

encrypt1 = OneTimeEncryption()

encrypt1.makeOneTimePad("Test")