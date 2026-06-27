'''
LIST DATATYPE
      List is a collection of different datatypes and enclosed in [] seperated by commas (,)
      List is muttable
      eg:-
      all_type = [1,'Python',[1,2]]

Methods in Lists:-
     1 Append():-add new items in the list.(will only take one item at a time) (gives one index value to anything you give. any datatype can be a string also )
      eg:- any_ = [1,3,2,4]
print(any_)
any_.append(5)
print(any_)
any_.append(10)
print(any_)
any_.append(10)
print(any_)
      
    2 extend():-this is also add theitem in the last index position like append but it will give each value in seperate index positions to single charactersif it is in the form of string.
    it will take only iterables(string,list,tuple)
     eg:- any_ =[1,2,3,4]
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
      
     5 insert():- HELPS TO INSERT A NEW ITEM IN THE LIST. here two types we can give index number to add an item at a specific place or if we use just (insert(value)) it will be added at the last.
      syntax:- variable_name.insert(index position,item)
      eg:- any_ = [1,2,45,78,23,90]
           any_.insert(2,12)
           print(any_)
      


        muttable                                                     immuttable

The datatype can be modified                             The datatype cannot be modifiedcan only be changed in runtime
eg:-  any_ [1,2,3,4}                                      eg:-  so = 'Python is a language'                                                
      print(any_)                                               so.replace('python','java')
      any_.append(5)                                            print(so)
      print(any_)
      any_.append(10)
      print(any_)
      

 SORTED AND SORT = sorted is like "change" the list can only be change in the runtime. therefore after sorted if you print variable the original list will be displayed.
 Where as sort is like "modified" its like a permenant change of the variable. after sort if you print variable the sorted version will be printed

 
[INDEXING === any_ = [1,2,'python is a language',[45,78,"java is a language",[1,23],90],'Hello']
print(any_[2][3][10])]


homework:- any_ = [56,[1,2],['python',,java,['python is a language',153,90],[78,6],'I know c']]

                                   TUPLE
TUPLE is a collection of different datatypes represent in () and seperated by comma ,
      it is immutatable
      count,index,min,max,len.
eg:- how = (1,2,3,4,"python",[4,5],(90,78))
     print(how.index("python"))    
     print(how.count("python"))

'''



any_ = [1,2,'python is a language',[45,78,"java is a language",[1,23],90],'Hello']
print(any_[2][3][10])








 





















