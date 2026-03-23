import pytest

def test_empty_list():
    assert double_the_difference([]) == 0

def test_all_negative():
    assert double_the_difference([-1, -3, -5]) == 0

def test_mixed_positive_negative():
    assert double_the_difference([-1, 1, -2, 3]) == 10

def test_all_even():
    assert double_the_difference([2, 4, 6]) == 0

def test_all_odd():
    assert double_the_difference([1, 3, 5]) == 35

def test_zero_in_list():
    assert double_the_difference([0, 1, 2, 3]) == 10

def test_floats_in_list():
    assert double_the_difference([1.0, 2.5, 3.0]) == 10

def test_mixed_types():
    assert double_the_difference([1, "a", 3, 2.5, -1]) == 10

def test_large_numbers():
    assert double_the_difference([99, 101]) == 20002

def test_single_odd():
    assert double_the_difference([1]) == 1

def test_single_even():
    assert double_the_difference([2]) == 0

def test_single_negative():
    assert double_the_difference([-1]) == 0

def test_example_1():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_example_2():
    assert double_the_difference([-1, -2, 0]) == 0

def test_example_3():
    assert double_the_difference([9, -2]) == 81

def test_example_4():
    assert double_the_difference([0]) == 0

def test_mixed_odd_even():
    assert double_the_difference([1, 2, 3, 4, 5]) == 35

def test_only_zero():
    assert double_the_difference([0]) == 0

def test_large_numbers_suite2():
    assert double_the_difference([101, 203, 305]) == 101**2 + 203**2 + 305**2

def test_floats_ignored():
    assert double_the_difference([1.0, 2.5, 3]) == 9

def test_strings_ignored():
    assert double_the_difference([1, "a", 3, "b"]) == 10

def test_mixed_types_suite2():
    assert double_the_difference([1, 2.5, 3, -4, "a", 5]) == 35

def test_negative_and_floats():
    assert double_the_difference([-1.5, -2, 0.5, 1]) == 1

def test_large_list():
    large_list = list(range(1, 101, 2))  # Odd numbers from 1 to 99
    expected_sum = sum(x**2 for x in large_list)
    assert double_the_difference(large_list) == expected_sum

def test_list_with_none():
    assert double_the_difference([1, None, 3]) == 10

def test_list_with_boolean():
    assert double_the_difference([1, True, 3]) == 10