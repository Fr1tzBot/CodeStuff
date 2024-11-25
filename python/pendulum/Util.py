from Vector import Vector2d
import math

def getAngle(point1: Vector2d, point2: Vector2d) -> float:
    return math.atan2(point2.y - point1.y, point2.x - point1.x)

def getDistance(point1: Vector2d, point2: Vector2d) -> float:
    return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)