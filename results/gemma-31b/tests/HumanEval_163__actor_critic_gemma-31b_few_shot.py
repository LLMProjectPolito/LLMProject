
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

def test_generate_integers_basic():
    """Test standard ranges within the single-digit range."""
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(1, 5) == [2, 4]

def test_generate_integers_reversed():
    """Test that the order of a and b does not affect the result."""
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(5, 1) == [2, 4]

def test_generate_integers_out_of_bounds():
    """Test ranges that consist entirely of numbers greater than 9."""
    assert generate_integers(10, 14) == []
    assert generate_integers(100, 200) == []

def test_generate_integers_partial_overlap():
    """Test ranges where only some numbers are single digits."""
    # Only 2, 4, 6, 8 are even digits; 10, 12 are even numbers but not digits
    assert generate_integers(4, 12) == [4, 6, 8]
    assert generate_integers(15, 6) == [6, 8]

def test_generate_integers_single_value():
    """Test ranges where a equals b, covering both even and odd cases."""
    assert generate_integers(2, 2) == [2]
    assert generate_integers(3, 3) == []

def test_generate_integers_no_evens():
    """Test ranges that contain no even digits."""
    # Range between two odd numbers with no even digit in between
    assert generate_integers(11, 13) == []

def test_generate_integers_full_digit_range():
    """Test the maximum possible range of even digits."""
    assert generate_integers(1, 9) == [2, 4, 6, 8]

def test_generate_integers_zero_and_negatives():
    """Test handling of zero and negative integers."""
    # Zero is an even single-digit integer
    assert generate_integers(0, 2) == [0, 2]
    # Negative inputs should not result in negative even digits
    assert generate_integers(-4, 2) == [0, 2]
    assert generate_integers(-10, -2) == []