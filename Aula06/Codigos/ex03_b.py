from Tkinter import *
import time


root = Tk()
var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )

var.set("Hey!? How are you doing?")
label.pack()

i=0
while i<10:
    i = i+1
    var.set("foram :" +str(i))
    root.update()
    time.sleep(1)

