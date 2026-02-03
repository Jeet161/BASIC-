def lcm(a,b):
    greater=max(a,b)
    while True:
        if greater%a==0 and greater%b==0:
            return greater
        greater+=1
a=int(input("enter first number"))
b=int(input("enter second number:"))
print("lcm of","a"and "b","is",lcm(a,b))