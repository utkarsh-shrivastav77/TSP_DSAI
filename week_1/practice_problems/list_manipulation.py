def my_func(numbers):
    # remove all the odd numbers and double remaining numbers
    modified_num = map(lambda x: x*2, filter(lambda x: x%2==0 , numbers))

    #sum of all the modified numbers
    ans = sum(modified_num)
    return ans

result = []
n = int(input("Enter the number of the elements : "))
for i in range(n):
    num = int(input("Enter the number : "))
    result.append(num)
print(my_func(result))