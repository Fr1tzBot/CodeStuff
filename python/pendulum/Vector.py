import math

class Vector2d:
    x = float()
    y = float()

    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2d(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Vector2d(self.x * other.x, self.y * other.y)

    __rmul__ = __mul__

    def getMagnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)
    
    def getAngle(self) -> float:
        return math.atan2(self.y, self.x)
