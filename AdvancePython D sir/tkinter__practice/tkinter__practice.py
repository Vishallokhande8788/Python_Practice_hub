from tkinter import *

root = Tk()
root.geometry('700x300')  # Corrected format: '700x300'
root.title("This is my first Tkinter frame")
root.minsize(300, 150)
root.maxsize(700, 400)

# Create label object
msg = Label(
    text='What is Python?',
    fg='yellow',
    bg='purple',
    font=('Times New Roman', 20, 'bold'),
    padx=10,
    pady=5,
    borderwidth=6,
    relief='sunken'
)
msg.pack(anchor='w', fill='x')

# Text for the second label
s = '''Tkinter is the standard GUI (Graphical User Interface) library that comes bundled with Python. 
It allows developers to create desktop applications with elements like windows, buttons, labels, and text input fields. 
Tkinter is a wrapper around the Tcl/Tk toolkit, making it simple to use while still powerful enough for many applications. 
Because it comes pre-installed with Python, it’s widely used, especially by beginners and for small projects. 
Overall, Tkinter is a beginner-friendly way to build desktop apps using Python.
'''

# Corrected: Display the string 's', not the number 5
ans = Label(
    text=s,
    fg='white',
    bg='green',
    font='Arial 12 italic',
    padx=20,
    pady=5,
    borderwidth=5,
    relief='ridge'
)


# Create a button with a background color and text
but = Button(
    root,
    text="Click Me",
    bg='blue',
    fg='white',  # Text color
    font=('Arial', 12, 'bold'),
    padx=10,
    pady=5
)
ans.pack(fill='x')
but.pack(pady=20)

root.mainloop()
