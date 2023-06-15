# It will restart or shutdown your computer by clicking the button

from tkinter import *
import os

def restart():
    os.system('shutdown /r /t 1')

def shutdown():
    os.system('shutdown /s /t 1')

root = Tk()

root.title('Shut-Down')
root.geometry('280x330')
root.config(bg='white')

button_1 = Button(root, text='Restart', font=('comic sans', 20, 'bold'),relief=RAISED, cursor='arrow', command=restart)
button_1.place(x = 65, y = 75, height = 50, width = 150)

button_2 = Button(root, text='Shut down', font=('comic sans', 20, 'bold'),relief=RAISED, cursor='arrow', command=shutdown)
button_2.place(x = 65, y = 175, height = 50, width = 150)

root.mainloop()