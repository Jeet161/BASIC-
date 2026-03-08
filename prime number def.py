def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # Exclude other even numbers

    # Check for factors from 3 to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Example usage:
num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a Prime number.")
else:
    print(f"{num} is NOT a Prime number.")