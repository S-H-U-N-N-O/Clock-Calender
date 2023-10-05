from tkinter import *
from time import *

root = Tk()
root.title("Calock")


def update():
    time_string = strftime('%I:%M:%S %p')
    time_label.config(text=time_string)

    daydate_string = strftime("%A, %D %B, %Y ")
    daydate_label.config(text=daydate_string)

    time_label.after(1000, update)

time_label = Label(root, font=("Arial", 50))
time_label.pack()

daydate_label = Label(root, font=("Arial", 50))
daydate_label.pack()

update()

root.mainloop()