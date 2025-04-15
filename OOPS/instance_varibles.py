
# what is instance variable
# when instance variable created or destroyed
# what is memory management / what is garbage collection
# where we can create a instance variable (in constructor , instance method by using self)



# # where we can create a instance variable 
# class Test:
#     def __init__(self):
#         self.a=10

#         def m1(self):
#             self.b = 20


# t = Test()
# print(t.__dict__)

# t.m1()
# print(t.__dict__)
# t.c =30 
# print(t.__dict__)
# print('.....t2.....')

# t2 = Test()
# print(t2.__dict__)
# print(t2.a)


# # How to accss instance variable
# # inside class by using self and outside class by using object-reference name

# class Test:
#     def __init__(self):
#         self.a=100

#     def m1(self):
#         print(self.a) # instance variable access inside class


# t=Test()
# t.m1()
# print(t.a) # instance variable access outside class

# how to delete instance variable

class Test:
    def __init__(self):
        self.a=10
        self.b=20

    def m1(self):
        del self.a


t=Test()
print(t.__dict__ )
t.m1()
print(t.__dict__ )

t2 = Test()
print(t2.__dict__ )
del t2.b
print(t2.__dict__ )




class Bank:
    def __init__(self, bank_name, acc_holder_name, acc_no, acc_balance):
        self.bank_name = bank_name
        self.acc_holder_name = acc_holder_name
        self.acc_no = acc_no
        self.acc_balance = acc_balance

    def display_details(self):
        print("\n--- Account Details ---")
        print('Bank Name:', self.bank_name)
        print('Account Holder Name:', self.acc_holder_name)
        print('Account No:', self.acc_no)
        print('Account Balance:', self.acc_balance)
        print('------------------------\n')

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.acc_balance:
            print(f"❌ Your balance is insufficient to withdraw ₹{withdraw_amount}. Current balance: ₹{self.acc_balance}")
        else:
            self.acc_balance -= withdraw_amount
            print(f"✅ ₹{withdraw_amount} withdrawn successfully. New balance: ₹{self.acc_balance}")

    def deposit(self, deposit_amount):
        self.acc_balance += deposit_amount
        print(f"✅ Your A/C No: {self.acc_no} has been credited with ₹{deposit_amount}. Total balance is ₹{self.acc_balance}")
