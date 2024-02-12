# Inbuilt functions
number = max(23,18,91)
print(number)

y = min(45,23,69,85)
print(y)

z =  pow(2,3)
print(z)

# User-defined functions
def name():
    print("Betsy")

name() # Calling a function

def details():
    name = "Betsy"
    age = 18
    course = "MIT"
    print(name,age,course)
details()

# Parameters/Variables and arguments/values
def patient(name,gender,age,course,MarriageStatus):
    print(name,gender,age,course,MarriageStatus)

patient("Job","male",45,"comp sci", "single")

def multiply (x,y):
    print(x*y)
multiply(9,6)

def employees(fullname,age,position,salary):
    print(fullname,age,position,salary)

employees("john Joe",45,"CEO",45000)
employees("Sand",56, "Secretary",30000)
employees("Andy",23, "Cashier",20000)
employees("Wendy",18,"Treasurer",36000)
employees("Dan",25,"Manager",15000)