'''
-------Lambda function-------
this is also called as annonymous function.
---> a lamda function can take n number of arguments but having only
one expression

syntax:- lambda argumengts : expression
eg:-(we can do multiple operations)
SOme = lambda an,so,why : an + so + why
print(SOme(10,8,89))

filter()
--------
---> this function is a built in function used to filter elements from 
an iterables such as list[],tuple() and set() based on condition.

syntax:- filter(function, itterable)

--> this filter() function returns filter object so we can convert that into list,
set and tuple.
eg:-
nums = [1,2,3,4,5]
rev = filter(lambda a: a%2 == 0, nums)
print(set(rev))

eg2:-
nums = [1,2,3,4,5]
rev = filter(lambda a: a%2 != 0, nums)
print(set(rev))

---------list comprehension---------
---> this offers a shorter syntax when we want to create a new list from the old list 
syntax:- variable_name = [Expression loop condition]
eg1:- without condition
old_ = [1,2,3,4,5,6]
new_ = [j for j in old_]  {1st j is the variable which iterates}
print(new_)

eg2:-with condition
old_ = [1,2,3,4,5,6]
new_ = [j for j in old_ if j % 2 == 0]
print(new_)

------------dictionary comprehensio---------
--> this offers a shorter syntax when we want to create a new dict from the old dict
syntax:- variable_name = [expression loop]
eg:-
old_dict = {1:2,3:7,5:6}
new_dict = {i:j for (i,j) in old_dict.items() if j % 2 == 0}
print(new_dict)


'''
old_dict = {1:2,3:7,5:6}
new_dict = {i:j for (i,j) in old_dict.items() if j % 2 == 0}
print(new_dict)

