import pytest

def test_special_filter_empty():
    assert specialFilter([]) == 0

def test_special_filter_no_match():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_special_filter_basic_match():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_special_filter_multiple_matches():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_special_filter_mixed():
    assert specialFilter([11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 303, 313, 323, 333, 343, 353, 363, 373, 383, 393, 404, 414, 424, 434, 444, 454, 464, 474, 484, 494, 505, 515, 525, 535, 545, 555, 565, 575, 585, 595, 606, 616, 626, 636, 646, 656, 666, 676, 686, 696, 707, 717, 727, 737, 747, 757, 767, 777, 787, 797, 808, 818, 828, 838, 848, 858, 868, 878, 888, 898, 909, 919, 929, 939, 949, 959, 969, 979, 989, 999]) == 90

def test_special_filter_negative_numbers():
    assert specialFilter([-11, -33, -55, -77, -99]) == 0

def test_special_filter_large_numbers():
    assert specialFilter([11111, 33333, 55555, 77777, 99999]) == 5

def test_special_filter_numbers_greater_than_10():
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 10

def test_special_filter_mixed_positive_and_negative():
    assert specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109, -11, 3, 5, 7, 9]) == 2