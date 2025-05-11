from tkinter import *
import tkinter.messagebox as AlertInfo

root = Tk()
root.geometry("800x700")
root.title("College Admission Form")

def dataWrite():
    data = {
        "Full Name": nameInput.get(),
        "Email": emailInput.get(),
        "Phone": phoneInput.get(),
        "Date of Birth": dobInput.get(),
        "Gender": genderVar.get(),
        "Course": courseVar.get(),
        "Address": addressInput.get("1.0", END)
    }
    
    with open("college_admission.txt", "a") as f:
        for key, value in data.items():
            f.write(f"{key}: {value}\n")
        f.write("="*40 + "\n")
    
    AlertInfo.showinfo("Success", "Registration Successful!")

# Labels and Input Fields
Label(root, text="College Admission Form", font=("Arial", 24, "bold")).grid(row=0, column=1, columnspan=2, pady=20)

Label(root, text="Full Name:", font=("Arial", 14)).grid(row=1, column=0, sticky=W, padx=20)
nameInput = Entry(root, width=40)
nameInput.grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Email:", font=("Arial", 14)).grid(row=2, column=0, sticky=W, padx=20)
emailInput = Entry(root, width=40)
emailInput.grid(row=2, column=1, padx=10, pady=5)

Label(root, text="Phone Number:", font=("Arial", 14)).grid(row=3, column=0, sticky=W, padx=20)
phoneInput = Entry(root, width=40)
phoneInput.grid(row=3, column=1, padx=10, pady=5)

Label(root, text="Date of Birth:", font=("Arial", 14)).grid(row=4, column=0, sticky=W, padx=20)
dobInput = Entry(root, width=40)
dobInput.grid(row=4, column=1, padx=10, pady=5)

Label(root, text="Gender:", font=("Arial", 14)).grid(row=5, column=0, sticky=W, padx=20)
genderVar = StringVar()
genderVar.set("Male")
Radiobutton(root, text="Male", variable=genderVar, value="Male").grid(row=5, column=1, sticky=W)
Radiobutton(root, text="Female", variable=genderVar, value="Female").grid(row=5, column=1, sticky=E)

Label(root, text="Course:", font=("Arial", 14)).grid(row=6, column=0, sticky=W, padx=20)
courseVar = StringVar()
courseList = ["BSc IT", "BCom", "BA", "MSc IT", "MBA"]
courseDropdown = OptionMenu(root, courseVar, *courseList)
courseVar.set(courseList[0])
courseDropdown.config(width=35)
courseDropdown.grid(row=6, column=1, padx=10, pady=5)

Label(root, text="Address:", font=("Arial", 14)).grid(row=7, column=0, sticky=NW, padx=20)
addressInput = Text(root, width=30, height=5)
addressInput.grid(row=7, column=1, padx=10, pady=5)

Button(root, text="Submit", font=("Arial", 14), bg="blue", fg="white", command=dataWrite).grid(row=8, column=1, pady=20)

root.mainloop()
