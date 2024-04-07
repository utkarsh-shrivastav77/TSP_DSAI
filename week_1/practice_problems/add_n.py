def add_n_num(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum

num = int(input("Enter the value of n : "))
number = []
for _ in range(num):
    a = int(input("Enter the number you want to add : "))
    number.append(a)
ans = add_n_num(*number)
print("The answer is : " + str(ans))
