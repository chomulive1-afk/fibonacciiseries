def get_fibonacci_sum(n):
    """Returns the sum of the first n Fibonacci numbers."""
    a, b = 0, 1
    total = 0

    for _ in range(n):
        total += a
        a, b = b, a + b

    return total


if __name__ == "__main__":
    n = 10
    print(f"Sum of first {n} Fibonacci numbers is: {get_fibonacci_sum(n)}")