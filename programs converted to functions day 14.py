'''
nums = [23,4,56,23,7,4]
empty_ =[]
def removes_(nums,empty):
    for j in nums:
        if j not in empty_:
            empty_.append(j)
    print(empty_)
removes_(nums,empty_)

2. prime number
prime_ = 7
count = 0
def prime_not(prime_, count):
    for j in range(1,prime+1):
        if prime_%j==0:
            count += 1
        if count == 2:
            print(f'{prime_} is a prime')
        else:
            print(f'{prime_} is not a prime')
prime_not(prime_,count)

3.counting
some = "python is a programmimg language"
count = 0
def counting(some,count):
    so = some.split(' ')
    for j in so:
        count += 1
    print(count)
counting(some,count)

4. captical small and space count
some = "python Is a proGraMmimg lanGuagE"
cap_count = 0
small_count = 0
space_count = 0
def cap_small(some,cap_count,small_count,space_count):
    for j in some:
        if j.isupper():
            cap_count += 1
        elif j.islower():
            small_count += 1
        else:
            space_count += 1
    print(f'There are total {cap_count} number cap')
    print(f'There are total {small_count} number cap')
    print(f'There are total {space_count} number cap')
cap_small(some,cap_count,small_count,space_count)

5.
def palindrome(so):
    empty_ = ""
    for j in so:
        empty_ = j + empty_
    if empty_ == so:
        print(f"{so} is a palindrome")
    else:
        print(f"{so} is not a palindrome")
palindrome("Garikapati")
palindrome("madam")
palindrome("mom")
palindrome("dad")
palindrome("chandu")

6.
eg:perfect number
num = 28
sum_ = 0
def perfect(num, sum_):
    for j in range(1, num):
        if num % j == 0:
            sum_ += j
    if sum_ == num:
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is not a perfect number")

perfect(num, sum_)

'''

num = 28
sum_ = 0
def perfect(num, sum_):
    for j in range(1, num):
        if num % j == 0:
            sum_ += j
    if sum_ == num:
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is not a perfect number")
perfect(num, sum_)










 
