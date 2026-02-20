def sum_of_squares(n):
    total=0
    for i in range (1,n+1):
        total+=i**2
        return total
n=int(input("enter a number:"))
print("sum of squares from 1 to",n,"is:",sum_of_squares(n))