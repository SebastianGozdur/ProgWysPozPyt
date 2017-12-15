from Tkinter import *

master = Tk()


entryValue = StringVar()
entry = Entry(master, textvariable = entryValue)
entry.grid(row=0)

buttons = []
for x in range (0,9):
    column = 0
    buttons.append(Button(master, text=str(x+1)))
    if x>=1 and x<=3:
        buttons[x].grid(row = x, column = column)
        column +=1
    elif x>=4 and x<=6:
        buttons[x].grid(row = x, column = column)
        column +=1
    elif x>=7 and x<=9:
        buttons[x].grid(row = x, column = column)
        column +=1
    if column == 2:
        column = 0
buttons.append(Button(master, text="0"))

master.mainloop()



