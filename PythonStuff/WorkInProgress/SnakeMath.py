from time import sleep
import random

screenLength = 32
screenWidth = 8

headY = screenWidth/2
headX = screenLength/2
headY = int(headY)
headX = int(headX)
headPos = [headX, headY]
snakeDir = random.randint(0, 7)
SnakeLength = 1
score = 0

appleX = 0
appleY = 0
applePos = [appleX, appleY]

allDirs   =  [0, 1, 2, 3, 4, 5, 6, 7]
upDirs    =  [0, 1, 2]
rightDirs =  [2, 3, 4]
leftDirs  =  [0, 7, 6]
downDirs  =  [6, 5, 4]

#HeadDirs
# 0  1  2
# 7     3
# 6  5  4

def drawPixel(x, y):
    #draw a whitePixel
    #print("Dreweds X: " + str(x) + " Y: " + str(y))
    pass
def redPixel(x, y):
    #draw a red pixel
    pass
def clearPixel(z,x,y):
    #print("cleared X: " + str(x) + " Y: " + str(y))
    pass
def killSnake():
    #end the game here
    print("You lost.")
    print("Therefore, you are a loser.")
    sleep(1)
    exit()
def getApplePos():
    return [random.randint(0, screenLength), random.randint(0, screenWidth)]
def updateHeadPos():
    global headX
    global headY
    global headPos
    global screenLength
    global snakeDir
    if headX == 0 and snakeDir in leftDirs and headX == screenLength and snakeDir in rightDirs:
        killSnake()
    elif headY == 0 and snakeDir in downDirs or headY == screenWidth and snakeDir in upDirs:
        killSnake()
    elif snakeDir == 0:
        headX -= 1
        headY += 1
    elif snakeDir == 1:
        headY += 1
    elif snakeDir == 2:
        headX += 1
        headY += 1
    elif snakeDir == 3:
        headX += 1
    elif snakeDir == 4:
        headX += 1
        headY -= 1
    elif snakeDir == 5:
        headY -= 1
    elif snakeDir == 6:
        headX -= 1
        headY -= 1
    elif snakeDir == 7:
        headX -= 1
def updateSnakeDir(testMode):
    global snakeDir
    global appleX
    global appleY
    global headX
    global headY
    if testMode == 1:
        snakeDir = random.randint(0, 7)
    elif testMode == 2:
        #point towards apple
        #HeadDirs
        # 0  1  2
        # 7     3
        # 6  5  4
        if appleX < headX and appleY > headY:
            snakeDir = 0
            print(dirToEnglish(snakeDir))
        elif appleX == headX and appleY > headY:
            snakeDir = 1
        elif appleX > headX and appleY > headY:
            snakeDir = 2
        elif appleX > headX and appleY == headY:
            snakeDir = 3
        elif appleX > headX and appleY < headY:
            snakeDir = 4
        elif appleX == headX and appleY < headY:
            snakeDir = 5
        elif appleX < headX and appleY < headX:
            snakeDir = 6
        elif appleX < headX and appleY == headY:
            snakeDir = 7
    elif testMode == 3:
        #immediatly kill urself on snake head
        pass
    else:
        for i in range(len(allDirs)):
            if allDirs[i] == snakeDir and i == len(allDirs) - 1:
                snakeDir = allDirs[0]
            elif allDirs[i] == snakeDir:
                snakeDir = allDirs[snakeDir + 1]
def dirToEnglish(dir):
    #BallDirs
    # 0  1  2
    # 7     3
    # 6  5  4
    if dir == 0:
        return "Up Left"
    elif dir == 1:
        return "Up"
    elif dir == 2:
        return "Up Right"
    elif dir == 3:
        return "Right"
    elif dir == 4:
        return "Down Right"
    elif dir == 5:
        return "Down"
    elif dir == 6:
        return "Down Left"
    elif dir == 7:
        return "Left"
applePos = getApplePos()
print(applePos)
while True:
    updateHeadPos()
    updateSnakeDir(1)
    headPos = [headX, headY]
    drawPixel(headPos[0], headPos[1])
    print("Dir: " + dirToEnglish(snakeDir) + " X: " + str(headX) + " Y: " + str(headY) + " Score: " + str(score))
    if headPos == applePos:
        applePos = getApplePos()
        drawPixel(applePos[0], applePos[1])
        score += 1
    sleep(0.1)
