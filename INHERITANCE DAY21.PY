'''
----------INHERITANCE---------


Single inheritance:-
a single inheritancce class inherits from one parent is called single inheritance.

class animal:
    def sound

class father:
    def land(self):
        print('5 ar of land')
class son(father):
    def flat(self):
        print('3BHK flat')
s = son()
s.land()
s.flat()


Multiple inheritance:-
-----------------------
a child class inherits more than one percent is call multiple inheritance.
eg1:-
class father:
    def skills(self):
        print('driving')
class mother:
    def talent(self):
        print('cooking')
class brother:
    def learn(self):
        print('python')
class son(father,mother,brother):
    def mine(self):
        print('coding')
all_ = son()
all_.skills()
all_.talent()
all_.mine()
all_.learn()                

eg2:-
class grandfather:
    def house(self):
        print('owns house')
class father(grandfather):
    def flat(self):
        print('new 3bhk flat')
class son(father):
    def car(self):
        print('Have a Car')
fam = son()
fam.house()
fam.flat()
fam.car()

Hierarchical inheritance:-
------------------------------
Multiple childs inherits from the same parents.

class mother:
    def gold(self):
        print('10kg gold')
class pinky(mother):
    def show(self):
        print('pinky will get 5kg ok gold')
class yuktha(mother):
    def show_2(self):
        print('yuktha will get remaining gold')
child_1 = pinky()                     #should create 2 objects cause we have two child class for only one single parent
child_2 = yuktha()

child_1.gold()
child_1.show()
child_2.show_2()


class father():
    def land(self):
        print('6 ar of land')
class child_1(father):
    def show_1(self):
        print('chandu will get 2 acres of land')
class child_2(father):
    def show_2(self):
        print('karthik will get 2 acres of land')
class child_3(father):
    def show_3(self):
        print('murthy will get 2 acres of land')
chandu = child_1
karthik = child_2
murthy = child_3

chandu.land()
karthik.land()
murthy.land()============


hybrid inhertance:-

class A:
    def methodA(self):
        print('Class A')
class B(A):
    def methodB(self):
        print('Class B')
class C(A):
    def methodC(self):
        print('Class C')
class D(B,C):
    def methodD(self):
        print('Class D')
so = D()
so.methodA()
so.methodB()
so.methodC()

super():-
==> this super() function is used to access the parent class methos or constructor in the child class..

class parent:
    def show(self):
        print('parent method')
class child(parent):
    def show(self):
     super().show()
     print('child class')
chi_=child()
chi_.show()

eg2:
class person:
    def __init__(self,name):
        self.name = name
class student(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll
    def display(self):
        print(self.name)
        print(self.roll)
an = student('Monica',100)
an.display()

'''
class person:
    def __init__(self,name):
        self.name = name
class student(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll
    def display(self):
        print(self.name)
        print(self.roll)
an = student('Monica',100)
an.display()

































