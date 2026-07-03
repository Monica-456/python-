'''
Coding:-
1. prime number(single)
num = int(input("Enter a number: "))
count = 0
for j in range (1, num+1):
    if num  j == 0 :
        count += 1
        #print(count)
if count == 2:
        print(f"{num} is a prime")
else:
    print(f"{num} is  not a prime")
----------------------------------------------------------------------------------------------------
2.generating prime number:
limt_ = 10
for j in range(2,limit_+1):
    count = 0
    for i in range(1,j+1):
        if j %1 == 0:
            count += 1
            print(count)
    if count == 2:
        print(F"{j} is a prime")

3. *
   * *
   * * *
   * * * *
   * * * * *
num = 5
for j in range(1,num+1):
    for i range(1,j+1):
        print("*", end = " ")
        print()
--------------------------------------------------
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
num = 5
for j in range(1,num+1):
    for i range(1,j+1):
        print("j", end = " ")
        print()
-------------------------------------------------
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
num = 5
for j in range(1,num+1):
    for i range range(1,j+1):
        print("i", end = " ")
        print()
----------------------------------------------------
find question
num = 4
count = 0
for j in range(1,num+1):
    for i range(1,j+1):
        count += 1
        print(i, end = " ")
     print()
------------------------------------------------------
1
1 2
1 2 3
1 2 3 4
num = 4
count = 0
for j in range(num,0,-1):
    for i range(1,j+1):
        count += 1
        print(i, end = " ")
     print()
----------------------------------------------------
amstrong number:-
am_str = 153
length_ = len(str(am_str))
all_sum = 0
for j in str(am_str):
    all_sum += int(j) ** length_
if all_sum ==am_str:
    print(f"{am_str} is amstrong")
else:
    print(f"{am_str} is not a amstrong")
--------------------------------------------------------
pyramid:-
      *
     ***
    *****
   *******
  *********
 ***********
num = 6
for j in range(num):      #whenever starts with range it starts with 0
    print(" " *(num-j-1),end =" ")
    print("*" *(2 * j +1))
----------------------------------------------------------





'''

'''
prime:-
num = int(input("Enter a number: "))
count = 0
for j in range (1, num+1):
    if num  j == 0 :
        count += 1
        #print(count)
if count == 2:
        print(f"{num} is a prime")
else:
    print(f"{num} is  not a prime")
------------------------------------------------
limt_ = 10
for j in range(2,limit_+1):
    count = 0
    for i in range(1,j+1):
        if j %1 == 0:
            count += 1
            print(count)
    if count == 2:
        print(F"{j} is a prime")
----------------------------------------------------------------
num = 5
for j in range(1,num+1):
    for i range range(1,j+1):
        print("*", end = " ")
        print()
----------------------------------------------------
num = 5
for j in range(1,num+1):
    for i range range(1,j+1):
        print(j, end = " ")
        print()
---------------------------------------------------------------
num = 10
for j in range(1,num+1):
    for i range(1,j+1):
        print(i, end = " ")
        print()
------------------------------------------        
num = 4
count = 0
for j in range(1,num+1):
    for i range(1,j+1):
        count += 1
        print(i, end = " ")
     print()
-------------------------------------
num = 4
count = 0
for j in range(num,0,-1):
    for i range(1,j+1):
        count += 1
        print(i, end = " ")
     print()
---------------------------------
num = 6
for j in range(num):
    print(" " *(num-j-1),end =" ")
    print("*" *(2 * j +1))
'''
    
num = 4
for j in range(num):      #whenever starts with range it starts with 0
    print(" " *(num-j-1),end =" ")
    print("*" *(2 * j +1))
 
