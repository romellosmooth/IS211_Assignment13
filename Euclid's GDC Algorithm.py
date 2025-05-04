def gcd(a, b):
    if b == 0:
        return a  # Base case: when b is 0, a is the GCD
    else:
        return gcd(b, a % b)  # Recursive case: call gcd with (b, remainder of a/b)

# Example usage:
print(gcd(48, 18))  # Should return 6
