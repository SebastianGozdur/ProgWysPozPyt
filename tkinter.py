import Tkinter as tt

def labelConfig(label, txt):
	label.config(text = txt, fg = "light green", bg = "dark green")

root = tt.Tk()
w = tt.Label(root, text = "Hello Tkinter")
labelConfig(w, "123")
w.pack()

root.mainloop()