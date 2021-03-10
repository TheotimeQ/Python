##--------------------------------------------------------------
import ctypes
import time
from time import time as temps
from ctypes import windll, Structure, c_long, byref
from PIL import ImageGrab
from pynput.keyboard import Key, Controller
import os
from PIL import Image
##--------------------------------------------------------------

def pos(x,y):
    ctypes.windll.user32.SetCursorPos(x, y)

def click():
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) 
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) 

def memorie():
    color_list = ["j","v", "r"]
    for k in range(0,30):
        for color in color_list:
            time.sleep(0.2)
            if color == "r" :
                pos(188,284)
                click()
            if color == "b" :
                pos(420,534)
                click()
            if color == "j" :
                pos(366,298)
                click()
            if color == "v" :
                pos(192,538)
                click()
        T = ( len(color_list) + 1 ) * ( 0.5 + 0.2 ) + 0.5
        time.sleep( T )
        img = ImageGrab.grab(bbox=(200,400,500,700))
        save_path = "color.jpg"
        img.save(save_path)
        r,g,b = img.getpixel((1,1))
        if r > 50 :
            color_list.append("r")
        r,g,b = img.getpixel((290,0))
        if g > 100 :
            color_list.append("j")
        r,g,b = img.getpixel((0,290))
        if g > 100 :
            color_list.append("v")
        r,g,b = img.getpixel((290,290))
        if g > 100 :
            color_list.append("b")
        time.sleep(1)

time.sleep(2)
memorie()