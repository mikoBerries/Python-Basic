# for loppings in python    

my_list = [1,2,3]
# similar like golang forr range
for list_item in my_list:
    print(list_item)

total_number = 0

number_list = [1,2,3,4,5,6,7,8,9]
for number in number_list:
    if number %2 ==0:
        print(f"this is are odd number : {number}")
    else:
        print(number)
    # total_number= total_number+number
    total_number += number


print(total_number)

mystring="This is String 12345"

for char in mystring:
    print(char)

for char in "This is another String":
    print(char)

# _ similar like golang is we nod neded
for _ in "This is another String":
    print("somthing")

# tuple on packing
list_tuple = [(1,2),(3,4),(5,6),(7,8)]
for a,b in list_tuple:
    print(a)

# iterate looping in dictionary
d = {"key1":1,"key2":2,"key3":3}

# basic iterated dictionary are just getting a key
for item in d:
    print(item)

# tuple in packing
for key,value in  d.items():
    print(f"{key} and {value}")

# d.items getting a items in dictionary (key and value)
for item in d.items():
    print(item)

# d.values() for value only
for value in d.values():
    print(value)

