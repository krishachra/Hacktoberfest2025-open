def factorial(n):
    """
    Returns the factorial of a non-negative integer n.
    """
    if n < 0:
        return "Invalid input"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# User input
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")

# Test cases
assert factorial(0) == 1
assert factorial(5) == 120
assert factorial(3) == 6
