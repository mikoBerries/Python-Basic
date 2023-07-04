# Decorators function in python
# just work like wrapper in other language
# Decorator work used function parameter to comsume
# and manipulating behavior/control flow of original function with other func we needed


def new_decorator(origin_func):
    "new_decorator decorating origin_func abd wrapped it with 2 print syntax"

    def wrapped_func():
        print("printing a syntax BEFORE original function executed")
        origin_func()
        print("printing a syntax AFTER original function executed")


    return wrapped_func

def myfunc():
    print("my original function ")

print(">>> manual function decorator\n")
myfunc()

decoratedfunc = new_decorator(myfunc)
decoratedfunc()


# or faster decoratod usage by adding @ and decoratore function name before def some function
# so we can simple adding and removing decorator by add/removing @ 

# this_function_need_to_decoreate are decorate by @new_decorator function
@new_decorator
def this_function_need_to_decoreate():
    print("my original function")

print("\n>>> automated function decorator by using @ symbol\n")
# when calling original function
# decorator function are included too
this_function_need_to_decoreate()


# This usage is commonly usage when working with other external liblary to wrapped some function