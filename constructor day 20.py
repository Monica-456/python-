'''
---------CONSTRUCTOR-------
This constructor initializes the obejct automatically when its is created.

class Batch:
    def __init__(self,name,branch):
        self.name = name
        self.branch = branch
    def display(self):
        print(self.name)
        print(self.branch)
B4 = Batch('Monica','BSC')
B4.display()

Accessing variables:-


public:-
eg:-
class Batch:
    def __init__(self,name,branch):
        self._name = name
        self.branch = branch
    def display(self):
        print(self._name)
        print(self.branch)
B4 = Batch('Monica','BSC')
B4.display()

eg2:-
class fam:
    def __init__(self):
        self._name = "Monica"
f = fam()
print(f._name)

private:-inside the class
class  bank:
    def __init__(self):
        self.__pin ='1112'
AC = bank()
print(AC._bank__pin)

outside the class
class  bank:
    def __init__(self):
        self.__pin ='1112'
    def display(self):
        print(self.__pin)
ac = bank()
ac.display()

--------Encapsulation--------
-->Encapsulation means wrapping up od the data and methods into one single unit(class) while controlling access to the data.



'''

class atm:
    def __init__(self, balance):
        self._balance = balance
    def deposit(self, amount):
        self._balance += amount
        print(self._balance)
trans = atm(balance = int(input("enter your amount :")))
trans.deposit(amount = int(input("enter your amount :")))
    



















































