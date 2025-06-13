from tkinter import *
import tkinter.messagebox as msg5


def add():
    print('hi')
    result.set(no1.get() + no2.get())

    msg5.showinfo('tttt','hello show info')
    msg5.showerror('tttt','hello show error')
    msg5.showwarning('ttt','hello show warning')

def sub():
    result.set(no1.get() - no2.get())

def mul():
    result.set(no1.get() * no2.get())

def dive():
    result.set(no1.get() // no2.get())


root =Tk()
root.geometry("700x300")
root.title("this is my first tkinter frame")
# b=Button(
#     text="click" ,
#     fg='red' ,
#     bg='black',
#     font='Arial 16 bold',
#     borderwidth=6,
#     relief='sunken'
# )
#
# b2 = Button(
# text="click" ,
#     fg='red' ,
#     bg='black',
#     font='Arial 16 bold',
#     borderwidth=6,
#     relief='sunken'
# )
#
# b3 = Button(
# text="click" ,
#     fg='red' ,
#     bg='black',
#     font='Arial 16 bold',
#     borderwidth=6,
#     relief='sunken'
# )
#
# b4 = Button(
#     text="click" ,
#     fg='red' ,
#     bg='black',
#     font='Arial 16 bold',
#     borderwidth=6,
#     relief='sunken'
# )

# b.grid(row=0, column=0)
# b2.grid(row=1, column=1)
# b3.grid(row=2, column=2)
# b4.grid(row=3, column=3)

no1 = IntVar()
no2 = IntVar()
result = IntVar()

#  basic calculator
msg = Label(
    text='No 1',
    font=('Times New Roman', 20, 'bold'),
    padx=100,
    pady=10
)
input = Entry(
    borderwidth=6,
    relief = 'sunken',
    textvariable=no1

)

msg1 = Label(
    text='No 2',
    font=('Times New Roman', 20, 'bold'),
    padx=100,
    pady=10,

)
input1 = Entry(
    borderwidth=6,
    relief = 'sunken',
    textvariable=no2

)
msg2 = Label(
    text='RESULT',
    font=('Times New Roman', 20, 'bold'),
    padx=100,
    pady=10,

)
input2 = Entry(
    borderwidth=6,
    relief = 'sunken',textvariable=result

)

b = Button(
    text='+',
    padx=30,
    pady=10,
    command=add
)

b1 = Button(
    text='-',
    padx=30,
    pady=10,
    command=sub
)

b2 = Button(
    text='*',
    padx=30,
    pady=10,
    command=mul
)
b3 = Button(
    text='/',
    padx=30,
    pady=10,
    command=dive
)


msg.grid(row=0, column=10)
input.grid(row=0 , column=12)

msg1.grid(row=1, column=10)
input1.grid(row=1 , column=12)

msg2.grid(row=2, column=10)
input2.grid(row=2 , column=12)

b.grid(row = 3 , column=9)
b1.grid(row = 3 , column=10)
b2.grid(row = 3 , column=12)
b3.grid(row =  3, column=14)




root.mainloop()



