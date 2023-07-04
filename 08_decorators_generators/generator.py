# genertor function in python is just like next level of constructor function in common language
# it's helping programmer to store a result in manner way
# in a simple way generator is generate contents of something
# commonly usage is range(0,10) => is fedeing for with syntax with list 0~10 without making a list object it self
# Generators are useful when we want to produce a large sequence of values, but we don't want to store all of them in memory at once.

def create_cube_normal(n):
    result=[]
    for x in range (n):
        result.append(x**2)

    return result

def create_cube_generators(n):
    for x in range (n):
        yield x**2

print("printing cube with list as feeder")
for x in create_cube_normal(10):
    print(x)

print("printing cube with generator as feeder")
for x in create_cube_generators(10):
    print(x)

print("producing same result but with generator we achive memory wise usage since list object are not created")

# when generating generator function generator function is remembering states of all param
# in function are defined and continue it after is needed again
def genfibon(n):
    """
    Generate a fibonnaci sequence up to n
    """
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b


print(genfibon(10))
print(type(genfibon(10)))

# parse it as list if we needed list object to work with
print(list(genfibon(10)))

for num in genfibon(10):
    print(num)

# least but rarely use to iter() a iterad object liek string etc

def simple_gen():
    for x in range(3):
        yield x

# Assign simple_gen 
g = simple_gen()
print(next(g))
print(next(g))
print(next(g))
try:
    # after 4x item used iterator sending eror because it's end of data
    print(next(g))
except:
    print("error happends")

s = 'hello'

#Iterate over string
for let in s:
    print(let)

s_iter = iter(s)

# s_iter can used whit next function 
next(s_iter)
next(s_iter)
next(s_iter)
next(s_iter)

# If the output has the potential of taking up a large amount of memory and 
# you only intend to iterate through it, you would want to use a generator.
# some other use case

import random

def rand_num(low,high,n):

    for i in range(n):
        yield random.randint(low, high)

for num in rand_num(1,10,12):
    print(num)



my_list = [1,2,3,4,5]

# use generator function instead to iterate all result 
gencomp = (item for item in my_list if item > 3)

# extract all value using generator
for item in gencomp:
    print(item)
