# Data Type

number = 67 # int
num = 78.98 # float
greeting = "Hello there" #str
IsPythonInteresting = True  #bool

# A variable storing multiple values
languages = ["Python", "PHP","Java"] # list
fruits = ("banana", "apple" "pineapple") #tuple
countries = {"Kenya", "China", "North America"} #sets
# Dictionary
details = {
    "firstname":"Brian",
    "age":17,
    "course":"MIT",
    "nationality": "Kenya"
}
print(details["nationality"])
print(details["course"])
print(number)
print (IsPythonInteresting)
print(details)

# Determining the data type
print(type(details))
print(type(countries))
print(type(languages))


# Typecasting - Converting one datatype to another
print(float(number))
print(int(num))