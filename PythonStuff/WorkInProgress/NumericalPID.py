from time import sleep
import time
import random
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

target = 50
Kp = 5
data = 0
Power = False
error = 0

def getData():
    global data
    if random.randint(0, 100) == 69:
        print("NOICE!")
        data = data * 2
        if data > 100:
            data = 100
    elif Power:
        data += random.randint(1, 2)
    elif data == 0:
        pass
    else:
        data -= random.randint(1, 2)
    return data
def setCondition(error, Kp):
    global Power
    calc = Kp*error
    power = calc
for i in range(100):
    if i == 0:
        start_time = time.time()
    error = target - getData()
    setCondition(error, Kp)
    print("E: " + str(error) + " On?: " + str(Power) + " Data: " + str(data))
    if data < 0 or data > 100:
        print("Out Of Bounds Error 969")
        exit()
    plt.plot(time.time() - start_time, data, 'o', color='black')
    #sleep(0.1)
plt.show()
    
