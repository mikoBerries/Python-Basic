# this collections.Counter help counting object in list
# Counter is inheritance from dictionary
from collections import Counter


mylist =[1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,3]
mylist2 =['a','a','a','a','a','a','a','b',100000]
mystring ='asdasdasdikhasdhiuasdzzzaai19230'

print(f"original list : {mylist}")
c = Counter(mylist)
print(c)

print(f"original list : {mylist2}")
c = Counter(mylist2)
print(f"result :{c}")


print(f"original list : {mystring}")
c = Counter(mystring)
print(f"result :{c}")
print(f"c.mostcommon(3) :{c.most_common(3)}")

# for word counter
some_sentence = "please check this word ?"
c = Counter(some_sentence.split()) # split it to became a list
print(f"result :{c}")

# common usage of Counter()
# sum(c.values())                 # total of all counts
# c.clear()                       # reset all counts
# list(c)                         # list unique elements
# set(c)                          # convert to a set
# dict(c)                         # convert to a regular dictionary
# c.items()                       # convert to a list of (elem, cnt) pairs
# Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
# c.most_common()[:-n-1:-1]       # n least common elements
# c += Counter()                  # remove zero and negative counts


# Defaultdict acting as normal dictionary but with default value when keys are not set before
from collections import defaultdict
# setting mydict unsetted key with 0 as default value
my_dict = defaultdict(lambda:0)

my_dict['key_1']=100
my_dict['key_2']=500
my_dict['key_3']=50
print(f"\ndictionary value : {my_dict}")
print(f"my_dict['key_4'] : {my_dict['key_4']}")
print()

# NamedTuple() helping programerr to work with tuple
# namedTuple data accesed by using name assigned to tuple (just like class with atribute) instead list index
from collections import namedtuple

Dog = namedtuple('Dog',['age','breed','name'])
print(type(Dog)) # <class 'type'>

mydog = Dog(age=5,breed='Husky',name='sam')
print(mydog)        # Dog(age=5, breed='Husky', name='sam')
# Calling each value by name like atribute in class object
print(mydog.age)
print(mydog.breed)
print(mydog.name)

# or calling like normal tuple
print(mydog[0]) # age
print(mydog[1]) # breed
print(mydog[2]) # name

# but when tuple data is bigger or have many value it's hard to read what index hold value of somethings