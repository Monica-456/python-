'''
Error Handling:-
===============
syntax error:-


indentation error:-
-----------------
   a = 20
for j in range(a):
    print(j)
else:
print()

o/p:-- IndentationError

value error:-
---------------

num = int(input("Enter a num: "))

o/p -- ValueError

exception handling:

try:-
-----
the try block will test the code for error

syntax -- try:

except:-
-------
this except block let us handle the errors in the code

syntax -- except:

eg1:-
try:
    print (num)
except NameError:
    print('will get name error')
output:--
will get name error

eg2:-
try:
    num = int(input("Enter a num: "))
    num_2 =int(input("Enter a num: "))
    print (num/num_2)
except:
    print('will get zerodivision error')
--------------------here if you not give exception the code give show error if except is kept the code eill go to the except and print the staement in the except if you have error in try.
    num = int(input("Enter a num: "))
num_2 =int(input("Enter a num: "))
print (num/num_2)

output:-
Enter a num: 78
Enter a num: 0
Traceback (most recent call last):
  File "C:/Users/Satya Monica/OneDrive/Desktop/codegnan/exception handling day day 24.py", line 67, in <module>
    print (num/num_2)
ZeroDivisionError: division by zero


else:
======
#if the try blck does not have any error then it will go to the else block and else block will be executed.

try:
    num = int(input("Enter a num: "))
    num_2 =int(input("Enter a num: "))
    print (num/num_2)
except ZerodivisionError:
    print('will get zerodivision error')
except NameError:
    print('will get zerodivision error')
else:
    print('No Error')

output:---
Enter a num: 45
Enter a num: 9
5.0
No Error

((Errors occuredd:--- #if there is an Error then it will show errors value and zerodivision.
~Enter a num: hhjh
Traceback (most recent call last):
  File "C:/Users/Satya Monica/OneDrive/Desktop/codegnan/exception handling day day 24.py", line 82, in <module>
    num = int(input("Enter a num: "))
ValueError: invalid literal for int() with base 10: 'hhjh'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/Satya Monica/OneDrive/Desktop/codegnan/exception handling day day 24.py", line 85, in <module>
    except ZerodivisionError:
NameError: name 'ZerodivisionError' is not defined. Did you mean: 'ZeroDivisionError'?

= RESTART: C:/Users/Satya Monica/OneDrive/Desktop/codegnan/exception handling day day 24.py
~Enter a num: 78
Enter a num: 0
Traceback (most recent call last):
  File "C:/Users/Satya Monica/OneDrive/Desktop/codegnan/exception handling day day 24.py", line 84, in <module>
    print (num/num_2)
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/Satya Monica/OneDrive/Desktop/codegnan/exception handling day day 24.py", line 85, in <module>
    except ZerodivisionError:
NameError: name 'ZerodivisionError' is not defined. Did you mean: 'ZeroDivisionError'? )

finally:---
==========
finally block will execute either you have error or not in your code.

eg:-
try:
    num = int(input("Enter a num: "))
    num_2 =int(input("Enter a num: "))
    print (num/num_2)
except ZerodivisionError:
    print('will get zerodivision error')
except NameError:
    print('will get zerodivision error')
else:
    print('No Error')

finally:
    print('End of the code')

output:-
Enter a num: 45
Enter a num: 9
5.0
No Error
End of the code
'''





































