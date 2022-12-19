import pyautogui as pg
import random 
import time

isMoving = True

while isMoving:
    pos_x = random.randint(60, 1000)
    pos_y = random.randint(60, 1000)
    pg.moveTo(pos_x, pos_y, 0.5)
    time.sleep(2)
    
