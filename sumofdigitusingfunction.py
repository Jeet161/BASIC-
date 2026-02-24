def sum_of_digit(temp):
    sum_digit=0
    while temp>0:
        sum=temp%10
        sum_digit += sum
        temp//=10
    return sum_digit   

num=int(input("enter a number:"))
result = sum_of_digit(num)
print(f"The sum of digits of {num} is: {result}")
