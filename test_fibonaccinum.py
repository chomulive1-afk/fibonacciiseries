import pytest
from fibonaccinum import get_fibonacci_sum

def test_get_fibonacci_sum():
    # Sample test value
    n = 6
    
    # Expected result
    # Fibonacci numbers: 0,1,1,2,3,5 → sum = 12
    expected_output = 12

    # Assertion
    assert get_fibonacci_sum(n) == expected_output