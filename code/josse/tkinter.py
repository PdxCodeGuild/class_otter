# import tkinter
# tkinter._test()

from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=40)
frm.grid()
ttk.Label(frm, text="Random Book Generator").grid(column=0, row=0)
ttk.Button(frm, text="Click here for random book",).grid(column=3, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=6)
root.mainloop()
