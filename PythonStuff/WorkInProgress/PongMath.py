import random
from time import sleep

P1Y = 4
P2Y = 4
BallX = 20 #ranges from 1 to 32
BallY = 4 #ranges from 1 to 8
Contact1 = False
Contact2 = False
BallDir = random.randint(0, 7)
BallSpeed = 1 #1 PPS
P1Score = 0
P2Score = 0

upDirs    =  [0, 1, 2]
rightDirs =  [2, 3, 4]
leftDirs  =  [0, 7, 6]
downDirs  =  [6, 5, 4]
#BallDirs
# 0  1  2
# 7     3
# 6  5  4
def drawPixel(x, y):
    #print("Dreweds X: " + str(x) + " Y: " + str(y))
    pass
def clearPixel(x, y):
    #print("cleared X: " + str(x) + " Y: " + str(y))
    pass
def UpdateBallDir():
    global Contact1
    global Contact2
    global BallDir
    global BallY
    global leftDirs
    global rightDirs
    if Contact1:
        BallDir = rightDirs[random.randint(0, 2)]
    elif Contact2:
        BallDir = leftDirs[random.randint(0, 2)]
    if BallY == 8 and BallDir in upDirs:
        if BallDir in rightDirs:
            BallDir = 4
        elif BallDir in leftDirs:
            BallDir = 6
    elif BallY == 1 and BallDir in downDirs:
        if BallDir in rightDirs:
            BallDir = 2
        elif BallDir in leftDirs:
            BallDir = 0
def drawPaddle(player, y):
    if player == 1:
        drawPixel(1, y - 1)
        drawPixel(1, y)
        drawPixel(1, y + 1)
    elif player == 2:
        drawPixel(32, y - 1)
        drawPixel(32, y)
        drawPixel(32, y + 1)
def moveBall(dir, speed):
    #BallDirs
    # 0  1  2
    # 7     3
    # 6  5  4
    global BallX
    global BallY
    if dir == 0:
        BallX = BallX - speed
        BallY = BallY + speed
    elif dir == 1:
        BallY = BallY + speed
    elif dir == 2:
        BallX = BallX + speed
        BallY = BallY + speed
    elif dir == 3:
        BallX = BallX + speed
    elif dir == 4:
        BallX = BallX + speed
        BallY = BallY - speed
    elif dir == 5:
        BallY = BallY - speed
    elif dir == 6:
        BallX = BallX - speed
        BallY = BallY - speed
    elif dir == 7:
        BallX = BallX - speed
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

        
while True:
    UpdateBallDir()
    clearPixel(BallX, BallY)
    moveBall(BallDir, BallSpeed)
    drawPixel(BallX, BallY)
    if BallX == 1:
        Contact1 = True
        if not BallY in range(P1Y - 1, P1Y + 1):
            P2Score += 1
    else:
        Contact1 = False

    if BallX == 32:
        Contact2 = True
        if not BallY in range(P2Y - 1, P2Y + 1):
            P1Score += 1
    else:
        Contact2 = False
    print("Dir: " + dirToEnglish(BallDir))
    print("X: " + str(BallX) + " Y: " + str(BallY))
    print("P1: " + str(P1Score) + " P2: " + str(P2Score))
    if not BallX in range(0, 33):
        print("BallX: " + str(BallX) + " out of Range!")
        exit()
    elif not BallY in range(0, 33):
        print("BallY: " + str(BallY) + " out of range!")
        exit()
    sleep(0.01)

    #drawPaddle(1,)


    
