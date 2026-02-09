import pyautogui
import time
import random

def infinite():
  print("inicializando...")

  time.sleep(10)
  mouse = pyautogui.position()

  while True:
    current = pyautogui.position()

    if (current != mouse):
      print("break")

    pyautogui.click()
    now = time.strtime("%Y-$m-%d %H:%M:%S", time.localtime())
    print("[(now)] click")

    awaiting = random.randint(180, 300)
    time.sleep(awaiting)

if (__name__ == "__main__"):
  infinite()
    
