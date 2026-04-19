
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

def test_generate_integers_standard():
    """Test standard range with multiple even digits."""
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reversed():
    """Test that the function handles reversed input order (b < a)."""
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_out_of_digit_range():
    """Test ranges where no numbers are single digits."""
    assert generate_integers(10, 14) == []
    assert generate_integers(100, 200) == []

def test_generate_integers_partial_overlap():
    """Test ranges that start/end outside the 0-9 digit range."""
    # Only 6 and 8 are even digits between 5 and 12
    assert generate_integers(5, 12) == [6, 8]
    # Only 2, 4, 6, 8 are even digits between -5 and 10
    assert generate_integers(-5, 10) == [0, 2, 4, 6, 8] if 0 is considered, else [2, 4, 6, 8]

def test_generate_integers_single_value():
    """Test when a and b are the same value."""
    assert generate_integers(4, 4) == [4]  # Even digit
    assert generate_integers(5, 5) == []   # Odd digit
    assert generate_integers(12, 12) == [] # Not a digit

def test_generate_integers_no_evens():
    """Test ranges that contain only odd digits."""
    assert generate_integers(1, 1) == []
    assert generate_integers(3, 3) == []
    assert generate_integers(1, 3) == [2] # 2 is between 1 and 3

def test_generate_integers_all_digits():
    """Test the full range of possible even digits."""
    # Assuming positive integers as per prompt, but testing boundaries
    assert generate_integers(1, 9) == [2, 4, 6, 8]

@pytest.mark.parametrize("a, b, expected", [
    (2, 4, [2, 4]),
    (4, 2, [2, 4]),
    (7, 9, [8]),
    (9, 7, [8]),
    (11, 15, []),
    (0, 2, [0, 2]), # Testing 0 as an even digit boundary
])
def test_generate_integers_parametrized(a, b, expected):
    """Comprehensive check of various boundary combinations."""
    # Note: If the implementation strictly follows "positive integers", 
    # 0 might be excluded. This test helps define that behavior.
    result = generate_integers(a, b)
    # We filter 0 out if the implementation defines positive as > 0
    if a > 0 and b > 0:
        assert result == expected
    else:
        # If 0 is passed, we check if the implementation handles it gracefully
        assert result == expected or result == [x for x in expected if x != 0]