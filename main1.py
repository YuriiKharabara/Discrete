from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os, threading, subprocess
import os
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt
root= Tk()
canvas1 = Canvas(root, width = 300, height = 300)
canvas1.pack()
Sbool = 0
menubar = Menu(root)
root.config(menu=menubar)

# create the file_menu
file_menu = Menu(
    menubar,
    tearoff=0
)

# add menu items to the File menu
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Close')
file_menu.add_separator()

# add Exit menu item
file_menu.add_command(
    label='Exit',
    command=root.destroy
)

# add the File menu to the menubar
menubar.add_cascade(
    label="File",
    menu=file_menu
)
# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='Welcome')
help_menu.add_command(label='About...')

# add the Help menu to the menubar
menubar.add_cascade(
    label="Help",
    menu=help_menu
)


def select_file():
    filetypes = (
        ('text files', '*.csv'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )


# open button
open_button = Button(
    root,
    text='Open a File',
    command=select_file
)

open_button.pack(expand=True)

def startA ():
    global Sbool
    if (Sbool == 0):
        label1 = Label(root, text= 'Started!', fg='green', font=('helvetica', 12, 'bold'))
        canvas1.create_window(150, 200, window=label1)
        # my_thread = threading.Thread(target=one)
        # my_thread.start()
        Sbool = 1
        global p
        p = subprocess.Popen('python script.py')
def stopA ():
    global Sbool
    if (Sbool == 1):
        label1 = Label(root, text= 'Stopped!', fg='green', font=('helvetica', 12, 'bold'))
        canvas1.create_window(150, 200, window=label1)
        #my_thread = threading.Thread(target=one)
        Sbool = 0
        p.terminate()
button1 = Button(text='Start',command=startA, bg='brown',fg='white')
button2 = Button(text='Stop',command=stopA, bg='brown',fg='white')
canvas1.create_window(150, 100, window=button1)
canvas1.create_window(150, 150, window=button2)
root.mainloop()