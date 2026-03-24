import pytest
from your_module import double_the_difference  # Replace your_module

def test_empty_list():
    assert double_the_difference([]) == 0

def test_positive_odd_numbers():
    assert double_the_difference([1, 3, 5]) == 1 + 9 + 25 == 35

def test_mixed_positive_and_even_numbers():
    assert double_the_difference([1, 2, 3, 4, 5]) == 1 + 9 + 25 == 35

def test_negative_numbers():
    assert double_the_difference([-1, -2, -3]) == 0

def test_negative_and_positive_numbers():
    assert double_the_difference([-1, 1, -2, 3]) == 1 + 9 == 10

def test_zero_in_list():
    assert double_the_difference([0, 1, 2, 3]) == 1 + 9 == 10

def test_all_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_all_negative_even_numbers():
    assert double_the_difference([-2, -4, -6]) == 0

def test_mixed_positive_negative_even_odd():
    assert double_the_difference([1, -2, 3, -4, 5]) == 1 + 9 + 25 == 35

def test_floats_and_strings():
    assert double_the_difference([1.5, "a", 3, 4.2]) == 9

def test_single_odd_number():
    assert double_the_difference([7]) == 49

def test_single_even_number():
    assert double_the_difference([2]) == 0

def test_single_negative_number():
    assert double_the_difference([-5]) == 0

def test_large_numbers():
    assert double_the_difference([101, 203]) == 10201 + 41209 == 51410

def test_zero_and_odd():
    assert double_the_difference([0, 1]) == 1

def test_zero_and_even():
    assert double_the_difference([0, 2]) == 0

def test_negative_and_positive_mixed():
    assert double_the_difference([-1, 2, 3, -4, 5]) == 1 + 9 + 25 == 35

def test_single_odd_number_2():
    assert double_the_difference([7]) == 49

def test_single_even_number_2():
    assert double_the_difference([4]) == 0

def test_single_negative_odd_number():
    assert double_the_difference([-1]) == 0

def test_single_negative_even_number():
    assert double_the_difference([-2]) == 0

def test_single_zero():
    assert double_the_difference([0]) == 0

def test_floats_and_strings_2():
    assert double_the_difference([1.5, "a", 3]) == 9

def test_mixed_types():
    assert double_the_difference([1, 2.0, "hello", 3, -4, 5]) == 1 + 9 + 25 == 35

def test_large_numbers_2():
    assert double_the_difference([1001, 3003]) == 1001**2 + 3003**2 == 1002001 + 9018009 == 10020010

def test_example_1():
    assert double_the_difference([1, 3, 2, 0]) == 1 + 9 == 10

def test_example_2():
    assert double_the_difference([-1, -2, 0]) == 0

def test_example_3():
    assert double_the_difference([9, -2]) == 81

def test_example_4():
    assert double_the_difference([0]) == 0