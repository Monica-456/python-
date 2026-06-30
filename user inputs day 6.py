'''
             input formatting from user
 input()
the input function is used to take from the user.
1. integer:- to take input as integer.
eg:-num = int(input("enter a number :"))
num_2 = int(input("enter a number:"))
print(num+num_2)

2. string():- we can take anything here as input it takes as string only even numbers.
eg:-so = input("enter a char :")
print(so+"monica")

3.float():- only takes integers.
eg:-num = float(input("enter your salary :"))
print(num, "is your salary")

4.List() :- coverts to list for int 
eg:-group_ = list(map(int,input().split()))
print(group_)
eg2:-group_ = list(input())
print(group_)

5. tuple:-
eg:-tuple(map(int,input().split()))
print(group_)
eg:-tuple(input().split())
print(group_)

===== eval keyword :-- gives you the type of data passed. 
num = eval(input("Enter : "))
print(type(num))========

===string and f-string===
there is nothing different btw them but f string gives the values of the variable. it has to be kept within curly brackets.we can also perform arthematic operations
where as string gives direct values.
eg:-
name_ = input("enter your name: ")
age_ = int(input("enter your age: "))
print(name_,"your age is",age_)
print(f"{name_} your age is {age_+6}")
output:-
enter your name: monica
enter your age: 21
monica your age is 21
monica your age is 27

modules string formatting:- uses modules symbol to assign values. its done without any use of commas to seperate the string
eg:-
name_ = input("enter your name: ")
age_ = int(input("enter your age: "))
print("My name is %s i'm %d years old" %(name_,age_))
output:-
enter your name: monica
enter your age: 21
My name is monica i'm 21 years old

(three types to take user input:- seperating with commas
with f strings:- curly braces
modules string)

'''

num = float(input( ))
print(num, "is your salary")
















