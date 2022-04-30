import time
from  tkinter import *

root = Tk()
reloj = Label(font='Arial')
root.resizable(648,480)
root.title('SolSpaceOS')
root.attributes('-fullscreen', True)
root.attributes('-disabled', True)

def clock():
    string = time.strftime('%H:%M:%S %p')
    reloj.config(text = string)
    reloj.after(1000, clock)


clock()
reloj.pack(anchor=SW)
root.mainloop()