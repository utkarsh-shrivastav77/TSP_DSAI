def pattern(n):
    for i in range(1,n+1):
        for _ in range(n-i):
            print(" ",end=" ")
        for _ in range(i):
            print("*", end=" ")
        print()

num = int(input("Enter the lines you want in the pattern : "))
pattern(num)