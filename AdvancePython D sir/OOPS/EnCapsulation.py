# 23/04/2024
# Encapsulation in Python is the concept of hiding internal details of a class and  restricting direct access to some of its components. It is done using **private (`__`) and protected (`_`) members**.
class Account:
    def __init__(self):
        self.__pin = 4444

    def SetPin(self, pin):
        uname = input("Enter your username: ")
        if uname == "qst":
            self.__pin = pin
        else:
            print("you are Invalid Person")

    def GetPin(self):
        uname = input("Enter your username: ")
        if uname == "qst":
            print(self.__pin)
            return self.__pin
        else: return "Invalid person "


a = Account()
a.SetPin(1234)
print(a.GetPin())