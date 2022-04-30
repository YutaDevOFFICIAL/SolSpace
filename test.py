import datetime
import tkinter as tk

root = tk.Tk()
clock = tk.Label(text=datetime.datetime.today)
clock.pack()
root.mainloop()