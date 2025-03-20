from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()
print("3")
sleep(1)
print("2")
sleep(1)
print("1")
sleep(1)

for i in "81227 84241 85130 80071 83294 83830 82516 82765 82239".split(" "):
    for j in i:
        keyboard.press(j)
        keyboard.release(j)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

keyboard.press(Key.enter)
