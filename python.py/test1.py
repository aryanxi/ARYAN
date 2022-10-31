from os import set_handle_inheritable
from cv2 import BackgroundSubtractor
import pyautogui
from random import randint
from time import sleep


def funbox():
 nofmessage=100

 def name():
    nameList = ["shanta","shantabai","baburao","rushipermi","kinner shantunu","gayshantunu"]
    rand_name = nameList[randint(0,len(nameList) - 1)]
    return rand_name

 while True:
    pyautogui.typewrite(f"tum bsdk ho {name()}")
    sleep(.00)
    pyautogui.typewrite("\n")
    sleep(0)
    nofmessage=nofmessage-1

    if nofmessage==0:
      break

funbox()

