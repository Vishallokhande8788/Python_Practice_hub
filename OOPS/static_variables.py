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



#  eg create a bank account with bankname , account holder name , account nno , balance , below that add to options withdrawl option  balance is 500 and witdraww 1000 then pring msg your balance is insufficient , deposite option , print deposite msg your ac/no xyz has been created with 1000 s now your total balance is previous balance + 1000 


class Bank:
    def __init__(self, bank_name, acc_holder_name, acc_no, acc_balance):
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
            self.acc_balance -= withdrawl_amount
            print(f"{withdrawl_amount} withdrawn. New balance: {self.acc_balance}")

    def l2(self, deposite_amount):
        self.acc_balance += deposite_amount
        print(f"{deposite_amount} deposited. New balance: {self.acc_balance}")


# Test the class
b = Bank('SBI', 'Vishal', '123456789', 500)
b.l1(200)
b.l2(100)
b.display_details()



