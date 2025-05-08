from tkinter import *
import tkinter.messagebox as msg

def select():
    msg.showinfo('Done', f'You selected: {rc.get()}')

root = Tk()
root.geometry("400x200")  # Fixed geometry spacing

Label(root, text='Father of Python', font='Bahnschrift 12 bold').grid(row=0, column=0, pady=10)

rc = StringVar()

Radiobutton(root, text='Elon Musk', variable=rc, value='Elon Musk').grid(row=1, column=0, sticky='w')
Radiobutton(root, text='Anil Ambani', variable=rc, value='Anil Ambani').grid(row=2, column=0, sticky='w')
Radiobutton(root, text='Gautam Adani', variable=rc, value='Gautam Adani').grid(row=3, column=0, sticky='w')
Radiobutton(root, text='Guido van Rossum', variable=rc, value='Guido van Rossum').grid(row=4, column=0, sticky='w')

Button(text='Submit', borderwidth=6, bg='white', font='Arial 14 bold', command=select).grid(row=6, column=0, pady=10)

root.mainloop()
