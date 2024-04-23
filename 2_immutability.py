#Immutablitiy means the data of a tuple cannot be adjusted in its location in memory

tup1 = (1,2,3,4,5)
print(tup1)

# tup1[3] = 'four' # Will throw a TypeError since tuples cant do this

#YOU CANT CHANGE TUPLE DATA IN PLACE

#-- Small work around to chane items in a tuple
#convert the tuple into a list, make changes, convert back to tuple

tup1 =  1,2,3,4,5
print(id(tup1))
tup1 = list(tup1)
tup1[3] = 'four'
tup1 = tuple(tup1)
print(id(tup1))

#-- concatenating tuples : adding them together

tup1 = 1,2,3,4,5
tup2 = 6,7,8,9,10

tup1 += tup2
print(tup1)

#-- repeating tuples

short_story = 'A tale', #make sure to have your trailing comma
print(short_story)
anthology = short_story * 3
print(anthology)