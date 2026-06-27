'''
 Data types
'integer= numbers above zero'
 num = 8
 
'float = points after numbers'
 num 2 = 7.89
 num = 6.89
 print (num//2)
String
string is a sequence of char that are enclosed in ' '," ",''' '''.
String is immutable

1 concatination
Here the addition operator(+) acts as to concatinate more than two strings aslo in lists
eg=
so = "python"
any = "is a language"
print(so+any)

2 Indexing = this is used to access a particular character in a string by passing a index postion value.
indexing starts from 0
we have negative indexing to count the positions from last to first.

eg=
so = "python is a language"
print(so[12])
print(so[-2])

3 string Methods
replace():-this method is usded to to change any substring in that particular string
           syntax:- variable_name.replace("old string","new string",count)
          eg 1 :- so = "python is a language"
                 print(so.replace("python","java")
          eg 2 :-so = "python is a language"
               print(so.replace("a","A",2)

join():- this metgod helps to add new substring after each char in the string
synatax:- "string".join(variable
eg:-

split()-
this method can divide the string into different index into list, based o fthe string pass by us..
syntax:- variable_name.split('substring')
eg:-
so = "python is a language"
print(so.split("is")


                        
count()= used to count the substring in the particular string and aslo specify the index position
syntax:- variable_name.count("substring",start index,end indx)
eg:-
so = "python is a language"
print(so.count("a",0,12))


Sting built in function
1.len()= this will find length of the string, which is number of the characters present in that string.
   eg
      so = "python is a language"
print(so.len("so")

2.Max()= will gwt the max value in the string
 eg
      so = "python is a language"
print(so.max("so")
      
3.Min()= will get the min value in th string
eg=
   so = "python is a language"
print(so.min("so")

LIST DATATYPE
      List is a collection of different datatypes and enclosed in [] seperated by commas (,)
      List is muttable
      eg:-
      all_type = [1,'Python',{1,2]}

Methods in Lists:-
     1 Append():-add new items in the list.(will only take one item at a time) (gives one index value to anything you give )
      eg:- any_ [1,2,3,4}
      print(any_)
      any_.append(5)
      print(any_)
      any_.append(10)
      print(any_)
      any_.append(10)
      print(any_)
      
    2 extend():-this is also add theitem in the last index position like append but it will give each value in seperate index positions.it will take only iterables(string,list,tuple)
      any_ =[1,2,3,4]
      any_.extend('python')
      print(any_)
      print(len(any_))

    3  pop():-It is used to delete the item from the list but it will delete based on the index position
       Syntax:-Variable_name.pop(index position)
       eg:- any_ = [1,2,45,78,23,90}
           any_.pop(1)
           print(any_)

    4  remove():- it is used to delete the item from the list but it will delete the direct value from the list.
       syntax:- Variable_name.remove(value)
       eg:- any_ = [1,2,45,78,23,90}
           any_.remove(1)
           print(any_)
      
     5 insert()
      syntax:- variable_name.insert[index position][item]
      
        muttable                                                     immuttable

The datatype can be modified                             The datatype cannot be modified 
eg:-  any_ [1,2,3,4}                                      eg:-  so = 'Python is a language'                                                
      print(any_)                                          print(so.replace('python','java'))
      any_.append(5)
      print(any_)
      any_.append(10)
      print(any_)
      

 SORTED AND SORT = sorted is like "change" the list can only be change in the runtime. therefore after sorted if you print variable the original list will be displayed.
 Where as sort is like "modified" its like a permenant change of the variable. after sort if you print variable the sorted version will be printed

 
[INDEXING === any_ = [1,2,'python is a language',[45,78,"java is a language",[1,23],90],'Hello']
print(any_[2][3][10])]


homework:- any_[56,[1,2],['python',,java,['python is a language',153,90],[78,6],'I know c']]

                                   TUPLE
TUPLE is a collection of different datatypes represent in () and seperated by comma ,
      it is immutatable
      count,index,min,max,len.
eg:- how = (1,2,3,4,"python",[4,5],(90,78))
     print(how.index("python"))    
     print(how.count("python"))
     

'''













 

