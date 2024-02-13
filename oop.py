class Person:
    def __init__(self,firstname,age,gender):
        self.firstname=firstname
        self.age = age
        self.gender = gender
    def details(self):
        print(self.firstname,"is studying")

teacher = Person("John",26,"male")
accountant = Person("Mary",42,"female")
doctor = Person("Joe",24,"male")

print(teacher.firstname,teacher.age,teacher.gender)
print(accountant.firstname,accountant.age,accountant.gender)