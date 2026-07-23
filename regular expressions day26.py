'''
---------------Regular Expression(RegEx)--------------------
~RegEx is an sequence of char that can searching pattern.
~To use RegEx
syntax:- import re

Functions::-
1.findall():-
-->it will find all the char that are in the string..
eg:-
import re
txt = 'python is a language and also called dynamically typed'
print(re.findall('[an]',txt))
output:-
['n', 'a', 'a', 'n', 'a', 'a', 'n', 'a', 'a', 'n', 'a', 'a']

2.search():-
-->the search() will find the character bur it will give the first sequence or occurance that found in the string.
eg:-
import re
txt = 'python is a language and also called dynamically typed'
print(re.search('[a]',txt))
output:-
<re.Match object; span=(10, 11), match='a'>

3.split:-
--> splits the string into different indexs. before split one index after split one index.
eg:-
import re
txt = 'python is a language and also called dynamically typed'
print(re.split('[ ]',txt))
output:-
['python', 'is', 'a', 'language', 'and', 'also', 'called', 'dynamically', 'typed']

4.sub:-
-->sub() works similar to replace
eg:-
import re
txt = 'python is a language and also called dynamically typed'
print(re.sub(' ','&',txt)
output:-
python&is&a&language&and&also&called&dynamically&typed

Metachar
==========
we have only symbols im Metachar.SHOULD ALWAYS KEPT IN SINGLE QUOTES(STRINGS)
[]:-
==
EG:-
import re
txt = 'I have 100 Ruppees'
print(re.findall('[0-9]',txt))
print(re.findall('[a-z]',txt))
print(re.findall('[A-Z]',txt))
output:-
['1', '0', '0']
['h', 'a', 'v', 'e', 'u', 'p', 'p', 'e', 'e', 's']
['I', 'R']
eg2:- give the first occurence of a specified character in the string
import re
txt = 'I have 100 Ruppees'
print(re.search('[0-9]',txt))
print(re.search('[a-z]',txt))
print(re.search('[A-Z]',txt))
output:-
<re.Match object; span=(7, 8), match='1'>
<re.Match object; span=(2, 3), match='h'>
<re.Match object; span=(0, 1), match='I'>

^:-used to check whearther a string is staring with particular thing or not
==
eg:-
import re
txt = 'I have 100 Ruppees'
print(re.findall('^I have',txt))
print(re.search('^I have',txt))
output:-
['I have']
<re.Match object; span=(0, 6), match='I have'>


$:- helps to find wheather a string is ending with particular thing or not
==
eg:-
import re
txt = 'I am going to school'
print(re.findall('school$',txt))
print(re.search('school$',txt))
output:-
['school']
<re.Match object; span=(14, 20), match='school'>

.:- dot is used to find fill in the blanks strings
==
eg:-
import re
txt = 'Hello! This is Teja'
print(re.findall('T...',txt))
print(re.search('T...',txt))
output:-
['This', 'Teja']
<re.Match object; span=(7, 11), match='This'>

*:-give the string until the specified character
==
eg:-
import re
txt = 'python module will going to complete this week'
print(re.findall('p.*n',txt))
print(re.findall('p.*ython',txt))
print(re.findall('p.*',txt))
output:
['python module will goin']
['python']
['python module will going to complete this week']

+:-Adds from one character to n number of characters. that + symbol will search for one character that is missing.and will searc for the matching word.
==
eg:-
import re
txt = 'python is a language'
print(re.findall('p.+n',txt))
print(re.findall('p.+ython',txt))
print(re.search('p.+a',txt))
output:
['python is a lan']
[] #gives empty string because + does not have anything to match and give the output. + means it will match with anything and then give the output
<re.Match object; span=(0, 18), match='python is a langua'>

{}:-used for specific index numbers.
==
eg:-
import re
txt = 'python is a language'
print(re.search('p.{10}',txt))
print(re.findall('p.{10}',txt))
output:
<re.Match object; span=(0, 11), match='python is a'>
['python is a']
'''






















