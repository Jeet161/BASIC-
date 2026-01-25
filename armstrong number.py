def armstrong(num):
    n=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**n
        temp//=10
    return sum==num

num=int(input("enter a number:"))
if armstrong(num):
        print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
