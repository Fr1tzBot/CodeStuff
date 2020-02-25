from time import sleep
import time
import random
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

target = 50
Kp = 5
data = 0
Power = 0
error = 0

def getData():
    global data
    if random.randint(0, 100) == 69:
        print("NOICE!")
        data = data * 2
        if data > 100:
            data = 100
    data = Power + data
    return data
def setCondition(error, Kp):
    global Power
    Power = Kp*error
for i in range(100):
    if i == 0:
        start_time = time.time()
    error = target - getData()
    setCondition(error, Kp)
    print("E: " + str(error) + " Power?: " + str(Power) + " Data: " + str(data))
    if data < 0 or data > 100:
        print("Out Of Bounds Error 969")
        break
    plt.plot(time.time() - start_time, data, 'o', color='black')
    #sleep(0.1)
plt.show()
    
