def fibonacci(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    elif n == 1:
        return 0  # Usually, Fibonacci starts with 0 as F(1)
    elif n == 2:
        return 1  # F(2) is 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
print(fibonacci(10))  # Should print the 10th Fibonacci number
