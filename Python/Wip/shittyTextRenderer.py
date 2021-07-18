import os
import time
import random
from random import randint

colors = {}

class shittyTextRenderer():
    def __init__(self, startcolor: str="black", character: str="█"):
        self.character = character
        self.startColor = startcolor
        self.colors = {
            "black":          "\033[30m" + character + "\033[39m",
            "red":            "\033[31m" + character + "\033[39m",
            "green":          "\033[32m" + character + "\033[39m",
            "yellow":         "\033[33m" + character + "\033[39m",
            "blue":           "\033[34m" + character + "\033[39m",
            "magenta":        "\033[35m" + character + "\033[39m",
            "cyan":           "\033[36m" + character + "\033[39m",
            "white":          "\033[37m" + character + "\033[39m",

            "gray":           "\033[90m" + character + "\033[39m",
            "bright black":   "\033[90m" + character + "\033[39m",
            "grey":           "\033[90m" + character + "\033[39m",

            "bright red":     "\033[91m" + character + "\033[39m",
            "bright green":   "\033[92m" + character + "\033[39m",
            "bright yellow":  "\033[93m" + character + "\033[39m",
            "bright blue":    "\033[94m" + character + "\033[39m",
            "bright magenta": "\033[95m" + character + "\033[39m",
            "bright cyan":    "\033[96m" + character + "\033[39m",
            "bright white":   "\033[97m" + character + "\033[39m"
        }
        self.setFullScreen(startcolor)

    def getRows(self) -> int:
        return os.get_terminal_size().columns
    def getCols(self) -> int:
        return os.get_terminal_size().lines

    def setFullScreen(self, color: str) -> None:
        screen = []
        cols = self.getCols()
        rows = self.getRows()
        for i in range(cols):
            screen.append([])
        for i in screen:
            for j in range(rows):
                i.append(color)
        self.screen = screen

    def setColor(self, x: int, y: int, color: str) -> None:
        screen = self.screen
        screen[y][x] = color
        self.screen = screen
    def display(self) -> None:
        colors = self.colors
        screen = self.screen

        out = "\n"
        for i in screen:
            for j in i:
                out += colors[j]
        print(out, end="")

