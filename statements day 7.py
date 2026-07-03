'''
statements
1.conditional statements:-
-------------------------------------
if==== used to
eg:-
num = 9
if num % 2 == 0:
    print(f'{num}' is an even number")
---------------------------------------
if-else====else is a fall back statement incase the if condition is false,the
eg 1:-
num = 9
if num % 2 == 0:
    print(f'{num} is an even number")
else:
    print(f"{num} is an odd number")

eg 2:-
Monica_ICIC_details = ("ATM PIN" : '6600')
pin_ = input("enter your 4 digit AtM pin: ")
if pin_ in Monica_ICIC_details['ATM PIN']:
    print("welcome to ICIC ATM")
else:
    print("you have entered incorrect pin")
-----------------------------------------
nested if:- if inside if
eg:-
Monica_ICIC_details = {"ATM PIN":'6600'}
pin_ = input("enter your 4 digit AtM pin: ")
if len(pin_) == 4:
  if pin_ in Monica_ICIC_details['ATM PIN']:
      print("welcome to ICIC ATM")
  else:
      print("you have entered incorrect pin")
else:
    print("please enter only a 4 digit pin")
---------------------------------------------
elif:-this give to execute or check multiple values
eg:-
marks_ = int(input("enter yor marks: "))
if marks_ >=90:
   print("A+")
elif marks_ >=80:
    print("B+")
elif marks_ >=70:
    print("C")
else:
    print("failed")


task for finding the maximum number:-
a=10
b=20
c=30
if a>b &a>c:
    print ("a is the maximum value")
elif b>a & b>c:
    print("b is the maximum vallue")
else:
    print("c is the maximum value")

task for finding a letter os a voel or a consonant.
so_ = input("enter a letter: ")
if so_ in 'aeiou':
    print(f"'{so_}' is a vowel")
else:
    print(f"{so_} is a consonant")
'''


so_ = input("enter a letter: ")
if so_ in 'aeiou':
    print(f"'{so_}' is a vowel")
else:
    print(f"{so_} is a consonant")
     






























