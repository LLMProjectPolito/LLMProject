import pytest
import math


# Focus: Boundary Values
import pytest

def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))
    
    product = (num_x * num_n) / (den_x * den_n)
    
    return product.is_integer()

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `simplify` checks if the product of two fractions `x` and `n` is a whole number.
### Boundary values to test include:
### 1. Small numerators and denominators (e.g., "1/1", "1/2")
### 2. Large numerators and denominators (e.g., "100/1", "1/100")
### 3. Cases where the product is an integer and not an integer.
### 4. Cases where one of the fractions is a whole number.

### STEP 2: PLAN - List test functions names and scenarios.
### test_simplify_small_integers
### test_simplify_large_integers
### test_simplify_fraction_times_whole_number

### STEP 3: CODE - Write the high-quality pytest suite.
def test_simplify_small_integers():
    assert simplify("1/1", "1/1") == True
    assert simplify("1/1", "1/2") == False
    assert simplify("1/2", "1/1") == False

def test_simplify_large_integers():
    assert simplify("100/1", "1/1") == True
    assert simplify("1/100", "100/1") == True
    assert simplify("100/1", "1/100") == False

def test_simplify_fraction_times_whole_number():
    assert simplify("1/2", "2/1") == True
    assert simplify("2/3", "3/1") == True
    assert simplify("3/4", "4/1") == True
    assert simplify("1/3", "4/1") == False

# Focus: Type Scenarios
import pytest

def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))
    
    product = (num_x * num_n) / (den_x * den_n)
    
    return product.is_integer()

def test_simplify_positive_whole_numbers():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "6/1") == True
    assert simplify("10/2", "2/1") == True

def test_simplify_non_whole_numbers():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("3/4", "5/1") == False

def test_simplify_large_numbers():
    assert simplify("100/10", "10/1") == True
    assert simplify("123/45", "45/1") == True
    assert simplify("1000/100", "10/1") == True

# Focus: Logic Branches
import pytest

def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))
    
    product_num = num_x * num_n
    product_den = den_x * den_n
    
    if product_num % product_den == 0:
        return True
    else:
        return False

@pytest.mark.logic_branch_1
def test_simplify_true():
    assert simplify("1/5", "5/1") == True

@pytest.mark.logic_branch_1
def test_simplify_false_1():
    assert simplify("1/6", "2/1") == False

@pytest.mark.logic_branch_1
def test_simplify_false_2():
    assert simplify("7/10", "10/2") == False