# while loop in python are similar to java or golang but there else down 

number = 5
# else will executed when boolean condition are not satisfied
while number>0:
    print(number)
    number-=1
else:
    print("done while loop and printed this")

# else act as normal if else since while condition not satistied at first
while number==5:
    print(number)
    number-=1
else:
    print("this is else and number are already 5")

# pass : usage for filling for indentation so python are not throwing error
# continue and break are act similar to other language