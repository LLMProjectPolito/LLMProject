
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

```python
import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n <= 1:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

class TestXORY:

    def test_prime_number_returns_x(0):
        assert x_or_y(7, 34, 12) == 34

    def test_non_prime_number_returns_y(1):
        assert x_or_y(15, 8, 5) == 5

    def test_prime_number_returns_x(2):
        assert x_or_y(2, 10, 20) == 10

    def test_non_prime_number_returns_y(2):
        assert x_or_y(4, 10, 20) == 20
    
    def test_prime_number_returns_x(3):
        assert x_or_y(3, 10, 20) == 10

    def test_non_prime_number_returns_y(3):
        assert x_or_y(6, 10, 20) == 20

    def test_large_prime_number_returns_x(4):
        assert x_or_y(101, 10, 20) == 10

    def test_large_non_prime_number_returns_y(4):
        assert x_or_y(100, 10, 20) == 20

    def test_edge_case_1_returns_y(5):
        assert x_or_y(1, 10, 20) == 20

    def test_edge_case_1_returns_y(6):
        assert x_or_y(6, 10, 20) == 20
    
    def test_prime_number_returns_x(6):
        assert x_or_y(11, 10, 20) == 10

    def test_non_prime_number_returns_y(6):
        assert x_or_y(12, 10, 20) == 20

    def test_another_prime_number_returns_x(7):
        assert x_or_y(13, 10, 20) == 10

    def test_another_non_prime_number_returns_y(7):
        assert x_or_y(14, 10, 20) == 20
    
    def test_another_prime_number_returns_x(8):
        assert x_or_y(17, 10, 20) == 10
    
    def test_another_non_prime_number_returns_y(8):
        assert x_or_y(16, 10, 20) == 20
    
    def test_another_prime_number_returns_x(9):
        assert x_or_y(19, 10, 20) == 10

    def test_another_non_prime_number_returns_y(9):
        assert x_or_y(21, 10, 20) == 20

    def test_another_prime_number_returns_x(10):
        assert x_or_y(23, 10, 20) == 10

    def test_another_non_prime_number_returns_y(10):
        assert x_or_y(25, 10, 20) == 20

    def test_another_prime_number_returns_x(11):
        assert x_or_y(29, 10, 20) == 10

    def test_another_non_prime_number_returns_y(11):
        assert x_or_y(30, 10, 20) == 20

    def test_another_prime_number_returns_x(12):
        assert x_or_y(31, 10, 20) == 10

    def test_another_non_prime_number_returns_y(12):
        assert x_or_y(33, 10, 20) == 20

    def test_another_prime_number_returns_x(13):
        assert x_or_y(37, 10, 20) == 10

    def test_another_non_prime_number_returns_y(13):
        assert x_or_y(38, 10, 20) == 20

    def test_another_prime_number_returns_x(14):
        assert x_or_y(41, 10, 20) == 10

    def test_another_non_prime_number_returns_y(14):
        assert x_or_y(42, 10, 20) == 20

    def test_another_prime_number_returns_x(15):
        assert x_or_y(43, 10, 20) == 10

    def test_another_non_prime_number_returns_y(15):
        assert x_or_y(44, 10, 20) == 20

    def test_another_prime_number_returns_x(16):
        assert x_or_y(47, 10, 20) == 10

    def test_another_non_prime_number_returns_y(16):
        assert x_or_y(48, 10, 20) == 20

    def test_another_prime_number_returns_x(17):
        assert x_or_y(53, 10, 20) == 10

    def test_another_non_prime_number_returns_y(17):
        assert x_or_y(54, 10, 20) == 20

    def test_another_prime_number_returns_x(18):
        assert x_or_y(59, 10, 20) == 10

    def test_another_non_prime_number_returns_y(18):
        assert x_or_y(60, 10, 20) == 20

    def test_another_prime_number_returns_x(19):
        assert x_or_y(61, 10, 20) == 10

    def test_another_non_prime_number_returns_y(19):
        assert x_or_y(62, 10, 20) == 20

    def test_another_prime_number_returns_x(20):
        assert x_or_y(67, 10, 20) == 10

    def test_another_non_prime_number_returns_y(20):
        assert x_or_y(68, 10, 20) == 20

    def test_another_prime_number_returns_x(21):
        assert x_or_y(71, 10, 20) == 10

    def test_another_non_prime_number_returns_y(21):
        assert x_or_y(72, 10, 20) == 20

    def test_another_prime_number_returns_x(22):
        assert x_or_y(73, 10, 20) == 10

    def test_another_non_prime_number_returns_y(22):
        assert x_or_y(74, 10, 20) == 20

    def test_another_prime_number_returns_x(23):
        assert x_or_y(79,