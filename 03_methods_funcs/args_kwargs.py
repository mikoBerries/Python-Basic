# args      : arguments
# kw-args   : KeyWord Arguments

# myfunc positional argument
def myfunc(a,b,c=0,d=0): 
    pass

# *args arbitary argument 
# this function accpet many args
def myfunc2(*args):
    # * args are becoming tuple
    print(args)
    print("*args becoming tuple inside function")

# ** arbitary keyword argument
def myfunc3(**kwargs):
    # **  producint  dictionary
    print(kwargs)
    print("**kwargs becoming dictionary inside function")
    # seaching fruit in kwargs dictionary
    if 'fruit' in kwargs:
        print("my fruit choice is {}".format(kwargs["fruit"]))


# combination args kwargs in function
def myfunc4(*args,**kwargs):
    print(args)
    print(kwargs)
    print("I would like {} {}".format(args[0],kwargs["food"]))

# usage
print("*args arbitary argument in function:")
myfunc2(10,20,30,40,50,60,70,80,90,100)

print("\n**kwargs arbitary keyword argument in function:")
myfunc3(fruit="apples",price=100)

print("\n*args and **kwargs arbitary argument combination in function:")
myfunc4(10,20,30,40,food="eggs")


def myfunc(*args):
    mylist=[]
    for arg in args:
        if arg%2==0:
            mylist.append(arg)
    
    return mylist

def hand_on_exercise_2(arg):
    result =''
    for i,char in  enumerate(arg):
        print("{} - {}".format(i,char))
        if i%2!=0:
            result+=char.upper()
        else:
            result+=char.lower()
            
    return result
        
print(hand_on_exercise_2("Anthropomorphism"))