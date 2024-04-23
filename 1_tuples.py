#Tuples are a datatype simialr to a list, with the exception that they are immutable

#Characteristics:
#-- Immutable : you cannot edit the data of a tuple with having to reassign it.
#-- Ordered : Like lists they have an order, and you can access the elements by index
#-- Like lists, they can store a variety of objects including duplicate objects

#Why bother:

#Create a collection that will not be changed by you or another dev

#Iterating over a tuple is faster than iterating over a list.

#creating Tuples
#we use () to define tuples
empty_tup = () #empty no items

#Singletonm, tuple with one item

singleton = ('element',) #requires a trailing comma

print(type(singleton))
print(singleton)

#multi-element tuple: don't need a trailing comma

pop_tup = ('this', 'is', 'a', 'populated','tuple')
print(pop_tup)

variety_tup = (4, 'Five', 6.0, [7,8,9], {'ten': 10}) #can store just about anything
print(variety_tup)

duple =(True, True, True, False, False, False) #and also store duplicates
print(duple)

#packing tuples : without parens 

packed = 't-shirt', 'pants', 'jacket', 'socks'
print(packed)
print(type(packed))

#pakcing vars into tuple
tup_pack = pop_tup, variety_tup, duple
print(tup_pack)


#Indexing and Slicing Tuples

pop_tup = ('this', 'is', 'a', 'populated','tuple')
print(pop_tup[3][4])
print(pop_tup[1])


variety_tup = (4, 'Five', 6.0, [7,8,9], {'ten': 10}) #can store just about anything
print(variety_tup[3][0])


print(tup_pack)
print(tup_pack[1][-1]['ten'])

#Slicing [start:stop] : default start = 0 and stop = end of the tuple
#stop is not included

duple =(True, True, True, False, False, False) #and also store duplicates
print(duple[:3]) #return a sub-tuple from 0-3 

print(duple[1:4])

print(duple[3:6])

#Inclass Indexing

historical_record = ("Medieval Era", ("Knights", "Castles", ("King", "Queen")), "Renaissance Period")
print(historical_record[1][2][1])

mythical_collection = ("Greek Myths", 
                        [    
                           ("Zeus", "Hera"),
                           [
                               "Mount Olympus", 
                               (
                                   "Lightning", 
                                   "Thunder")]], 
                       "Norse Myths")
print(mythical_collection[1][1][1][0])
