import pytest
import math


# Focus: Prime Number Determination
import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_x_or_y_prime():
    """Test x_or_y when n is a prime number."""
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 100, 200) == 100
    assert x_or_y(13, 5, 1) == 5
    assert x_or_y(3, -1, 0) == -1

def test_x_or_y_not_prime():
    """Test x_or_y when n is not a prime number."""
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(1, 99, 100) == 100
    assert x_or_y(6, 0, -1) == -1

def test_x_or_y_edge_cases():
    """Test x_or_y with edge cases like 0 and 1."""
    assert x_or_y(0, 10, 20) == 20
    assert x_or_y(1, 30, 40) == 40

# Focus: Value Assignment Logic
import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_x_or_y_prime():
    """Test when n is a prime number, it should return x."""
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(2, 10, 20) == 10
    assert x_or_y(13, 5, 8) == 5

def test_x_or_y_not_prime():
    """Test when n is not a prime number, it should return y."""
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(4, 1, 2) == 2
    assert x_or_y(9, 7, 9) == 9

def test_x_or_y_edge_case_one():
    """Test when n is 1, it should return y."""
    assert x_or_y(1, 10, 20) == 20

# Focus: Input Data Types
import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n < 2:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@pytest.mark.parametrize("n, x, y", [
    (7, 34, 12),
    (15, 8, 5),
    (2, "hello", 10),
    (4, 100, "world"),
    (1, 1, 2),
    (0, 5, 6),
    (-5, 7, 8),
    (3.14, 1, 2),
    ("5", 1, 2),
    (5, 1, "2")
])
def test_x_or_y_input_types(n, x, y):
    """Tests the function with various input data types."""
    if isinstance(n, float) or isinstance(n, str):
        with pytest.raises(TypeError):
            x_or_y(n, x, y)
    else:
        result = x_or_y(n, x, y)
        if isinstance(n, int) and n >= 0:
            if is_prime(n):
                assert result == x
            else:
                assert result == y
        else:
            assert result == y