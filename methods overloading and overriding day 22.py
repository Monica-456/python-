'''

class Cal:
    def add(self,num,num_2=0):
        print(num+num_2)
obj = Cal()
obj.add(4,7)

-METHOD OVERLOADING---
-->Method overloading means multiple methods with the same name but different parameters
eg:-
class cal:  #one class diff methods
    def add(self,num,num_2=0):
        print(num+num_2)
    def add(self,a,b,c):
        print(a+b+c)
obj = cal()
obj.add(45,67)
obj.add(4,7)

2.method overriding:-
#diff class same method which will activate the child class which is called riding

eg:-
class animals:
    def sound(self):
        print("Animals make sounds")
class dog(animals): #even though animal(parent class got inherited it will still activate child class method which is recent one (last method).
    def sound(self):             #output is cat meowss
        print("dogs barks")
    def sound(self)
    print("cat meowss")
d = dog()
d.sound()

operator overloading:-
--> this allows seperate operators (+,-,*) to work differently for user-defined objects.
1. __add__(+)
2.__sub__(-)
3.__mul__(*)
4.__truediv__(/)
5.__eq__(==)
6.__It(<)

eg:-
class student:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,other):
        return self.marks - other.marks
s1 = student(56)   #here the output is -11 which mean return lo ey symbol istrhey ah operation jarugutadhi,kani __add__ tesukunam kabbati print lo (+) matrame tesukovali lekpothey error vasthadhi
s2 =student(67)            #same __sub__ isthey print lo - tesukovali kani return lo em synbol isthey ah operation ey perform chesthadhi
print(s1 + s2)        


4.DATA ABSTRACTION:--
--> data abstraction is the process of hiding implemented details and showing only the essenctial data to the user.
eg:-
-ATM
-Cars
-Apps

eg:--syntaxx
from abc import ABC, abstractmethod
class parent:

    @abstractmethod     #ABC ninchi abc ni import cheskunteneh abstract method ni use cheygalam. 
    def display(self):
        pass
    

'''
from abc import ABC, abstractmethod
class bank:
    @abstractmethod
    def interest(self):
        raise NotImplementedErroe('subclass must implement intrest()')

class SBI(bank):
    def interest(self):
        print('SBI interest rate: 6.5%')

class HDFC(bank):
    def interest(self):
        print('HDFC interest rate: 5.5%')

class ICICI(bank):
    def interest(self):
        print('ICICI interest rate: 6.9%')

banks = [SBI(),HDFC(),ICICI()]

for j in banks:
    j.interest()




   

























