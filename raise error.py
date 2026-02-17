def fact(n):
    if n<0:
        raise ValueError("negative number!")
    return 1 if n in(0,1) else n*fact(n-1)
print(fact(8))
    