from datetime import datetime
import tkinter as tk
import time as tm

root = tk.Tk()
clock = tk.Label(text=datetime.time)
clock.pack()
root.mainloop()