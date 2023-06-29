# There is some importan built in function 

# range
# The range function allows you to quickly generate a list of integers, this comes in handy a lot, so take note of how to use it! There are 3 parameters you can pass, a start, a stop, and a step size. Let's see some examples:

created_list= list(range(0,11))
print(created_list)

# enumerate
# enumerate is a very useful function to use with for loops.
# enumerate helping for in statement to getting index iterator

index_count = 0
my_string = 'abcde'
for letter in my_string:
    print("At index {} the letter is {}".format(index_count,letter))
    index_count += 1 # act as counter

print()

# Wrapped with enumerated becaming index ,items
# than unpacked with tuples
for i,letter in enumerate(my_string):
    print(f"At index {i} the letter is {letter}")

# Code becoming more simple and clean


# zip
# Zip is just squasing all item becoming one List of Tupels with given n items
# zip wil loopeing for shortest lenght
mylist1 = [1,2,3,4,5,6,7]
mylist2 = ['a','b','c','d','e','x','y']
mylist3 = ['a','b','c','d','e','x','y']
for item1, item2,item3 in zip(mylist1,mylist2,mylist3):
    print('For this tuple, first item was {} and second item was {} and {}'.format(item1,item2,item3))

# Zip helping us to iterate many list together 


# in & not in operator
# build it search of items from list
# to check if some object or variable is not present in a list.
print("'x' not in ['x','y','z']")
print('x' not in ['x','y','z'])

print("'x' not in [1,2,3]")
print('x' not in [1,2,3])

# min and max
# returning min / max of item type on given list
mylist = [10,20,30,40,100]
print ()

print(f"list : {mylist}")
print("min(mylist)")
print(min(mylist))

print("max(mylist)")
print(max(mylist))

# import statement from pacakge ramdong importing shufle class
from random import shuffle

print ()
# This shuffles the list "in-place" meaning it won't return
# anything, instead it will effect the list passed
shuffle(mylist)
print(f"shuffeled list: {mylist}")

from random import randint
# Return random integer in range [a, b], including both end points.
randoms = randint(0,100)
print(randoms)

# input prompt from cmd 
# imput() always porudce string 
userinput = input('Enter Something into this box: ')

print(f"your input : {userinput}")
# use type case to use other than string example
# as float
print(float(userinput))
# or as interger
print(int(userinput))

# And user input stayed as string type