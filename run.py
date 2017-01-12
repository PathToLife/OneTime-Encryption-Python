import random, string, time
from datetime import datetime

class OneTimeEncryption:
    def __init__(self):
        pass

    def makeOneTimePad(self,fileName):
        file_open = open(fileName + datetime.now().strftime("-%d-%m-%y.onetime") + ".txt","w")
        for i in range(0,20):
            file_open.write(''.join([random.choice(string.ascii_lowercase + string.digits) for i in range(0,80)]) + \
            "\n")
        print("Created", file_open.name)
        file_open.close()


encrypt1 = OneTimeEncryption()

encrypt1.makeOneTimePad("Test")
