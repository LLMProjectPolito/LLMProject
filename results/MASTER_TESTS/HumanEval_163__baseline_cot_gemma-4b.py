import pytest

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    result = []
    if a <= b:
        for i in range(a, b + 1):
            s = str(i)
            for digit in s:
                if int(digit) % 2 == 0:
                    if int(digit) not in result:
                        result.append(int(digit))
        result.sort()
    else:
        for i in range(a, b - 1, -1):
            s = str(i)
            for digit in s:
                if int(digit) % 2 == 0:
                    if int(digit) not in result:
                        result.append(int(digit))
        result.sort()
    return result

def test_generate_integers_normal_case():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reverse_order():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_digit_even():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_single_digit_odd():
    assert generate_integers(1, 3) == []

def test_generate_integers_larger_range():
    assert generate_integers(10, 20) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def test_generate_integers_with_zeros():
    assert generate_integers(20, 25) == [2, 4, 6, 8, 20, 22, 24]

def test_generate_integers_start_and_end_same():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_large_numbers():
    assert generate_integers(100, 102) == [100, 102]

def test_generate_integers_edge_case_1():
    assert generate_integers(1, 2) == []

def test_generate_integers_edge_case_2():
    assert generate_integers(2, 1) == [2]

def test_generate_integers_edge_case_3():
    assert generate_integers(1, 1) == []

def test_generate_integers_edge_case_4():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_edge_case_5():
    assert generate_integers(1000, 1002) == [1000, 1002]