n = int(input("Enter number of rows:"))
for i in range (1,n+1):
    row="  "
    for j in range (1,n+1):
        row+=(str(j)+"  ")if (i==1 or i==n or j==1 or j==n) else"   "
    print(row)