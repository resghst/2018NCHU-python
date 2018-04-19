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
# from Tkinter import *

# def DrawList():
#     plist = ['L', 'T', 'C']
#     for item in plist:
#         listbox.insert('end', item)

# win = Tk()
# listbox = Listbox(win)
# button = Button(win, text = "press me", command = DrawList)
# button.pack()
# listbox.pack()
# win.mainloop()


from Tkinter import *
class GUIDemo( Frame ): 
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        # input
        self.inputText = Label(self)
        self.inputText["text"] = "input:" 
        self.inputText.grid(row=0, column=0)
        self.inputField = Entry(self)
        self.inputField["width"] = 50
        self.inputField.grid(row=0, column=1, columnspan=3)

        # output
        self.outputText = Label(self)
        self.outputText["text"] = "output:" 
        self.outputText.grid(row=1, column=0)
        self.outputField = Entry(self)
        self.outputField["width"] = 50
        self.outputField.grid(row=1, column=1, columnspan=3)

        self.new = Button(self)
        self.new["text"] = "New"
        def newMethod(self):
            self.displayText["text"] = "this is New button."
        self.new["command"] = newMethod
        self.new.grid(row=2, column=0)
        
        self.load = Button(self)
        self.load["text"] = "load"
        self.load.grid(row=2, column=1)
        
        self.save = Button(self)
        self.save["text"] = "save"
        self.save.grid(row=2, column=2)
        
        self.encode = Button(self)
        self.encode["text"] = "encode"
        self.encode.grid(row=2, column=3)
        
        self.decode = Button(self)
        self.decode["text"] = "decode"
        self.decode.grid(row=2, column=4)
        
        self.clear = Button(self)
        self.clear["text"] = "clear"
        self.clear.grid(row=2, column=5)
        
        self.copy = Button(self)
        self.copy["text"] = "copy"
        self.copy.grid(row=2, column=6)
        
        self.displayText = Label(self)
        self.displayText["text"] = "something happend"
        self.displayText.grid(row=3, column=0, columnspan=7)

if __name__ =="__main__":
    root =Tk()
    app = GUIDemo(master=root)
    app.mainloop()