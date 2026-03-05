def interest(principal,rate,time):
    return(principal*rate*time)/100
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))
print("Simple Interest is:",interest (p, r, t))
