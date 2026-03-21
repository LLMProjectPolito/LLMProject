import pytest

def test_empty_list():
    """Test that an empty list returns an empty list"""
    assert intersperse([], 4) == []

def test_single_element_list():
    """Test that a list with a single element returns the same list"""
    assert intersperse([1], 4) == [1]

def test_multiple_element_list():
    """Test that a list with multiple elements returns the correct interspersed list"""
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

def test_large_list():
    """Test that a large list returns the correct interspersed list"""
    numbers = [i for i in range(10)]
    expected = [0, 4, 1, 4, 2, 4, 3, 4, 4, 4, 5, 4, 6, 4, 7, 4, 8, 4, 9]
    assert intersperse(numbers, 4) == expected

def test_delimeter_zero():
    """Test that a delimeter of zero returns the correct interspersed list"""
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

def test_delimeter_negative():
    """Test that a delimeter of a negative number returns the correct interspersed list"""
    assert intersperse([1, 2, 3], -4) == [1, -4, 2, -4, 3]

def test_delimeter_non_integer():
    """Test that a non-integer delimeter raises a TypeError"""
    with pytest.raises(TypeError):
        intersperse([1, 2, 3], 4.5)

def test_input_not_list():
    """Test that a non-list input raises a TypeError"""
    with pytest.raises(TypeError):
        intersperse("123", 4)

def test_delimeter_not_integer():
    """Test that a non-integer delimeter raises a TypeError"""
    with pytest.raises(TypeError):
        intersperse([1, 2, 3], "4")