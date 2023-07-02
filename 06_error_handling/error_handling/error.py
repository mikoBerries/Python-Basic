# eror handling in python
# there are some build in error type
# https://docs.python.org/3/library/exceptions.html

def some_func()->None:
    "this is fucntion doc string"
    try:
        f = open('test.txt','r')
        f.write("do some write")
    except OSError:
        print("some error happend")
    finally:
        print("i always run like java try -> catch -> finally")

def other_func()->None:
    " this is fucntion doc string"
    while True:
        try:
            result =int(input("please input int or error happend : "))
            print(f"your input {result}")
        except:
            print("error when converting input")
            continue
        else:
            print("else: are executed")
            break
        # finally:
        #     print("this is finally")

some_func()
print()
other_func()
