import pytest

def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    if n <= 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        result *= factorial
    return result

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def test_special_factorial_1():
    assert special_factorial(1) == 1

def test_special_factorial_2():
    assert special_factorial(2) == 2

def test_special_factorial_3():
    assert special_factorial(3) == 12

def test_special_factorial_4():
    assert special_factorial(4) == 288

def test_special_factorial_5():
    assert special_factorial(5) == 34560

def test_special_factorial_6():
    assert special_factorial(6) == 24883200

def test_special_factorial_0():
    assert special_factorial(0) == 1

def test_special_factorial_large():
    assert special_factorial(7) == 185794560000

def test_special_factorial_edge_case():
    assert special_factorial(10) == 1316818944000000000

def test_special_factorial_performance():
    # Check performance for a moderate input
    import time
    start_time = time.time()
    special_factorial(8)
    end_time = time.time()
    assert end_time - start_time < 0.1  # Adjust threshold as needed