
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

# Assuming even_odd_count is imported from your module
# from your_module import even_odd_count

@pytest.mark.parametrize("input_val, expected", [
    # --- Standard Mixed Digits ---
    pytest.param(123, (1, 2), id="mixed_digits_small"),
    pytest.param(456, (2, 1), id="mixed_digits_small_alt"),
    pytest.param(4567, (2, 2), id="mixed_digits_medium"),
    pytest.param(1024, (3, 1), id="mixed_with_zero_internal"),
    pytest.param(1212, (2, 2), id="alternating_even_odd"),

    # --- Negative Numbers (Signs should be ignored) ---
    pytest.param(-12, (1, 1), id="negative_mixed"),
    pytest.param(-135, (0, 3), id="negative_all_odd"),
    pytest.param(-246, (3, 0), id="negative_all_even"),
    pytest.param(-864, (3, 0), id="negative_all_even_alt"),
    pytest.param(-5, (0, 1), id="negative_single_digit"),

    # --- Edge Cases: Zero and Single Digits ---
    pytest.param(0, (1, 0), id="zero_is_even"),
    pytest.param(2, (1, 0), id="single_digit_even"),
    pytest.param(7, (0, 1), id="single_digit_odd"),
    pytest.param(8, (1, 0), id="single_digit_even_alt"),
    pytest.param(10, (1, 1), id="two_digits_with_zero"),

    # --- All Even / All Odd ---
    pytest.param(2468, (4, 0), id="all_even"),
    pytest.param(802, (3, 0), id="all_even_with_zero"),
    pytest.param(222, (3, 0), id="all_even_repeated"),
    pytest.param(13579, (0, 5), id="all_odd"),
    pytest.param(91, (0, 2), id="all_odd_small"),
    pytest.param(111, (0, 3), id="all_odd_repeated"),
    pytest.param(1357, (0, 4), id="all_odd_medium"),

    # --- Large Numbers ---
    pytest.param(1000000, (7, 0), id="large_power_of_ten"),
    pytest.param(987654321, (4, 5), id="large_mixed"),
    pytest.param(9876543210, (5, 5), id="large_mixed_with_zero"),
    pytest.param(24680246802468024680, (20, 0), id="extremely_large_even"),
], ids=None) # IDs are handled within pytest.param
def test_even_odd_count_logic(input_val, expected):
    """Tests all logical combinations of even and odd digits, including edge cases."""
    assert even_odd_count(input_val) == expected

def test_even_odd_count_return_type():
    """Verifies that the function returns a tuple of exactly two integers."""
    result = even_odd_count(123)
    assert isinstance(result, tuple), "Output should be a tuple"
    assert len(result) == 2, "Output tuple should have length 2"
    assert all(isinstance(x, int) for x in result), "Tuple elements must be integers"