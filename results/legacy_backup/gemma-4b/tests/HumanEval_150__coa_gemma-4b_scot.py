import pytest
import math


# Focus: Boundary Values
import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if (n % i) == 0:
                return y
        return x
    else:
        return y

@pytest.mark.boundary
def test_x_or_y_prime_small():
    assert x_or_y(7, 34, 12) == 34

@pytest.mark.boundary
def test_x_or_y_prime_large():
    assert x_or_y(11, 34, 12) == 34

@pytest.mark.boundary
def test_x_or_y_not_prime_small():
    assert x_or_y(15, 8, 5) == 5

@pytest.mark.boundary
def test_x_or_y_not_prime_large():
    assert x_or_y(20, 8, 5) == 5

# Focus: Type Scenarios
import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if (n % i) == 0:
                return y
        return x
    else:
        return y

@pytest.mark.type_scenario("prime_x")
def test_x_prime():
    assert x_or_y(7, 34, 12) == 34

@pytest.mark.type_scenario("non_prime_y")
def test_non_prime_y():
    assert x_or_y(15, 8, 5) == 5

@pytest.mark.type_scenario("non_prime_x")
def test_non_prime_x():
    assert x_or_y(9, 34, 12) == 12

# Focus: Logic Branches
import pytest

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if (n % i) == 0:
                return y
        return x
    else:
        return y

@pytest.mark.logic_branch
def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34

@pytest.mark.logic_branch
def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5

@pytest.mark.logic_branch
def test_x_or_y_edge_case_1():
    assert x_or_y(1, 34, 12) == 12

@pytest.mark.logic_branch
def test_x_or_y_edge_case_2():
    assert x_or_y(2, 34, 12) == 34