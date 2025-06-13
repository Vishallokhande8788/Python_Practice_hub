from tkinter import *

# Initialize root window
root = Tk()
root.title("Counter App")
root.geometry("300x200")

# Counter variable
counter = IntVar()
counter.set(0)

# Functions for add and subtract
def increment():
    counter.set(counter.get() + 1)

def decrement():
    counter.set(counter.get() - 1)

# UI Elements
Label(root, text="Counter", font=("Arial", 18, "bold")).pack(pady=10)

countLabel = Label(root, textvariable=counter, font=("Arial", 24))
countLabel.pack()

# Buttons Frame
btn_frame = Frame(root)
btn_frame.pack(pady=20)

Button(btn_frame, text="+ Add", width=10, font=("Arial", 12), command=increment).grid(row=0, column=0, padx=10)
Button(btn_frame, text="- Sub", width=10, font=("Arial", 12), command=decrement).grid(row=0, column=1, padx=10)

root.mainloop()
