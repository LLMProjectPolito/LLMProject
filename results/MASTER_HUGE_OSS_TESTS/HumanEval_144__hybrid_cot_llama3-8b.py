import pytest

@pytest.mark.parametrize("x, n, expected", [
    ("1/5", "5/1", True),
    ("1/6", "2/1", False),
    ("7/10", "10/2", False),
    ("0/5", "5/1", False),
    ("5/0", "5/1", False),
    ("1/2", "1/2", True),
    ("1/100000", "100000/1", True),
    ("100000/1", "1/100000", True),
    # Test cases where the input fractions are not strings
    (1, 2, False),
    ("a/b", "5/1", False),
    # Test cases where the input fractions are not in the format "numerator/denominator"
    ("1.5/2", "5/1", False),
    ("1/2.5", "5/1", False),
    # Test cases where the numerator or denominator is a very large number
    ("1000000000/1000000000", "1000000000/1000000000", True),
    ("1000000000/1000000001", "1000000000/1000000001", False),
])

def test_simplify(x, n, expected):
    """Test the simplify function."""
    # Parse the input fractions
    x_num, x_den = parse_fraction(x)
    n_num, n_den = parse_fraction(n)

    # Calculate the result of x * n
    result_num = x_num * n_num
    result_den = x_den * n_den

    # Check if the result is a whole number
    is_whole_number = result_den == 1 or result_num % result_den == 0

    # Assert the expected outcome
    assert simplify(x, n) == expected
    assert is_whole_number == expected

@pytest.mark.parametrize("x, n, expected", [
    ("1/5", "5/1", True),
    ("1/6", "2/1", False),
    ("7/10", "10/2", False),
    ("0/5", "5/1", False),
    ("5/0", "5/1", False),
    ("1/2", "1/2", True),
    ("1/100000", "100000/1", True),
    ("100000/1", "1/100000", True),
    # Test cases where the input fractions are not strings
    (1, 2, False),
    ("a/b", "5/1", False),
    # Test cases where the input fractions are not in the format "numerator/denominator"
    ("1.5/2", "5/1", False),
    ("1/2.5", "5/1", False),
    # Test cases where the numerator or denominator is a very large number
    ("1000000000/1000000000", "1000000000/1000000000", True),
    ("1000000000/1000000001", "1000000000/1000000001", False),
])

def test_simplify_valid_fractions(x, n, expected):
    assert simplify(x, n) == expected

@pytest.mark.parametrize("x, n, expected", [
    ("1/6", "2/1", False),
    ("7/10", "10/2", False),
    ("1/10", "1/10", False),
    ("0/5", "5/1", False),
    ("5/0", "5/1", False),
    # Test cases where the input fractions are not strings
    (1, 2, False),
    ("a/b", "5/1", False),
    # Test cases where the input fractions are not in the format "numerator/denominator"
    ("1.5/2", "5/1", False),
    ("1/2.5", "5/1", False),
    # Test cases where the numerator or denominator is a very large number
    ("1000000000/1000000001", "1000000000/1000000001", False),
])

def test_simplify_invalid_fractions(x, n, expected):
    assert not simplify(x, n) == expected

@pytest.mark.parametrize("x, n, expected", [
    ("0/5", "5/1", False),
    ("5/0", "5/1", False),
    # Test cases where the input fractions are not strings
    (1, 2, False),
    ("a/b", "5/1", False),
    # Test cases where the input fractions are not in the format "numerator/denominator"
    ("1.5/2", "5/1", False),
    ("1/2.5", "5/1", False),
    # Test cases where the numerator or denominator is a very large number
    ("1000000000/1000000001", "1000000000/1000000001", False),
])

def test_simplify_zero_numerator(x, n, expected):
    assert not simplify(x, n) == expected

@pytest.mark.parametrize("x, n, expected", [
    ("1/0", "5/1", False),
    ("7/0", "10/2", False),
    # Test cases where the input fractions are not strings
    (1, 2, False),
    ("a/b", "5/1", False),
    # Test cases where the input fractions are not in the format "numerator/denominator"
    ("1.5/2", "5/1", False),
    ("1/2.5", "5/1", False),
    # Test cases where the numerator or denominator is a very large number
    ("1000000000/1000000001", "1000000000/1000000001", False),
])

def test_simplify_zero_denominator(x, n, expected):
    assert not simplify(x, n) == expected

@pytest.mark.parametrize("x, n, expected", [
    ("-1/5", "5/1", False),
    # Test cases where the input fractions are not strings
    (1, 2, False),
    ("a/b", "5/1", False),
    # Test cases where the input fractions are not in the format "numerator/denominator"
    ("1.5/2", "5/1", False),
    ("1/2.5", "5/1", False),
    # Test cases where the numerator or denominator is a very large number
    ("1000000000/1000000001", "1000000000/1000000001", False),
])

def test_simplify_negative_numerator(x, n, expected):
    assert not simplify(x, n) == expected

@pytest.mark.parametrize("x, n, expected", [
    ("1/-5", "5/1", False),
    # Test cases where the input fractions are not strings
    (1, 2, False),
    ("a/b", "5/1", False),
    # Test cases where the input fractions are not in the format "numerator/denominator"
    ("1.5/2", "5/1", False),
    ("1/2.5", "5/1", False),
    # Test cases where the numerator or denominator is a very large number
    ("1000000000/1000000001", "1000000000/1000000001", False),
])

def test_simplify_negative_denominator(x, n, expected):
    assert not simplify(x, n) == expected

@pytest.mark.parametrize("x, n, expected", [
    ("", "5/1", False),
    ("1/5", "", False),
    # Test cases where the input fractions are not strings
    (1, 2, False),
    ("a/b", "5/1", False),
    # Test cases where the input fractions are not in the format "numerator/denominator"
    ("1.5/2", "5/1", False),
    ("1/2.5", "5/1", False),
    # Test cases where the numerator or denominator is a very large number
    ("1000000000/1000000001", "1000000000/1000000001", False),
])

def test_simplify_empty_strings(x, n, expected):
    with pytest.raises(ValueError):
        simplify(x, n)

@pytest.mark.parametrize("x, n, expected", [
    ("1/5a", "5/1", False),
    ("1/5", "5/1a", False),
    # Test cases where the input fractions are not strings
    (1, 2, False),
    ("a/b", "5/1", False),
    # Test cases where the input fractions are not in the format "numerator/denominator"
    ("1.5/2", "5/1", False),
    ("1/2.5", "5/1", False),
    # Test cases where the numerator or denominator is a very large number
    ("1000000000/1000000001", "1000000000/1000000001", False),
])

def test_simplify_malformed_strings(x, n, expected):
    with pytest.raises(ValueError):
        simplify(x, n)