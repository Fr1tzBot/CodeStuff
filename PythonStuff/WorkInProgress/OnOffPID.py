#%matplotlib inline
from time import sleep
import time
import random
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

target = 5
Kp = 5
data = 0
isOn = False
error = 0

def getData():
    global data
    #if random.randint(0, 100) == 69:
        #print("NOICE!")
        #data = data * 2
        #if data > 100:
            #data = 100
    if isOn:
        data += 1 #random.randint(1, 5)
    elif data == 0:
        pass
    else:
        data -= 1#random.randint(1, 5)
    return data
def setCondition(error, Kp):
    global isOn
    calc = Kp*error
    if calc > 0:
        isOn = True
    elif calc < 0:
        isOn = False
for i in range(100):
    if i == 0:
        start_time = time.time()
    error = target - getData()
    setCondition(error, Kp)
    #print("E: " + str(error) + " On?: " + str(isOn) + " Data: " + str(data))
    if data < 0 or data > 100:
        print("Out Of Bounds Error 969")
        exit()
    plt.plot(time.time() - start_time, data, 'o', color='black')

    #sleep(0.1)
plt.show()
    
