from Tkinter import *
import time

def decrement():
    print "test"
    t_end = time.time() + float(entryValue.get())
    print time.time()
    print t_end
    integerStart = int(entryValue.get())
    while time.time() < t_end:
        print time.time()
        integerStart = integerStart - 1
        entryValue.set(str(integerStart))
        time.sleep(1)



master = Tk()

entryValue = StringVar()
entry = Entry(master, textvariable = entryValue)
entry.grid(row=0)

button = Button(master, text="Count: ", command = decrement)
button.grid(row=1)


master.mainloop()
