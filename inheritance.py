# Parent class/Super class/Base class

class Animal:
    def sound(self):
        print("Animal is speaking")

# Child class / Sub class /Derived class
class Dog(Animal):
    def sound(self):
        print("Dog is barking")

class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

a = Animal()
d = Dog()
c = Cat()