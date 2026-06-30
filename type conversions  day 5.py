'''
Type conversions

This is the process of converting one data type to another.
int==string;float
eg:-
num = 89
num_2 = float(num)
print(num_2)
print(type(num))
so = str(num)
print(type(so))

float==string;int.
eg:-num = 8.9
how = str(num)
print(how)
print(type(how))
num_2 = int(num)
print(num_2)

string== integer;float;list;tuple.(to convert str ti integer===only possible in the string contains digits inside it)
eg:-
hai = "79"
num = int(hai)
print(num+10)
eg:-float
hello = "67.89"
num_2 = float(hello)
print(hello)
eg:-list
any_ = "123456"
so = list(any_)
print(so)
eg:-tuple
any_ = "123456"
so = tuple(any_)
print(so)

list== string;tuple
eg:-str
var_ = ['p','y','t','h','o','n']
text_ = "".join(var_)
print(text_)
eg:-tuple
var_ = ['p','y','t','h','o','n']
text_ = tuple(var_)
print(text_)
eg:-dict
pyth_ = [('a',1),('b',2)]
conversion = dict(pyth_)
print(conversion)

tuple==list;string
eg:-
fam = (1,2,3,4,5)
print(list(fam))
eg:-
fam = ('h','e','l','l','o')
text_2 = "".join(fam)
print(text_2)


built-in functions===
str()
float()
int()
list()
dict()


'''
fam = (1,2,3,4,5)
print(list(fam))

fam = ('h','e','l','l','o')
text_2 = "".join(fam)
print(text_2)







          
