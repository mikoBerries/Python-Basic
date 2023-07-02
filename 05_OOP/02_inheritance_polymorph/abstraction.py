# abstraction class used to become base model of some type/class
# that have some blank function to inheritance class implement it with each class behavior

# With helping of Animal as abstract Dog and Cat are having a similar method to work with. 
class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name

    def speak(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

# Dog & Cat are inheritance class of Animal
class Dog(Animal):
    
    def speak(self):
        return self.name+' says Woof!'
    
class Cat(Animal):

    def speak(self):
        return self.name+' says Meow!'
    
fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak())
print(isis.speak())

# polymorp
for pet in [fido,isis]:
    print(fido.speak())