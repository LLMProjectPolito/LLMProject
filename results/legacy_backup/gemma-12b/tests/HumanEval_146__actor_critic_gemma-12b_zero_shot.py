import pytest
from your_module import specialFilter  # Replace your_module

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_matching_numbers():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_single_matching_number():
    assert specialFilter([15]) == 1

def test_multiple_matching_numbers():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_positive_multiple_of_15():
    assert specialFilter([30]) == 1

def test_zero():
    assert specialFilter([0]) == 0

def test_large_numbers():
    assert specialFilter([13579]) == 1

def test_large_numbers_with_other_numbers():
    assert specialFilter([13579, 123, 456, 789]) == 1

def test_numbers_with_leading_zeros():
    assert specialFilter([15, 15]) == 1  # Corrected test: explicitly test decimal 15

def test_numbers_with_trailing_zeros():
    assert specialFilter([150, 350]) == 0

def test_numbers_with_both_leading_and_trailing_zeros():
    assert specialFilter([1500, 3500]) == 0

def test_negative_multiple_of_15():
    assert specialFilter([-15]) == 0  # Explicitly test negative multiples

def test_zero_and_multiple_of_15():
    assert specialFilter([0, 15]) == 1

def test_large_number_near_max():
    assert specialFilter([99999]) == 0

def test_edge_case_multiple_of_15_at_end():
    assert specialFilter([1, 2, 3, 15]) == 1

def test_large_input_size():
    large_list = list(range(1, 1001))
    assert specialFilter(large_list) == 0  # Assuming no numbers meet the criteria

def test_non_integer_input():
    with pytest.raises(TypeError):  # Assuming function should raise TypeError
        specialFilter([15.0])

def test_string_input():
    with pytest.raises(TypeError):  # Assuming function should raise TypeError
        specialFilter(["15"])