# inheritance helping programmer to re use code/method 
# that do commong things in some other class
class Animal():

    def __init__(self) -> None:
        print("animal created")

    def who_am_i(self):
        print("I am an animal")
    
    def eat(self):
        print("I am Eating")



# derrive class (inheritance)
class Dog(Animal):
    # Similar in java
    def __init__(self) -> None:
        super().__init__()
        print("Dog Created")

    def bark(self)->None:
        print("woof")

my_animal= Dog()

my_animal.bark()

# special magic/dunder methond
# all starting with double _
# example :
# __init__
# __str__


#