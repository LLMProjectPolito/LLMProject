
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

import pytest

@pytest.mark.parametrize("a, b, expected", [
    # Provided examples
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (10, 14, []),
    
    # Single digit cases
    (2, 2, [2]),
    (3, 3, []),
    (4, 4, [4]),
    (0, 0, [0]),
    (1, 1, []),
    
    # Ranges within single digits
    (1, 5, [2, 4]),
    (5, 1, [2, 4]),
    (3, 7, [4, 6]),
    (3, 5, [4]),
    (5, 3, [4]),
    (5, 7, [6]),
    (7, 9, [8]),
    (9, 7, [8]),
    (1, 9, [2, 4, 6, 8]),
    (9, 1, [2, 4, 6, 8]),
    
    # Boundary cases with 10
    (1, 10, [2, 4, 6, 8]),
    (10, 1, [2, 4, 6, 8]),
    (7, 11, [8]),
    (8, 10, [8]),
    (9, 11, []),
    (11, 9, []),
    
    # Large number ranges (no single-digit even numbers in range)
    (100, 200, []),
    (1, 1000, [2, 4, 6, 8]),
    (1000, 1, [2, 4, 6, 8]),
    (11, 19, []),
    (11, 13, []),
    (13, 15, []),
    (15, 17, []),
])
def test_generate_integers(a, b, expected):
    """
    Tests the generate_integers function with various scenarios including
    ascending/descending ranges, single digits, non-digit ranges, and boundaries.
    """
    assert generate_integers(a, b) == expected

def test_generate_integers_type_error():
    """
    Check if the function handles non-integer inputs.
    """
    with pytest.raises(TypeError):
        generate_integers("2", 8) # type: ignore

def test_generate_integers_type_consistency():
    """
    Ensures the return type is always a list.
    """
    assert isinstance(generate_integers(2, 8), list)
    assert isinstance(generate_integers(10, 14), list)

def test_generate_integers_order():
    """
    Ensures the output is always in ascending order and consistent regardless of input order.
    """
    result_asc = generate_integers(2, 8)
    result_desc = generate_integers(8, 2)
    assert result_asc == sorted(result_asc)
    assert result_desc == sorted(result_desc)
    assert result_asc == result_desc