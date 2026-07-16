'''
-----------------OOPs-------------------
Object oriented programmimg language system(oops), this will be organize the code using class and object..

use:-
-code reusable
-Easy maintanence
-clear understanding
-better undderstanding

classes:- class is a blue printy or a template used to create an object.

class Batch_4:
    pass

object:-object is an instance of the class
eg:-
class student:
    studn = 'Teja'
st_ = student()     #object
print(st_)

Attributes:-Attributes are the variables that belongs to an object or the class
eg:-
class how:
    def __init__(self,name,age):
        self.name = name           #instance attributes
        self.age = age
    def nam(self):
        print(self.name)
s1 = how('monica',21)
print(s1.nam())

Methods:-
---------
Method are nothing but functions inside the class


'''
class calculator:
    def add(self,num,num_2):
        print(num+num_2)
    def sub(self,num,num_2):
        print(num-num_2)
cal = calculator()
cal.add(45,6)
cal.sub(9,5)
  
