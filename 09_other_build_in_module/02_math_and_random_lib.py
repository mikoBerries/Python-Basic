# math lib populate all matematict math function
import math
value=4.35
print(f"value={value}")
print("math.floor(value)")
print(math.floor(value))

print("math.ceil(value)")
print(math.ceil(value))

print()
print("round(4.5)")
print(round(4.5))
print()
print(round(5.5))

# 3.14
math.pi
math.e

math.inf #infinty
math.nan #nan

# for depper matehamty wes can use numpy lib

math.log(math.e)
math.log(1000,10) #3.0 --> 10**3

print()
# random lib

import random

rand = random.randint(0,100) # random int  0 - 100
print(rand)

mylist =list(range(0,20))

# picking random choice
random.choice(mylist)
print()
# random picking with given items
random.choices(mylist,10) # returning list

print()
# random picking withour duplicate value
random.sample(mylist)

print()
# shuffleing list
random.shuffle(mylist)

print()
# getting flot value from 0~100
random.uniform(a=0,b=100)