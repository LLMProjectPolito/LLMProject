
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

# The function is assumed to be available in the namespace.
# Since I am not allowed to redefine it, I will write the tests 
# assuming 'even_odd_count' is imported or defined above.

@pytest.mark.parametrize("input_num, expected", [
    (123, (1, 2)),      # 1 (O), 2 (E), 3 (O)
    (456, (2, 1)),      # 4 (E), 5 (O), 6 (E)
    (1357, (0, 4)),     # All odd
    (2468, (4, 0)),     # All even
    (102, (2, 1)),      # 1 (O), 0 (E), 2 (E)
    (9, (0, 1)),        # Single odd
    (8, (1, 0)),        # Single even
    (0, (1, 0)),        # Zero case
])
def test_even_odd_count_standard_and_edge_cases(input_num, expected):
    """Tests standard positive integers, single digits, and the zero case."""
    assert even_odd_count(input_num) == expected

@pytest.mark.parametrize("input_num, expected", [
    (-12, (1, 1)),      # 1 (O), 2 (E)
    (-444, (3, 0)),     # 4, 4, 4 (All E)
    (-135, (0, 3)),     # 1, 3, 5 (All O)
    (-10, (1, 1)),      # 1 (O), 0 (E)
])
def test_even_odd_count_negative_numbers(input_num, expected):
    """Tests that negative signs are ignored and digits are counted correctly."""
    assert even_odd_count(input_num) == expected

def test_even_odd_count_large_integers():
    """Tests very large integers to ensure robustness."""
    # 10 digits: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
    # Evens: 2, 4, 6, 8, 0 (5)
    # Odds: 1, 3, 5, 7, 9 (5)
    large_num = 1234567890
    assert even_odd_count(large_num) == (5, 5)
    
    # Another large number: 22222222221111111111
    large_num_2 = 22222222221111111111
    assert even_odd_count(large_num_2) == (10, 10)

def test_even_odd_count_return_type():
    """Ensures the return type is strictly a tuple."""
    result = even_odd_count(123)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], int)
    assert isinstance(result[1], int)

def test_even_odd_count_all_zeros():
    """Tests a number composed of multiple zeros."""
    assert even_odd_count(000) == (1, 0) # Note: 000 is just 0 in Python
    assert even_odd_count(0) == (1, 0)