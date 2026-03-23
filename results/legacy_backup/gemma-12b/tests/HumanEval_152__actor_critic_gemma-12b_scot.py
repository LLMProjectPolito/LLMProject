import pytest
from your_module import compare  # Replace your_module

def test_empty_lists():
    assert compare([], []) == []

def test_unequal_lengths():
    with pytest.raises(ValueError):
        compare([1, 2, 3], [1, 2])

def test_all_correct_guesses():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_all_incorrect_guesses():
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_mixed_guesses():
    """
    Tests a mix of correct and incorrect guesses.
    Expected behavior: 0 for correct guesses, absolute difference for incorrect guesses.
    """
    assert compare([1, 2, 3, 4, 5], [1, 3, 3, 4, 6]) == [0, 1, 0, 0, 1]

@pytest.mark.parametrize("numbers, sign", [([5, 10, 15], 1), ([5, 10, 15], -1)])
def test_signed_numbers(numbers, sign):
    """Tests positive and negative numbers."""
    if sign == 1:
        assert compare([5, 10, 15], [5, 8, 15]) == [0, 2, 0]
    else:
        assert compare([-5, -10, -15], [-5, -8, -15]) == [0, 2, 0]

def test_zero_values():
    assert compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]

def test_mixed_positive_negative_zero():
    assert compare([0, 5, -5], [0, 3, -5]) == [0, 2, 0]

def test_duplicate_values():
    assert compare([1, 2, 2, 3], [1, 2, 2, 4]) == [0, 0, 0, 1]

def test_large_numbers():
    assert compare([1000000, 2000000], [1000000, 2000001]) == [0, 1]

def test_integer_float_comparison():
    """Tests comparison of integers and floats."""
    assert compare([1, 2.5, 3], [1, 2.5, 3.1]) == [0, 0, 0.1]

def test_different_orders():
    """
    This test highlights that the comparison is not order-independent.
    The behavior is documented as such.
    """
    assert compare([1, 2, 3], [3, 2, 1]) == [2, 0, 2]

def test_single_element_list():
    assert compare([5], [5]) == [0]

def test_none_values():
    with pytest.raises(TypeError):
        compare([1, 2, None], [1, 2, 3])

def test_string_values():
    with pytest.raises(TypeError):
        compare(["a", "b", "c"], ["a", "b", "d"])

def test_empty_vs_nonempty():
    assert compare([], [1, 2, 3]) == [1, 2, 3]
    assert compare([1, 2, 3], []) == [1, 2, 3]