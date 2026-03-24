
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

import pytest
import math


# Focus: Boundary Values
import pytest

def test_boundary_zero_numerator():
    assert simplify("0/1", "1/1") == True
    assert simplify("1/1", "0/1") == True
    assert simplify("0/5", "5/1") == True

def test_boundary_one_numerator_denominator():
    assert simplify("1/1", "1/1") == True
    assert simplify("5/1", "1/1") == True
    assert simplify("1/1", "5/1") == True

def test_boundary_large_numbers():
    assert simplify("1000/1", "1/1000") == True
    assert simplify("1000/2", "1/500") == True
    assert simplify("999/1", "1/999") == True

# Focus: Equivalence Partitioning
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
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    result = (x_num * n_num) / (x_den * n_den)
    return result == int(result)

def test_equivalence_partitioning_whole_number():
    assert simplify("1/1", "1/1") == True
    assert simplify("2/1", "1/1") == True
    assert simplify("1/5", "5/1") == True
    assert simplify("4/2", "3/1") == True

def test_equivalence_partitioning_not_whole_number():
    assert simplify("1/2", "1/1") == False
    assert simplify("1/3", "1/1") == False
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/4", "2/3") == False

def test_equivalence_partitioning_edge_cases():
    assert simplify("1/1", "2/2") == True
    assert simplify("2/2", "3/3") == True
    assert simplify("5/5", "1/1") == True

# Focus: Error Handling (Invalid Input Format)
import pytest

def test_invalid_input_format_x():
    """Test with invalid format for x."""
    with pytest.raises(ValueError):
        simplify("1.5/2", "2/1")

def test_invalid_input_format_n():
    """Test with invalid format for n."""
    with pytest.raises(ValueError):
        simplify("1/2", "2.5/1")

def test_invalid_input_format_both():
    """Test with invalid format for both x and n."""
    with pytest.raises(ValueError):
        simplify("1.5/2", "2.5/1")