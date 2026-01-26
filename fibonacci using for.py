def fibonacci(n):
    if n<=0:
        print ("please enter positive integer.")
    elif n ==1:
        print ("fibonacci series:")
    else:
        a,b=0,1
        print("fibonacci series:")
        print(a)
        print(b)
        for _ in range(2,n):
            c=a+b
            print(c)
            a=b
            b=c            
n=int(input("enter a number:"))
print(fibonacci(n))
