from time import sleep

snakelength = 1
foodX = None
foodY = None
snakeDir = 1
toclear = (0, 0)
#   1
# 4   2
#   3
Invincibility = True
snakeArray = ((0, 0))
exampleSnakeArray = ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5))

def drawPixel(x, y):
    print("Drew Pixel X: " + str(x) + " Y: " + str(y))

def clearPixel(x, y):
    print("Cleared Pixel X: " + str(x) + " Y: " + str(y))

def drawSnake(SnakeArray):
    global toclear
    for i in range(len(SnakeArray)):
        drawPixel(SnakeArray[i][0], SnakeArray[i][1])
    toclear = SnakeArray[-1]

def updateArray():
    global snakeArray
    global snakelength
    

def clearEnd():
    clearPixel(toclear[0], toclear[1])


drawSnake(exampleSnakeArray)
clearEnd()
