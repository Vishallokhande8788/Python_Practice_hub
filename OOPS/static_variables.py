# static variables
# what is static variable
# when static variable created or destroyed
# what is memory management / what is garbage collection
# where we can create a static variable 

'''
directly inside class
inside constructor , instance method , static mathed using class name 
inside class method either using class name or cls 
outisde class by using class name

'''

'''
class Test:
    a = 10
    def __init__(self):
        Test.b=20

    def m1(self):
        Test.c = 30

    
    @classmethod
    def m2(cls):
        Test.d = 40
        cls.e=50

    @staticmethod
    def m3():
        Test.f = 60

t=Test()
t.m1()
t.m2()
t.m3()
Test.g = 70
print(Test.__dict__)

'''



#  eg create a bank account with ba
# nkname , account holder name , account nno , balance , below that add to options withdrawl option  balance is 500 and witdraww 1000 then pring msg your balance is insufficient , deposite option , print deposite msg your ac/no xyz has been created with 1000 s now your total balance is previous balance + 1000 

'''
class Bank:
    bank_name = 'SBI'
    def __init__(self, bank_name, acc_holder_name, acc_no, acc_balance=1000):
        self.bank_name = bank_name
        self.acc_holder_name = acc_holder_name
        self.acc_no = acc_no
        self.acc_balance = acc_balance

    def display_details(self):
        print('Bank Name:', self.bank_name)
        print('Account Holder Name:', self.acc_holder_name)
        print('Account No:', self.acc_no)
        print('Account Balance:', self.acc_balance)

    def l1(self, withdrawl_amount):
        if withdrawl_amount > self.acc_balance:
            print("Insufficient Balance")
        else:
            self.acc_balance = self.acc_balance - withdrawl_amount
            print(f"your account no is {self.acc_no} id debited with {withdrawl_amount} ")
            print(f"{withdrawl_amount} withdrawn. New balance: {self.acc_balance}")

    def l2(self, deposite_amount):
        self.acc_balance =self.acc_balance + deposite_amount
        print(f"your account no is {self.acc_no} id credited with {deposite_amount} ")
        print(f"{deposite_amount} deposited. New balance: {self.acc_balance}")




print(" Welcome to  " , Bank.bank_name)
name = input("enter your name: ")
acc_no = input("enter your account number: ")

a = Bank(name, acc_no)

while True:
    op  = input('select : \n d: deposite \n w: withdrawl \n q: quit \n ')
    if op.lower() == 'd':
        amnt = int(input("enter amount: "))
        a.deposit(amnt)
    elif op.lower() == 'w':
        amnt = int(input("enter amount: "))
        a.withdraw(amnt)
    elif op.lower() == 'q':
        break
    else:
        print("enter valid input")
'''
#  bank acc eg 

class Bank:
    bank_name = 'SBI'  # Static variable

    def __init__(self, acc_holder_name, acc_no, acc_balance=1000):
        self.acc_holder_name = acc_holder_name
        self.acc_no = acc_no
        self.acc_balance = acc_balance
        print(f"Your A/C No. {self.acc_no} has been created with ₹{acc_balance}.\n")

    def display_details(self):
        print('\n--- Account Details ---')
        print('Bank Name:', Bank.bank_name)
        print('Account Holder Name:', self.acc_holder_name)
        print('Account No:', self.acc_no)
        print('Account Balance: ₹', self.acc_balance)
        print('------------------------\n')

    def withdraw(self, amount):
        if amount > self.acc_balance:
            print(" Insufficient Balance\n")
        else:
            self.acc_balance -= amount
            print(f" ₹{amount} withdrawn from A/C {self.acc_no}.")
            print(f"New Balance: ₹{self.acc_balance}\n")

    def deposit(self, amount):
        self.acc_balance += amount
        print(f" ₹{amount} deposited into A/C {self.acc_no}.")
        print(f"New Balance: ₹{self.acc_balance}\n")

    def Acc_info(self ):
        print(f"Account Name: {self.acc_holder_name}")
        print(f"Account Number: {self.acc_no}")
        print(f"Account Balance: {self.acc_balance}")
        print("\n")


# # --- Main Program ---
# print("Welcome to", Bank.bank_name)
# name = input("Enter your name: ")
# acc_no = input("Enter your account number: ")

# a = Bank(name, acc_no)

# while True:
#     op = input("Select: \nd: Deposit \nw: Withdrawal \nq: Quit\n> ")
#     if op.lower() == 'd':
#         amnt = int(input("Enter deposit amount: ₹"))
#         a.deposit(amnt)
#     elif op.lower() == 'w':
#         amnt = int(input("Enter withdrawal amount: ₹"))
#         a.withdraw(amnt)
#     elif op.lower() == 'q':
#         print("Thank you for banking with", Bank.bank_name)
#         break
#     else:
#         print("⚠️ Enter a valid input\n")

t = Bank()
t.Acc_info('vishal' , 1234567890 , 1000)
