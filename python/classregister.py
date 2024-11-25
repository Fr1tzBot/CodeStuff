from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()
print("3")
sleep(1)
print("2")
sleep(1)
print("1")
sleep(1)

for i in "13435 11896 10111 11233 12620 13135 12510".split(" "):
    for j in i:
        keyboard.press(j)
        keyboard.release(j)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

keyboard.press(Key.enter)
