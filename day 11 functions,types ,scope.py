'''
--------------Functions---------------
---->function is a block of code that can be reusable
---->function can avoid the repeated lines of code...

functions are of two types:-
---------------------------
1. built_in:-
---------------
eg:- print(), max(),min(), type(),sum()

2.user-defined:-
---------------
this function starts with a keyword (def)
def func_name(parameters)
     ---------------
     --------------
     --------------
func_name(arguments)
eg:-
def add(a,b):
    print("HELLO")
add()

Types of Arguments
-------------------
1.Required Arguments
2.Default Argumnets
3.Keyword Arguments
4.Variable length Arguments

1.Required Arguments:-you have to pass same number of arguments with the definition of the funtion.
eg1:-
def add(a,b):
    print(a+b)
add(3,2)
--->#how we should not use:-
def add(a,b):
    print(a+b)
add(3,2)

2.Default Arguments:-takes arguments as defaults no matte rhoe they are assigned
eg:-
def add(a,b):
    print(a+b)
add(b=9,a=6)

eg2:_
num = 7
num_2 = 9
num_3 = 8
def add(a,b,c):
    print(a)
    print(b)
    print(b)
add(num,num_2,num_3)

3.Keyword Arguments:-we can pass as a pair like(variable=
eg:-
def add(a,b):
    print(a+b)
add(a=3,b=2)

4. Variable length:-
--->can pass n number of arguments and just use args in the parameters, will recieve tuple of arguments. args are defined with help of (*) and we can access them useing indexing.
eg:- print(a[2])
with ** we can use it ad dictionary
eg1:-
num = 7
num_2 = 9
num_3 = 8
num_3 = 8
def add(*a):
    print(a)
add(num,num_2,num_3,num_4)
eg2:-
def all_(**Any):
    print(Any['Age'])
all_)(Name = "Teja",Age = 14)
----------------------------------------------------------------------
-----scope of vaiables------
1.Global vaiable:- this variable can be used throughtout the program.
eg:-
num = 9
def func_():
    print(num)
func_()

2.Local variable:- this variable can only be accesed within and function and not outsid ethe function.
eg:-
def func_():
    num = 9
    print(num)
func_()
print(num)

#note:-to change the global variable we have to add keyword global that will change the value completely inside and outside of the function. global keyword causes permenant chnages ireespective
of the before number given.
eg:-
num = 9
def func_():
    global nun
    num = 89
    print(num)
func_()
print(num)
output:-
89
89
(which tells us that the variable has completely(permenantly) changed the value from 9 to 89 because of the global keyword and this 89 continues throughout the progrram.




'''
num = 9
def func_():
    global nun
    num = 89
    print(num)
func_()
print(num)












