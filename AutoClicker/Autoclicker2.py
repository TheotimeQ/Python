##--------------------------------------------------------------
import ctypes
import time
from ctypes import windll, Structure, c_long, byref
##--------------------------------------------------------------

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

def pos(x,y):
    ctypes.windll.user32.SetCursorPos(x, y)

def click():
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
    time.sleep(0.5)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

def get():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}

def getB():
    while 1 == 1 :
        pt = POINT()
        windll.user32.GetCursorPos(byref(pt))
        return { "x": pt.x, "y": pt.y}

def Clean():
        while(1==1):
            click()










