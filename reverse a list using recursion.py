def reverse_list(lst):
    if len(lst)==0:
        return[]
    return[lst[-1]]+reverse_list(lst[:-1])
lst=input("enter elements separated by space:").split()
print("reversed list:",reverse_list(lst))


num=int(input("enter number"))
rev=0
temp=num
while temp>0:
    rev=rev*10+temp%10
    temp//=10
print("reverse of", num,"is",rev)