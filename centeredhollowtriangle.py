# Centered Hollow Triangle Program

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    # Print leading spaces for centering
    print(" " * (n - i), end="")

    # First row
    if i == 1:
        print("*")

    # Last row (base of triangle)
    elif i == n:
        print("*" * (2 * n - 1))

    # Middle rows
    else:
        print("*" + " " * (2* i - 3) + "*")
