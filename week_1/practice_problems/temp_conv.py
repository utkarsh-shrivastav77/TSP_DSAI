def temp_conv(tmp, units):
    if units=="F":
        num = ((tmp*9)/5)+32
    else:
        num = ((tmp-32)*5)/9
    return num

conv = input("Enter which conversion F:Fahrenheit & C:Celsiusn ")
tmp = int(input("Enter the value of temperature "))

print("The conversion is " + str(temp_conv(tmp,conv)))