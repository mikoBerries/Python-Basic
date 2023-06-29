# all about string
print("Hello World")

mystring="0123456789"
print(mystring[-1])
print(mystring[3:])
print(mystring[:5])
# iterator in string jumsp 2 char
print(mystring[::2])
# reverse string
print(mystring[::-1])

mutiplerLetter = "z"
print(mutiplerLetter*10)

#Format print
print("this is {2} {3} {1} {0} {0} {0}".format("fox","fox","brown","quick"))
# with keyword
print("this is {b} {q} {q} {q} {f2} {f}".format(f="fox",f2="Fox",b="brown",q="quick"))
# with float prcision
print("this is float {my_float}".format(my_float=0.12345678))
print("this is float+with precision: {my_float:.2f}".format(my_float=0.12345678))

# python 3+ format-string(f-string)
name="jon"
number=100

print(f"hello {name} your number is {number}")