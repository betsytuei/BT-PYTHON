num = 13
if num > 1 :
    for x in range (2,num) :
        if num % x == 0 :
            print("not a prime number")
        else :
            print("the number is prime")
            break
    else :
        print("the number is not prime")