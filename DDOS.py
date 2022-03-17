import subprocess
import platform
from tkinter import *
from tkinter import messagebox
import tkinter as tk

window = Tk()
window.title("Ddos Test")
window.geometry("400x200")
def ButtonFunc():
 messagebox.showinfo( "Start Test", "Test is Started")
B = Button(window, text ="Start Test", command = ButtonFunc)
B.pack()
L1 = Label(window, text="Write Website Domain")
L1.pack( side = LEFT)
E1 = Entry(window, bd =5)
E1.pack(side = RIGHT)
window.tk_setPalette("#ff1dce")
window.mainloop()

def ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '0', host]
    return subprocess.call(command)

host = 'Write Website Domain'
print(ping(host))
