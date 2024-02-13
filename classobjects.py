# A class is a blueprint of an object
# An object is an instance of a class

class Person:
  #Properties/Attributes/Variables
    name = "Joe"
    age = 24
  #Method/Function/Behaviour

    def talk(self):
        print("Person is talking")

teacher = Person()
print(teacher.name)
print(teacher.age)

teacher.talk()
