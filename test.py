import pyautogui
import keyboard

print("hello")
print(pyautogui.position())
print("start")
keyboard.wait("a")
pyautogui.typewrite('Hello world!')
