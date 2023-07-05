# other method in python Dictionary

# Dictionary Comprehensions
# Just like List Comprehensions, Dictionary Data Types also support their own version of comprehension 
# for quick creation. It is not as commonly used as List Comprehensions, but the syntax is:

d ={x:x**2 for x in range(10)}
print(d)
# >>> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# not common usage but it can
print("this is all the keys:")
# iter key /value in dictionary
for k in d.keys():
    print(k)
print("this is all the value:")
for v in d.values():
    print(v)