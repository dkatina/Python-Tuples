#Unpacking Tuples

#packing tuples reminder

packed = 'bacon', 'lettuce', 'tomato'
print(packed)

#basic upacking

first, second, third = packed

print(first)
print(second)
print(third)

#Will throw a ValueError if the vars and items are not equal
#-- too many values to unpack
#-- not enough values to unpack


#extended unpacking : takes addition varless values and packs them into a list

#everything that doesnt have a home, ends up in the star bin
enhanced_blt = 'bacon', 'lettuce', 'tomato', 'mayo', 'avocado', 'everthing bagel seasoning'
print(enhanced_blt)
first, second, third, *condiments = enhanced_blt
print(first)
print(second)
print(third)
print(condiments)

story = 'intro', 'conflict', 'build', 'big reveal', 'climax', 'conclusion'

beginning, fight, *middle, end = story
print(beginning)
print(tuple(middle))

print(end)
print(fight)

#You can't have multiple * expressions or you'll get a SyntaxError