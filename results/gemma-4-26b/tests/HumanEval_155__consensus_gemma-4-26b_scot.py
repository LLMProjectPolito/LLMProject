
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

@pytest.mark.parametrize("num, expected", [
    # Basic positive integers
    (123, (1, 2)),
    (246, (3, 0)),
    (135, (0, 3)),
    (222, (3, 0)),
    (111, (0, 3)),
    
    # Negative integers
    (-12, (1, 1)),
    (-4, (1, 0)),
    (-135, (0, 3)),
    (-2468, (4, 0)),
    (-468, (3, 0)),
    (-1357, (0, 4)),
    (-9876543210, (5, 5)),
    
    # Zero
    (0, (1, 0)),
    
    # Single digits
    (2, (1, 0)),
    (7, (0, 1)),
    (8, (1, 0)),
    (9, (0, 1)),
    (4, (1, 0)),
    (3, (0, 1)),
    
    # Mixed and Large numbers
    (102, (2, 1)),
    (1029384756, (5, 5)),
    (9876543210, (5, 5)),
    (999999, (0, 6)),
    (2468024680, (10, 0)),
    (1357913579, (0, 10)),
    (1234567890, (5, 5)),
    (11111, (0, 5)),
    (22222, (5, 0)),
    (999, (0, 3)),
    (888, (3, 0)),
])
def test_even_odd_count(num, expected):
    """Tests the even_odd_count function with various integer inputs."""
    assert even_odd_count(num) == expected

def test_even_odd_count_return_type():
    """Ensures the function returns a tuple of length 2."""
    result = even_odd_count(123)
    assert isinstance(result, tuple)
    assert len(result) == 2

def test_even_odd_count_element_types():
    """Ensures the elements within the tuple are integers."""
    result = even_odd_count(123)
    assert isinstance(result[0], int)
    assert isinstance(result[1], int)

def test_even_odd_count_type_error():
    """Tests that the function handles non-integer inputs appropriately."""
    with pytest.raises(TypeError):
        even_odd_count("123") # type: ignore
    with pytest.raises(TypeError):
        even_odd_count(None) # type: ignore