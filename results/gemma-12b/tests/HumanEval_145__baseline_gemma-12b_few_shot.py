def sum_digits(n: int) -> int:
    """Calculates the sum of the digits of an integer."""
    s = 0
    for digit in str(abs(n)):
        s += int(digit)
    return s

def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    assert order_by_points([5]) == [5]

def test_order_by_points_same_digit_sum():
    assert order_by_points([1, 10, 100]) == [1, 10, 100]

def test_order_by_points_negative_numbers():
    assert order_by_points([-1, -10, -100]) == [-1, -10, -100]

def test_order_by_points_mixed_positive_negative():
    assert order_by_points([1, -1, 10, -10]) == [1, -1, 10, -10]

def test_order_by_points_zero():
    assert order_by_points([0, 1, -1]) == [0, 1, -1]

def test_order_by_points_duplicate_numbers():
    assert order_by_points([2, 2, 2]) == [2, 2, 2]

def test_order_by_points_large_numbers():
    assert order_by_points([123, 45, 6]) == [123, 45, 6]

def test_order_by_points_complex_case():
    assert order_by_points([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def test_order_by_points_another_complex_case():
    assert order_by_points([12, 21, 3, 13, 23]) == [3, 13, 12, 21, 23]