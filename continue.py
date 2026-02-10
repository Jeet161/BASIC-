n=int(input("enter a number:"))
for i in range(1,n+1):
    if i%3==0:
        continue
    print(i,end="")