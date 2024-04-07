def fact(num):
    if num==0:
        return 1
    return num * fact(num-1)

n = int(input("Enter the number you want factorial for : "))
print("The factorial of " + str(n) + " is " + str(fact(n)))