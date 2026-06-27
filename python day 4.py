'''
 DICTIONARY
 dict is a key:value pair seperated by :, and keys should be unique.(no duplicate value is allowed)
 in the place of keys we have to use immuttable datatype. in values we can use any datatype either muttable or immuttable. (string,tuple,list)
details_ = ("name" : "monica",
            1:"number"
            (6,7):[1,2];
print(details_)

methods ===
keys():- used to get all the keys from the dictionary
syntax:- variable_name.keys
eg:-details_ = {"name" : "monica",
            1:"number"
            (6,7):[1,2]}
print(details_)
value:-
items()

clear():- used to cleqar the dictionary
eg:- details_ = {"Name": "monica",
            "Age" :  "21",
            "Gender" : "Female"}
details_.clear()
print(details_)

Update():- used to update only values in the dictionary.
eg:-details_ = {"name" : "monica",
            "Age":"21",
            "Gender": "Female"}
details_.update({"mob":123456789})
print(details_)

   SET
It is a collection of unordered elemets that are seperated by comma.
set is a muttable
it can remove duplicates by itself.
no duplicates are allowed.

go = {1,2,3,4,2}
print(go)

methods

union():- combine the elements from both sides.
syntax:-set_1.union(set_2)
eg:-
go = {1,2,3,4}
so = {4,5,6,7}
print(go | so)
print(go.union(so))

intersection():- gives the common element from both the sets.
syntax:- set_1.intesection(set_2)
eg:-
go = {1,2,3,4}
so = {4,5,6,7}
print(go & so)
print(go.intersection(so))

symmetric Difference() :- removes commom elemests and gives all different elements from both sets
syntax:- set_1.symmetric_difference(set_2)
eg:-
go = {1,2,3,4}
so = {4,5,6,7}
print(go ^ so)
print(go.symmetric_Difference(so))

add():- used to add new elements into set
eg:-go = {1,2,3,4}
go.add(5)
print(go)

remove():- del the elements from set based on element. but if there is no metioned element in the set it shows error.
eg:-go = {1,2,3,4}
go.remove(2)
print(go)

pop():-removes the last elements from the set if not mentioned the index value 
eg:-go = {1,2,3,4}
go.pop()
print(go)

discard():- removes the elementjust like the remove() but it doesnt show error like remove()
eg:-go = {1,2,3,4}
go.discard(5)
print(go)

DIFF BTW REMOVE AND DISCARD
both does the same work but,remove throws error when element is not there in the set byt discard do not do like that
'''


details_ = {"name" : "monica",
            "Age":"21",
            "Gender": "Female"}
details_.update({"mob":123456789})
print(details_)


{"name" : "monica",
                 "Age":"21",
                "Gender": "Female"}
details_.update({"mob":123456789})
print(details_)










