# Polymorphism refers to the way in which different object classes can share the same method name,
#  and those methods can be called from the same place even though a variety of different objects might be passed in.

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Woof!'
    
class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Meow!' 
    
niko = Dog('Niko')
felix = Cat('Felix')

print(niko.speak())
print(felix.speak())

# There a few different ways to demonstrate polymorphism. First, with a for loop:
# since list are binded by type

for pet in [niko,felix]:
    print(pet.speak())

# Another is with functions:
# and argument in function are any/interface{}/T
def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)