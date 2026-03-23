import pytest
from your_module import specialFilter  # Replace your_module

def is_odd_digit(digit):
    return int(digit) % 2 != 0

def check_first_and_last_digit_odd(num):
    num_str = str(abs(num))
    if not num_str:
        return False
    first_digit = num_str[0]
    last_digit = num_str[-1]
    return is_odd_digit(first_digit) and is_odd_digit(last_digit)

@pytest.fixture
def sample_data():
    return [
        [15, -73, 14, -15],
        [33, -2, -3, 45, 21, 109],
        [11, 22, 33, 44, 55],
        [1, 3, 5, 7, 9],
        [2, 4, 6, 8, 10],
        [111, 121, 131, 141, 151],
        [10, 20, 30, 40, 50],
        [15, 25, 35, 45, 55],
        [11, 13, 15, 17, 19],
        [21, 23, 25, 27, 29],
        [],
        [10],
        [11],
        [101],
        [1001],
        [10001],
        [-11],
        [-13],
        [-15],
        [-17],
        [-19],
        [15.0],
        [15.1],
        [15.5],
        [15.9],
        [15.01],
        [15.02],
        [15.03],
        [15.04],
        [15.05],
        [15.06],
        [15.07],
        [15.08],
        [15.09],
        [15.10],
        [15.11],
        [15.12],
        [15.13],
        [15.14],
        [15.15],
        [15.16],
        [15.17],
        [15.18],
        [15.19],
        [15.20],
        [15.21],
        [15.22],
        [15.23],
        [15.24],
        [15.25],
        [15.26],
        [15.27],
        [15.28],
        [15.29],
        [15.30],
        [15.31],
        [15.32],
        [15.33],
        [15.34],
        [15.35],
        [15.36],
        [15.37],
        [15.38],
        [15.39],
        [15.40],
        [15.41],
        [15.42],
        [15.43],
        [15.44],
        [15.45],
        [15.46],
        [15.47],
        [15.48],
        [15.49],
        [15.50],
        [15.51],
        [15.52],
        [15.53],
        [15.54],
        [15.55],
        [15.56],
        [15.57],
        [15.58],
        [15.59],
        [15.60],
        [15.61],
        [15.62],
        [15.63],
        [15.64],
        [15.65],
        [15.66],
        [15.67],
        [15.68],
        [15.69],
        [15.70],
        [15.71],
        [15.72],
        [15.73],
        [15.74],
        [15.75],
        [15.76],
        [15.77],
        [15.78],
        [15.79],
        [15.80],
        [15.81],
        [15.82],
        [15.83],
        [15.84],
        [15.85],
        [15.86],
        [15.87],
        [15.88],
        [15.89],
        [15.90],
        [15.91],
        [15.92],
        [15.93],
        [15.94],
        [15.95],
        [15.96],
        [15.97],
        [15.98],
        [15.99]
    ]

def test_special_filter_empty_list():
    assert specialFilter([]) == 0

def test_special_filter_no_matches():
    assert specialFilter([2, 4, 6, 8, 10]) == 0

def test_special_filter_single_match():
    assert specialFilter([15, 2, 4, 6, 8, 10]) == 1

def test_special_filter_multiple_matches():
    assert specialFilter([33, 2, 4, 6, 8, 10, 109]) == 2

def test_special_filter_negative_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_special_filter_all_matches():
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_special_filter_mixed_numbers():
    assert specialFilter([11, 22, 33, 44, 55]) == 3

def test_special_filter_large_numbers():
    assert specialFilter([111, 121, 131, 141, 151]) == 5

def test_special_filter_zero():
    assert specialFilter([0, 15, 33]) == 1

def test_special_filter_decimal_numbers():
    assert specialFilter([15.0, 15.1, 15.5, 15.9]) == 0

def test_special_filter_decimal_numbers_with_odd_digits():
    assert specialFilter([15.01, 15.03, 15.05, 15.07, 15.09]) == 0

def test_special_filter_decimal_numbers_with_odd_digits_2():
    assert specialFilter([15.11, 15.13, 15.15, 15.17, 15.19]) == 0

def test_special_filter_decimal_numbers_with_odd_digits_3():
    assert specialFilter([15.21, 15.23, 15.25, 15.27, 15.29]) == 0

def test_special_filter_decimal_numbers_with_odd_digits_4():
    assert specialFilter([15.31, 15.33, 15.35, 15.37, 15.39]) == 0

def test_special_filter_decimal_numbers_with_odd_digits_5():
    assert specialFilter([15.41, 15.43, 15.45, 15.47, 15.49]) == 0

def test_special_filter_decimal_numbers_with_odd_digits_6():
    assert specialFilter([15.51, 15.53, 15.55, 15.57, 15.59]) == 0

def test_special_filter_decimal_numbers_with_odd_digits_7():
    assert specialFilter([15.61, 15.63, 15.65, 15.67, 15.69]) == 0

def test_special_filter_decimal_numbers_with_odd_digits_8():
    assert specialFilter([15.71, 15.73, 15.75, 15.77, 15.79]) == 0

def test_special_filter_decimal_numbers_with_odd_digits_9():
    assert specialFilter([15.81, 15.83, 15.85, 15.87, 15.89]) == 0

def test_special_filter_decimal_numbers_with_odd_digits_10():
    assert specialFilter([15.91, 15.93, 15.95, 15.97, 15.99]) == 0