import keyFunction
import time
import keyboard

keyDefine = {
    "escape":  0x01,
    "e": 0x12,
    "right": 0xCD,
    "left": 0xCB,
}


currentP = 1


def customPressKey(key):
    key = keyDefine[key]
    keyFunction.PressKey(key)
    time.sleep(0.05)
    keyFunction.ReleaseKey(key)


def changeToPosition(startP, toP):
    dif = toP - startP
    delay = 0.035
    if dif != 0:
        customPressKey('escape')
        time.sleep(delay)
        customPressKey('e')
        time.sleep(delay)
        customPressKey('e')
        time.sleep(delay)
        if dif > 0:
            while dif != 0:
                customPressKey('right')
                dif = dif - 1
                time.sleep(delay)
        else:
            while dif != 0:
                customPressKey('left')
                dif = dif + 1
                time.sleep(delay)
        customPressKey('e')
        time.sleep(delay)
        customPressKey('escape')
        time.sleep(delay)


def changeMain(position):
    global currentP
    changeToPosition(currentP, position)
    currentP = position


if __name__ == "__main__":
    print(keyDefine["escape"])
    time.sleep(1)
    print('start')
    keyboard.add_hotkey('y', changeMain, args=(1,))
    keyboard.add_hotkey('u', changeMain, args=(2,))
    keyboard.add_hotkey('i', changeMain, args=(3,))
    keyboard.add_hotkey('o', changeMain, args=(4,))
    keyboard.add_hotkey('p', changeMain, args=(5,))
    keyboard.wait('a')
    print('end')
