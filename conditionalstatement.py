temperature = 34

if temperature > 25 :
    print("It is hot")
else :
    print("It is cold")


# A program that determines the largest number among three numbers
num1 = 78
num2 = 90
num3 = 23
if num1 > num2 and num1 > num3 :
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3 :
    print(num2, "is the largest number")
else :
    print(num3, "is the largest number")

# A program that checks whether a number is even or odd
number = 25

if number % 2  == 0 :
    print(number, "is even")
else :
    print(number, "is odd")

# A program that checks whether a number is a prime number or not
number = 133
if number < 2:
    print(number, "is not a prime number")
elif number % 2 == 0 :
    print(number, "is not a prime number")
elif number % 3 == 0 and number != 3 :
    print(number, "is not a prime number")
elif number % 5 == 0 and number != 5 :
    print(number, "is not a prime number")
elif number % 7 == 0 and number != 7 :
    print(number,"is not a prime number")
elif number % 11 == 0 and number != 11 :
    print(number,"is not a prime number")
else :
    print(number,"is a prime number")