import pytest

def generate_integers(a, b):
    """
    Given two integers a and b, return the numbers between a and b
    (inclusive) where all digits are even, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    generate_integers(-1, 0) => []
    """
    if a > b:
        a, b = b, a
    result = []
    for i in range(a, b + 1):
        s = str(i)
        all_even = True
        for digit in s:
            if int(digit) % 2 != 0:
                all_even = False
                break
        if all_even:
            result.append(i)
    return result

def test_normal_case():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_no_even_digits():
    assert generate_integers(10, 14) == []

def test_single_digit_range():
    assert generate_integers(2, 2) == [2]

def test_single_digit_odd():
    assert generate_integers(3, 3) == []

def test_start_at_zero():
    assert generate_integers(0, 5) == [0, 2, 4]

def test_end_at_zero():
    assert generate_integers(5, 0) == [0, 2, 4]

def test_large_range():
    assert generate_integers(1, 9) == [2, 4, 6, 8]

def test_large_range_with_gap():
    assert generate_integers(1, 11) == [2, 4, 6, 8]

def test_same_number():
    assert generate_integers(4, 4) == [4]

def test_negative_numbers():
    assert generate_integers(-2, -1) == []

def test_negative_input_with_zero():
    assert generate_integers(-1, 0) == []

def test_mixed_digits():
    assert generate_integers(1234, 1236) == []

def test_mixed_digits_2():
    assert generate_integers(123, 124) == []

def test_mixed_digits_some_even():
    assert generate_integers(12345, 12347) == []

def test_large_numbers_with_mixed_digits():
    assert generate_integers(12345678, 12345680) == []