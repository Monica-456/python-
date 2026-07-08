'''
passing by value:-
def some(a):
    for j in a:
        print (j)
some([1,2,3])

passing by referance:-
a = (1,2,3)
def some(a):
    for j in a:
        print (j)
some(a)

return keyword:-in a function if reuturn is executed then it will exit from the function with certain return values.
eg:-
4def myfunc_(b):
    return 5+b
a = myfunc_(10)
c = myfunc_(100)
print(a)
print(c)

###builtin functions###
import builtins
builtin_functions = [
    name for name in dir(builtins)
    if callable(getattr(builtins,name))]
print(builtin_functions)
print(f"Total built-in functions are {len(builtin_functions)}"
###

Recursive function:-
---->recursive function that calls itself repeatedly until a specified condition is met.
syntax:-
def func_name(parameter):
    if condition base : ---> base case
        return statement
    else:
         return statement
print(func_name(arguments))

eg:-
def func_name(num):
    if  num== 1:               {factoriall form}
        return 1
    else:
         return num * func_name(num-1)
num = 10
print(func_name(num))difference btw print and return:- print prints the value that is asked to display, return holds the value and stores that value in the calling function.
'''











