import pytest

def test_empty_list():
    """Test with an empty list"""
    assert specialFilter([]) == 0

def test_single_element_list():
    """Test with a single-element list"""
    assert specialFilter([15]) == 1

def test_numbers_less_than_10():
    """Test with a list containing numbers less than 10"""
    assert specialFilter([5, 2, 7, 3]) == 0

def test_numbers_greater_than_10_but_odd_first_and_last_digits():
    """Test with a list containing numbers greater than 10 but not having odd first and last digits"""
    assert specialFilter([14, 22, 36]) == 0

def test_numbers_greater_than_10_and_odd_first_and_last_digits():
    """Test with a list containing numbers greater than 10 and having odd first and last digits"""
    assert specialFilter([15, -73, 109]) == 2

def test_mixed_list():
    """Test with a list containing a mix of numbers that meet and don't meet the conditions"""
    assert specialFilter([15, -73, 14, 1]) == 2

def test_negative_numbers():
    """Test with a list containing negative numbers"""
    assert specialFilter([-15, -33, 55, -77, 99]) == 1

def test_negative_number():
    """Test with a negative number"""
    assert specialFilter([15, -73, -109]) == 2

def test_zero():
    """Test with zero"""
    assert specialFilter([15, 0, 109]) == 2

def test_numbers_with_digits_larger_than_9():
    """Test with numbers having digits larger than 9"""
    assert specialFilter([15, 117, 109]) == 2

def test_large_numbers():
    """Test with large numbers"""
    assert specialFilter([151, 117, 109]) == 2

def test_float_number():
    """Test with a float number"""
    assert specialFilter([15, 12.5, 109]) == 2

def test_non_numeric_input():
    """Test with non-numeric input (will raise ValueError)"""
    with pytest.raises(ValueError):
        specialFilter([15, 'a', 109])