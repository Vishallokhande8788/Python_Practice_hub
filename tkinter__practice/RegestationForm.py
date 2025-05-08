from tkinter import *
import tkinter.messagebox as AlertInfo


root =Tk()
root.geometry("900x600")
root.title("this is my first tkinter form")
def alert():
    AlertInfo.showinfo('info', 'your registation done')

def dataWrite():
    UserNameData = userNameInput.get()
    UserPasswordData =UserPasswordInput.get()
    UserEmailData = UserEmailInput.get()
    allData = [ UserNameData + '\n' , UserPasswordData +'\n' , UserEmailData +'\n']
    write_into_file(allData)
    AlertInfo.showinfo('info' ,'regestation successful !')

def write_into_file(data):
    f = open('mykinter.txt','w')
    f.writelines(data)
    f.close()

UserName= Label(text='UserName',font=('Times New Roman', 20, 'bold'),padx=10,pady=10)
userNameInput = Entry(borderwidth=6,relief = 'sunken')


userPassword= Label(text='Password',font=('Times New Roman', 20, 'bold'),padx=10,pady=10)
UserPasswordInput = Entry(borderwidth=6,relief = 'sunken')

UserEmail= Label(text='Email',font=('Times New Roman', 20, 'bold'),padx=10,pady=10)
UserEmailInput = Entry(borderwidth=6,relief = 'sunken')

RegisterButton = Button(text='Register',padx=30,pady=10 ,command=dataWrite)


UserName.grid(row=0, column=1)
userNameInput.grid(row=0 , column=2)

userPassword.grid(row=1 , column=1)
UserPasswordInput.grid(row=1 , column=2)

UserEmail.grid(row=2 , column=1)
UserEmailInput.grid(row=2, column=2)

RegisterButton.grid(row=3,column=1)


root.mainloop()
