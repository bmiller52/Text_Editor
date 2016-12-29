from Tkinter import *
from tkFileDialog import *
import tkFont

filename = None

def new_file():
    global filename
    filename = 'Untitled'
    text.delete(0.0, END)

def save_as():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title='Opps!', message='Unable to save file...')

def open_file():
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

def credits():
    cred = Tk()
    my_text = tkFont.Font(family='Cochin', size=20)
    cred.minsize(width=400, height=100)
    cred.title('Credits')
    text = Text(cred)
    text.insert(INSERT, 'Programmer: Brett A. Miller')
    text.insert(INSERT, ' ')
    text.insert(INSERT, 'Designer: Brett A. Miller')
    text.insert(INSERT, ' ')
    text.insert(INSERT, 'Programmed in Python 2.7.1')
    text.insert(INSERT, 'Modules Used: Tkinter')
    text.pack()

root = Tk()
my_text = tkFont.Font(family='Cochin', size=20)
root.title('Python Text Editor')
root.minsize(width=700, height=500)
root.maxsize(width=700, height=500)

text = Text(root, width=700, height=500, font=my_text, padx=15, pady=10)
text.pack()

menubar = Menu(root)
filename = Menu(menubar)
filename.add_command(label='New           None', command=new_file)
filename.add_command(label='Open         None', command=open_file)
filename.add_command(label='Save          None', command=save_as)
#filename.add_separator()
#filename.add_command(label='Credits', command=credits)
filename.add_separator()
filename.add_command(label='Quit          Cmd Q', command=root.quit)
menubar.add_cascade(label='File', menu=filename)

root.config(menu=menubar)
root.mainloop()
