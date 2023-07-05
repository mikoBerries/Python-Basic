# other method in python List

# insert
# insert() takes in two arguments: insert(index,object) This method places the object at the index supplied. For example:

list1= [1,2,3,4,5,6,7]

# Place a 'inserted' at the index 2
list1.insert(2,'inserted')
print(list1) # -> [1, 2, 'inserted', 3, 4]


# pop
# You most likely have already seen pop(), which allows us to "pop" off the last element of a list.
# However, by passing an index position you can remove and return a specific element.

ele = list1.pop(1)      # pop the second element
print(list1)            # -> [1, 'inserted', 3, 4]
print(f"popped:{ele}")  # >>> 2

# remove
# The remove() method removes the first occurrence of a value. For example:

list1.insert(5,'inserted')
print(list1)
# remove first founded object -> 'inserted'
list1.remove('inserted')

# sort
# The sort() method will sort your list in place:

list2 = [3, 4, 2, 1]
list2.sort()
# now list2 sorted froom small to big
print(list2)            # >>> [1, 2, 3, 4]


list2.sort(reverse=True)
# now list2 sorted froom big to small
print(list2 )               # >>> [4, 3, 2, 1]