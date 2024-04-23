#looping over tuples is the exact same as looping over lists


#werite a function that loops over a given tuple

def tup_loop(atuple):

    for item in atuple:
        print(item)

my_tup = 'apple', 'banana', 'orange'

tup_loop(my_tup)


def while_tup(atuple):
    i = 0
    while i < len(atuple):
        print(atuple[i])
        i+= 1

teams = 'Bull Dogs' , 'Falcons', 'Hawks', 'Braves'

while_tup(teams)

#-- enumerate() that allows you to iterate over the index and item at the same time

today = 'woke up', 'ate breakfast', 'walked my dog', 'prepped lecture', 'ate lunch', 'graded', 'meetings', 'in class'

for task in enumerate(today): #task is a tuple of the index and item
    print(task[1])

print('--------------------')

for idx, task in enumerate(today):
    print(idx)
    print(task)