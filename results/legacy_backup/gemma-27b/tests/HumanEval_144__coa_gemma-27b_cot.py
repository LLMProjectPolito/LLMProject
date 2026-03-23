import pytest
import math


# Focus: Boundary Values
import pytest

def test_simplify_boundary_whole_numbers():
    assert simplify("1/1", "1/1") == True
    assert simplify("2/1", "1/1") == True
    assert simplify("1/1", "2/1") == True

def test_simplify_boundary_zero_numerator():
    assert simplify("0/1", "1/1") == True
    assert simplify("1/1", "0/1") == True
    assert simplify("0/1", "0/1") == True

def test_simplify_boundary_large_numbers():
    assert simplify("1000/1", "1/1000") == True
    assert simplify("1000/1", "2/1000") == False
    assert simplify("1/1000", "1000/1") == True

# Focus: Equivalence Partitioning
import pytest

def test_equivalence_partitioning_valid_simplification():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("1/1", "1/1") == True
    assert simplify("5/2", "2/5") == True

def test_equivalence_partitioning_invalid_simplification():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/2", "1/3") == False
    assert simplify("3/4", "1/2") == False

def test_equivalence_partitioning_edge_cases():
    assert simplify("1/1", "1/1") == True
    assert simplify("2/1", "1/2") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("10/1", "1/10") == True

# Focus: Error Handling (Invalid Input Format)
import pytest

def test_simplify_invalid_x_format():
    """Test with invalid format for x."""
    with pytest.raises(ValueError):
        simplify("1a/5", "5/1")

def test_simplify_invalid_n_format():
    """Test with invalid format for n."""
    with pytest.raises(ValueError):
        simplify("1/5", "5b/1")

def test_simplify_invalid_x_and_n_format():
    """Test with invalid format for both x and n."""
    with pytest.raises(ValueError):
        simplify("1a/5", "5b/1")