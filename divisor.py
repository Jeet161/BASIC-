def divisors(n):
    divs=[]
    for i in range(1,n+1):
        if n%i==0:
          divs.append(i)
    return divs
num=int(input("enter a number:"))
print("Divisors of",num,"are:",divisors(num))