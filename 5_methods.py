#Tuples don't have too many methods

#-- tuple.count(item) : counts how many times an item appears in a tuple

shopping = 'eggs', 'milk', 'creamer', 'creamer', 'creamer', 'creamer', 'chicken'

print(shopping.count('creamer'))

#-- len(tuple) : give the length of the tuple

print(len(shopping))

#-- tuple.index(item) : returns the first index of an item

print(shopping.index('chicken'))
print(shopping.index('creamer'))


#-- Membership checks of a tuple, if item in tuple, 'in', Returns True or False depending

print('creamer' in shopping)
print('Cinnamon Toast Crunch' in shopping)


nest = 'start', ('early', 'middle', 'towards end'), 'end'



for item in nest:
    if isinstance(item, tuple) and 'most' in item:
        print('I found the middle')