# other method in python set

# adding set
s =set()
s.add(1)
s.add(2)
s.add(3)

# copy
# returns a copy of the set. Note it is a copy,
# so changes to the original don't effect the copy.
remove_this = s.copy()

# discard
# Removes an element from a set if it is a member. 
# If the element is not a member, do nothing.
print(f"initial set:{s}")
s.discard(2)
print(f"discarted 2 :{s}")

# clear
# removes all elements from the set

remove_this.clear()
print(remove_this)

# difference
# difference returns the difference of two or more sets. The syntax is:
s2=set()
s2.add(1)
s2.add(2)
s2.add(100)
print(f"set1:{s}")
print(f"set2:{s2}")
print("set 1 diffrent from set 2:")
print(s.difference(s2))

# difference_update
# dthe method returns set1 after removing elements found in set2
s1 = {1,2,3}
s2 = {1,4,5}
print(s1.difference_update(s2)) #-> {2, 3}

# intersection (opposite of diffrence) and intersection_update
# Returns the intersection of two or more sets as a new set.(i.e. elements that are common to all of the sets.)
s1 = {1,2,3}
s2 = {1,2,4}
print(s1.intersection(s2)) # -> 1,2  what data are sliced lik edb relational

# intersection_update will update a set with the intersection of itself and another.
s1.intersection_update(s2)
print(s1)


# isdisjoint
# This method will return True if two sets have a null intersection.
s1 = {1,2}
s2 = {1,2,4}
s3 = {5}

print(s1.isdisjoint(s2)) #-> False
print(s1.isdisjoint(s3)) #-> True


# issubset
# This method reports whether another set contains this set.
s1 = {1, 2}
s2 = {1, 2, 4}
print(s1.issubset(s2)) # -> True

# issuperset
# This method will report whether this set contains another set.

print(s2.issuperset(s1)) #-> True
print(s1.issuperset(s2)) #-> False

# symmetric_difference and symmetric_update
# Return the symmetric difference of two sets as a new set.(i.e. all elements that are in exactly one of the sets.)
s1 = {1, 2}
s2 = {1, 2, 4}

print(s1.symmetric_difference(s2)) # >>> {4}

s1.symmetric_difference_update(s2)
print(s1) # >>> s1 = {4}

# union (combine)
# Returns the union of two sets (i.e. all elements that are in either set.)
s1 = {1, 2, 5}
s2 = {1, 2, 4}

print(s1.union(s2)) # >>> {1, 2, 4, 5}

# update
# Update a set with the union of itself and others.

s1.update(s2)
print(s1) # >>> s1 value become = {1, 2, 4, 5}