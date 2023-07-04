# python debugger
# debugger in python allow us stop at some state we want
# and calling every value was assign happened before called
import pdb

x=[1,2,3]
y=2
z=3
result  = y+z
pdb.set_trace()

result2 = x+y