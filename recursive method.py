def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


n = int(input("Enter a number: "))
print("Factorial using Recursive Method:", factorial_recursive(n))