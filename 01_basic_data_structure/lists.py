# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists can have multiple object type
my_list = [1,2,3,4,"abc"]
print(my_list)

# assigment
my_list[0]="pop this"
print(my_list)
# append
my_list.append("new item")
print(my_list)

# popping a list like a stack default is top of list or with param 
print(my_list.pop(0))
print("after pop :",my_list)

to_sort_list =["a","x","asdas","y","b","z"]
# build in sort func in list
to_sort_list.sort()
print(to_sort_list)

# reverse list
to_sort_list.reverse()
print(to_sort_list)