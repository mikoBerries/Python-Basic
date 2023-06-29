# List comprehension
# In addition to sequence operations and list methods, Python includes a more advanced operation called a list comprehension.

# Grab every letter in string
lst = [x for x in 'word']
print(lst)

# Square numbers in range and turn into list
lst = [x**2 for x in range(0,11)]
print(lst)

# some if statement 
# Check for even numbers in a range
lst = [x for x in range(11) if x % 2 == 0]
print(lst)

# some arithmetic operator
# Convert Celsius to Fahrenheit
celsius = [0,10,20.1,34.5]

fahrenheit = [((9/5)*temp + 32) for temp in celsius ]
print(fahrenheit)

# The idea is the first variable inside list [temp] are inputed in list
# and temp difeined by forfrom right statement and so on


# x appended by if else and value from for range
result = [x if x%2==0 else "ODD" for  x in range(0,11)]
print(result)


# nested loop 
mylist=[]

# normal way
for x in [2,4,6]:
    for y in [100,200,400]:
        mylist.append(x*y)

print(mylist)

# List comprehension way not a best practice since hard to read
mylist= [x*y for x in[2,4,6] for y in[100,200,400]]