
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """

import pytest

# The function int_to_mini_roman is assumed to be defined in the environment.

@pytest.mark.parametrize("number, expected", [
    (1, 'i'),
    (2, 'ii'),
    (3, 'iii'),
    (5, 'v'),
    (10, 'x'),
    (50, 'l'),
    (100, 'c'),
    (500, 'd'),
])
def test_basic_values(number, expected):
    """Test simple additive Roman numerals."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (4, 'iv'),
    (9, 'ix'),
    (40, 'xl'),
    (90, 'xc'),
    (400, 'cd'),
    (900, 'cm'),
])
def test_subtractive_cases(number, expected):
    """Test the subtractive notation rules (4s and 9s)."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (19, 'xix'),
    (152, 'clii'),
    (426, 'cdxxvi'),
])
def test_provided_examples(number, expected):
    """Verify the examples provided in the problem description."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (1, 'i'),
    (1000, 'm'),
])
def test_boundary_values(number, expected):
    """Test the lower and upper bounds of the constraints (1 <= num <= 1000)."""
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize("number, expected", [
    (399, 'cccxcix'),
    (444, 'cdxliv'),
    (888, 'dlxxxviii'),
    (999, 'cmxcix'),
])
def test_complex_combinations(number, expected):
    """Test numbers that require a mix of additive and subtractive logic."""
    assert int_to_mini_roman(number) == expected

def test_output_is_lowercase():
    """Ensure that the output is always lowercase regardless of the number."""
    # Test a variety of numbers and check if any uppercase characters exist
    for i in [1, 4, 9, 49, 99, 400, 900, 1000]:
        result = int_to_mini_roman(i)
        assert result == result.lower(), f"Output for {i} contains uppercase letters: {result}"
        assert not any(char.isupper() for char in result), f"Output for {i} contains uppercase letters: {result}"

@pytest.mark.parametrize("invalid_input", [0, 1001, -1])
def test_out_of_bounds_behavior(invalid_input):
    """
    While the constraint is 1 <= num <= 1000, a robust function should 
    either handle these gracefully or we should document the behavior.
    This test checks that the function doesn't crash, or we can assert 
    specific error handling if the implementation defines it.
    """
    try:
        int_to_mini_roman(invalid_input)
    except Exception as e:
        # If the function is designed to raise an error for out-of-bounds, 
        # this is acceptable. If it's not, we just ensure it doesn't crash 
        # unexpectedly with a SegFault or similar.
        pass