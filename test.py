import time
import datetime
import random
import string

time.time()

list1 = [1,2,3]

print(sum(list1))

print(datetime.datetime.today())
print(datetime.datetime.now())

print (''.join( [random.choice(string.ascii_lowercase + string.digits) for i in range(0,200)] ))
