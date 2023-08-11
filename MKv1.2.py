import time, keyboard, threading, pydirectinput
from tkinter import *
from array import array
from PIL import ImageGrab
from PIL import ImageOps
import pyautogui
from numpy import *

window = Tk()

window.title("Clicker")

#functions
def clickedStart():
    time.sleep(3)

    run = True
    keyChar = None
    intervalInt = None

    try:
       keyChar = str(keyTxt.get())
       intervalInt = int(txt.get())
    except:
      pass

    start = time.time()

    while run == True:

        if keyboard.is_pressed('0'):
            run = False
            pydirectinput.keyUp(keyChar)
            #pyautogui.keyUp(keyChar)
            break

        if intervalInt != None:
            if time.time() >= (start + intervalInt):
                pydirectinput.keyDown(keyChar)
                #pyautogui.keyDown(keyChar)
                start = time.time()
        else:
            time.sleep(0.1)
            pydirectinput.keyDown(keyChar)
            #pyautogui.keyDown(keyChar)

lbl = Label(window, text="Click delay")
lbl.grid(column=1, row=0, padx=(32, 10))

keyLbl = Label(window, text="What key")
keyLbl.grid(column=2, row=0, padx=(32, 10))

txt = Entry(window, width=10)
txt.grid(column=1, row=1, padx=(32,10))

keyTxt = Entry(window, width=10)
keyTxt.grid(column=2, row=1, padx=(32,10))

btn = Button(window, text="Start bot", command=clickedStart, bg="green", fg="Lightgreen")
btn.grid(column = 1, row=2, padx=(32,10), pady=(15, 10))

window.geometry('250x100')

#photo = PhotoImage(file = "iconBruh.png")
#window.iconphoto(False, icon)

txt.focus()
window.mainloop()