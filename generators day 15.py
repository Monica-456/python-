'''
----Generator----
--> this generator is special function that returns the iterator, instead of returing
all the values at once..
--> here we are going to use yield keyword
eg:-
def some():
    yield 1    
    yield 2                      #the value comes only when it is called using next() keyword
    yield 3
so = some()
print(next(so))
print(next(so))
print(next(so))

working of generator:-
---------------------
--> when a function is called
--> it does not execute the function immediately
-->it will return the generator object
-->then the function will pauses at each yeild.
-->when the next() is called again,execution resumes from where it stopped.
eg:-
def demo():
    print("start")
    yield 1

    print("middle")
    yield 2

    print("middle")
    yield 3
how = demo()
print(next(how))
print(next(how))

with generator for loops:---
def how(so):
    for i in range(so):
        yield 1*1
any_ = how(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))

without generator:---
def sqt(n):
    for j in range(n):
        print(j*j)
sqt(5)

yield keyword:-
---> this produces the value just like return
---> but the yield pauses the function unlike reuturn
---> and yield will save the functions current state
--->yield will continue where it stopped. 

netxt():-
--->the next() function is used to retrieve the next value from a generator.

stopiteration:-
--------------
---> calling next function after all values been retrieved, then it will raise stopiteration exception.
eg:-
def how(so):
    for i in range(so):
        yield 1*1
any_ = how(5)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))

##def how(so):
    for i in range (so):
        yield i+2*2
sum_ = how(10)
print(next(sum_))
print(next(sum_))
print(next(sum_))
print(next(sum_))
print(next(sum_))
print(next(sum_))
print(next(sum_))##

--Generator Expression--
------------------------
-->the generator expression is similar to a list comprehension but uses parenthesis() instead of []
eg:-
gen = (x*x for x in range(5))
print(next(gen))
print(next(gen))                       #where x*x is argument and x is expression
print(next(gen))
print(next(gen))
print(next(gen))


'''

gen = (x*x for x in range(5))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))












































