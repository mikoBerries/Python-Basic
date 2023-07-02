#s Some class 
class sample():   
    # class object attribute
    inside_atribbute = 'this in inside class'

    # init func to create this object (constructor)
    def __init__(self,something,atribute2,atribute3) -> None:

        # Assign atribute in python to sample class/object
        self.something = something
        self.atribute2 = atribute2
        self.atribute3 = atribute3

    # method in python
    def print_all(self):
        print(self.something)
        print(self.atribute2)
        print(self.atribute3)
        print(self.inside_atribbute)

my_sample = sample(1,2,3)

print(my_sample)
# <__main__.sample object at 0x0000006F48144890>

print(my_sample.something)
# 1
print(my_sample.atribute2)
# 2
print(my_sample.atribute3)
# 3
print(my_sample.inside_atribbute)
# this in inside class


my_sample.print_all()

print(type(1))
print(type([]))
print(type(()))
print(type({}))