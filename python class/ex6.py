# show python GUI by Tkinter
# import Tkinter as tk
# win = tk.Tk()
# win.title("TK GUI")
# label = tk.Label(win, text="Hellow World")
# label.pack()
# button = tk.Button(win, text="OK")
# button.pack()
# win.mainloop()

# show python GUI Button click action by Tkinter
from Tkinter import *

def DrawList():
    plist = ['L', 'T', 'C']
    for item in plist:
        listbox.insert('end', item)

win = Tk()
listbox = Listbox(win)
button = Button(win, text = "press me", command = DrawList)
button.pack()
listbox.pack()
win.mainloop()