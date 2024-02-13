class Shape:
    def draw(self):
        print("Drawing Shape")

class Square:
    def draw(self):
        print("Drawing a square")

class Rectangle:
    def draw(self):
        print("Drawing a rectangle")

sh = Shape()
sh.draw()
sq = Square()
sq.draw()
rc = Rectangle()
rc.draw()

# Encapsulation
class Employee:
    # constructor
    def __init__(self, name, salary, project):
        # data members
        self.name = name
        self.salary = salary
        self.project = project

    # method
    # to display employee's details
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)

    # method
    def work(self):
        print(self.name, 'is working on', self.project)

# creating object of a class
emp = Employee('Jessa', 8000, 'NLP')

# calling public method of the class
emp.show()
emp.work()