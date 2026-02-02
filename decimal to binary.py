def decimal_to_binary(n):
    if n>1:
        decimal_to_binary(n//2)
    print(n%2,end='')

num=int(input("Enter a decimal number:"))
print("Binary equivalent:",end="")
decimal_to_binary(num)
print()
