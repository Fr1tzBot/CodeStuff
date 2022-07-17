from random import randint

def constrain(value: int, minimum: int, maximum: int) -> int:
    """Return a value constrained to an inclusive range"""
    if value < minimum:
        return minimum
    elif value > maximum:
        return maximum
    else:
        return value

class pong:
    class ball:
        contact1 = False
        contact2 = False
    class p1:
        score = 0
    class p2:
        score = 0
    def __init__(self, xres = 15, yres=15, pause=50, speed=1):
        """Constructor Function for pong class"""
        brain.clear()
        #initialize constant direction info
        self.blankRow = []
        for i in range(xres):
            self.blankRow.append(0)
        self.upDirs    =  [0, 1, 2]
        self.rightDirs =  [2, 3, 4]
        self.leftDirs  =  [0, 7, 6]
        self.downDirs  =  [6, 5, 4]
        self.screen = []
        self.pause = pause
        self.ball.speed = speed #1 pixel/s sideways or √2 pixel/s diagonal
        self.ball.direction = 3
        #set the xres and yres to the provided values
        self.xres = xres
        self.yres = yres
        #initialize the ball and pattles around the middle of the screen
        self.ball.x = int(xres/2)
        self.ball.y = int(yres/2)
        self.p1.y = int(yres/2)
        self.p2.y = int(yres/2)
    def p(self, text: str) -> None:
        """does what the standard print() does in vexvr"""
        brain.print(text)
        brain.new_line()
    def render(self, screen) -> None:
        """Draw the pixels of a given screen list in the print window"""
        #function to clear the screen and then draw thew pixels in the screen list
        brain.clear()
        for i in screen:
            if i == self.blankRow:
                brain.new_line()
                continue
            for j in i:
                brain.print("█") if j==1 else brain.print("-")
            brain.new_line()
    def drawPixel(self, x: int, y: int, screen: list) -> list:
        """Returns an edited screen list with a given pixel turned on"""
        #function to update the screen list and render the updated list
        screen[constrain(y, 0, self.yres-1)][constrain(x, 0, self.xres-1)] = 1
        return screen
        #p("Dreweds X: " + str(x) + " Y: " + str(y))
    def clearPixel(self, x: int, y: int, screen) -> None:
        """Returns an edited screen list with a given pixel turned off"""
        #function to update the screen list and render the updated list
        screen[constrain(y, 0, self.yres)][constrain(x, 0, self.xres)] = 0
        return screen
        #p("cleared X: " + str(x) + " Y: " + str(y))
    def updateBallDir(self) -> None:
        """Change the balls direction based on if it is touching a border"""
        #function to update the ball's direction
        ballDir = self.ball.direction
        ballY = self.ball.y

        leftDirs = self.leftDirs
        rightDirs = self.rightDirs
        upDirs = self.upDirs
        downDirs = self.downDirs

        yres = self.yres

        #if it's touching either wall, bounce off at a random angle
        if self.ball.contact1:
            ballDir = rightDirs[randint(0, 2)]
        elif self.ball.contact2:
            ballDir = leftDirs[randint(0, 2)]
        if ballY == yres-1 and ballDir in upDirs:
            if ballDir in rightDirs:
                ballDir = 4
            elif ballDir in leftDirs:
                ballDir = 6
        elif ballY == 0 and ballDir in downDirs:
            if ballDir in rightDirs:
                ballDir = 2
            elif ballDir in leftDirs:
                ballDir = 0
        self.ball.direction = ballDir
        #ballDirs
        # 0  1  2
        # 7     3
        # 6  5  4
    def drawPaddle(self, player: int, y: int, screen: list) -> list:
        """Returns a screen list with pixels turned on for the specified paddle"""
        drawPixel = self.drawPixel
        xres = self.xres
        if player == 1:
            x = 0
        elif player == 2:
            x = xres-1
        screen = drawPixel(x, y - 1, screen)
        screen = drawPixel(x, y, screen)
        screen = drawPixel(x, y + 1, screen)
        return screen
    def moveBall(self, direction: int, speed: int) -> list:
        """Returns x and y values altered by the provided speed value"""
        #ballDirs
        # 0  1  2
        # 7     3
        # 6  5  4
        ballX = self.ball.x
        ballY = self.ball.y
        #move the ball based on the direction
        if direction == 0:
            ballX -= speed
            ballY += speed
        elif direction == 1:
            ballY += speed
        elif direction == 2:
            ballX += speed
            ballY += speed
        elif direction == 3:
            ballX += speed
        elif direction == 4:
            ballX += speed
            ballY -= speed
        elif direction == 5:
            ballY -= speed
        elif direction == 6:
            ballX -= speed
            ballY -= speed
        elif direction == 7:
            ballX -= speed
        return ballX, ballY
    def main(self):
        """The main function in the pong class"""
        #grab functions from parent class
        updateBallDir = self.updateBallDir
        clearPixel = self.clearPixel
        moveBall = self.moveBall
        drawPixel = self.drawPixel
        drawPaddle = self.drawPaddle
        #get constant variables
        xres = self.xres
        yres = self.yres
        pause = self.pause

        #set up screen 2d list
        for i in range(yres):
            self.screen.append([])
            for j in range(xres):
                self.screen[i].append(0)
        
        while True:
            updateBallDir()
            self.screen = clearPixel(self.ball.x, self.ball.y, self.screen)
            self.ball.x, self.ball.y = moveBall(self.ball.direction, self.ball.speed)
            self.screen = drawPixel(self.ball.x, self.ball.y, self.screen)
            #self.screen = drawPaddle(1, self.p1.y, self.screen)
            #self.screen = drawPaddle(2, self.p2.y, self.screen)
            if self.ball.x == 0: #if ball is on the far left of the screen
                self.ball.contact1 = True #set the corresponding contact variable to true
                if not self.ball.y in range(self.p1.y - 1, self.p1.y + 2): #if the ball did not hit the paddle, add 1 point to the score
                    self.p2.score += 1
            else: #otherwise, ensure the corresponding contact variable is false
                self.ball.contact1 = False
            if self.ball.x == xres-1: #if ball is on the far right of the screen
                self.ball.contact2 = True #set the corresponding contact variable to true
                if not self.ball.y in range(self.p2.y - 1, self.p2.y + 2):#if the ball did not hit the paddle, add 1 point to the score
                    self.p1.score += 1
            else: #otherwise, ensure the corresponding contact variable is false
                self.ball.contact2 = False
            self.render(self.screen)
            wait(pause, MSEC)
#1000 ms=1 fps  100 ms=10 fps  50 ms = 20 fps  10 ms=100 fps  17 ms~=60 fps  33 ms~=30 fps        
thread = pong(xres=46, yres=17, pause=50, speed=1)
vr_thread(thread.main())
