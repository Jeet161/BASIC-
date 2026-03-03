a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a>b and a>c:
    print("largest is",a)
elif b>c:
    print("largest is",b)
else:
    print("largest is",c)