import Tkinter


def setRedColor():
    button.config(fg ="red")

def setGreenColor():
    button.config(fg ="green")

def setBlueColor():
    button.config(fg ="blue")

master = Tkinter.Tk()

master.geometry("300x300")
button = Tkinter.Button(master, text="Text: ")
button.grid(row=0, column = 2)

var = Tkinter.IntVar()
Tkinter.Checkbutton(master, text="RED", variable=var, command = setRedColor).grid(row=1, column = 0)

var = Tkinter.IntVar()
Tkinter.Checkbutton(master, text="BLUE", variable=var, command = setBlueColor).grid(row=1, column = 1)

var = Tkinter.IntVar()
Tkinter.Checkbutton(master, text="GREEN", variable=var, command = setGreenColor).grid(row=1, column = 2)

master.mainloop()

