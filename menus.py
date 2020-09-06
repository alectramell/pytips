import os
import sys
import tkinter
from tkinter import *
from tkinter import ttk

root = Tk()

def XSAVE():

	print('<save-option-selected>')

def XOPEN():

	print('<open-option-selected>')

root.title('MENUS v1.0')
root.geometry('900x600+200+30')
root.config(bg='#050505', border=0)
root.resizable(False, False)

# Build the Menu Bar..
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

# Add commands to the Menu Bar..
filemenu.add_command(label='Open..', command=XOPEN)
filemenu.add_command(label='Save..', command=XSAVE)

# Pack, and add the Menu Bar..
menubar.add_cascade(label='File', menu=filemenu)
root.config(menu=menubar)

root.mainloop()
