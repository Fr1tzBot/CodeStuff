from time import sleep
from random import getrandbits

lower = False
upper = False
lowerPrev = False
upperPrev = False
ballsHeld = 0

stateList = ["empty", "oneBall", "full"]
currentState = "empty"
events = ["collect 1", "eject 1"]
lastEvent = "idle"

def lowerRising() -> bool:
    return (not lowerPrev) and lower

def upperFalling() -> bool:
    return (not upper) and lowerPrev

def randBool() -> bool:
    return bool(getrandbits(1))

def setState(state: str, event: str) -> None:
    global currentState
    global lastEvent
    global ballsHeld

    if state == "empty":
        currentState = "empty"
        ballsHeld = 0
    elif state == "oneBall":
        currentState = "oneBall"
        ballsHeld = 1
    elif state == "full":
        currentState = "full"
        ballsHeld = 2
    lastEvent = event


while True:
    upper = randBool()
    lower = randBool()

    if currentState == "empty":
        if lowerRising():
            setState("oneBall", "collect 1")
        else:
            lastEvent = "idle"
    elif currentState == "oneBall":
        if lowerRising():
            setState("full", "collect 1")
        elif upperFalling():
            setState("empty", "eject 1")
        else:
            lastEvent = "idle"
    elif currentState == "full":
        if upperFalling():
            setState("oneBall", "eject 1")
        else:
            lastEvent = "idle"


    lowerPrev = lower
    upperPrev = upper

    print("\nState: " + currentState + "\nLast Event: " + lastEvent + "\nBalls: " + str(ballsHeld))
    sleep(1)
