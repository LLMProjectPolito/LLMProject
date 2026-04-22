
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

# The function even_odd_count is assumed to be imported or defined in the environment.

@pytest.mark.parametrize("input_num, expected", [
    (123, (1, 2)),        # 1(O), 2(E), 3(O)
    (456, (2, 1)),        # 4(E), 5(O), 6(E)
    (1357, (0, 4)),       # All odd
    (2468, (4, 0)),       # All even
    (102, (2, 1)),        # 1(O), 0(E), 2(E)
    (444, (3, 0)),        # All even (repeated case)
])
def test_even_odd_count_positive_integers(input_num, expected):
    """Tests standard positive integers with various parity distributions."""
    assert even_odd_count(input_num) == expected

@pytest.mark.parametrize("input_num, expected", [
    (-12, (1, 1)),        # 1(O), 2(E)
    (-876, (2, 1)),       # 8(E), 7(O), 6(E)
    (-135, (0, 3)),       # All odd
    (-246, (3, 0)),       # All even
    (-10, (1, 1)),        # 1(O), 0(E)
])
def test_even_odd_count_negative_integers(input_num, expected):
    """Tests that negative signs are ignored and parity is calculated on digits."""
    assert even_odd_count(input_num) == expected

@pytest.mark.parametrize("input_num, expected", [
    (0, (1, 0)),          # Zero is even
    (2, (1, 0)),          # Single even
    (7, (0, 1)),          # Single odd
])
def test_even_odd_count_edge_cases(input_num, expected):
    """Tests edge cases: zero and single-digit inputs."""
    assert even_odd_count(input_num) == expected

@pytest.mark.parametrize("input_num, expected", [
    (1234567890, (5, 5)),               # Standard large integer
    (24680135792468013579, (10, 10)),   # Extremely large integer
])
def test_even_odd_count_large_integers(input_num, expected):
    """Tests very large integers to ensure no overflow or logic errors."""
    assert even_odd_count(input_num) == expected

def test_even_odd_count_output_contract():
    """Verifies the return type is specifically a tuple of length 2."""
    result = even_odd_count(123)
    assert isinstance(result, tuple), "Result must be a tuple"
    assert len(result) == 2, "Result tuple must have exactly 2 elements"

def test_even_odd_count_input_validation():
    """Verifies that the function raises TypeError for non-integer inputs."""
    with pytest.raises(TypeError):
        even_odd_count("123")  # type: ignore
    with pytest.raises(TypeError):
        even_odd_count(12.34)  # type: ignore