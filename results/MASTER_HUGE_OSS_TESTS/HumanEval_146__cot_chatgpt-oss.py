import pytest

# Basic examples from the problem statement
@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([15, -73, 14, -15], 1),          # only 15 qualifies
        ([33, -2, -3, 45, 21, 109], 2),   # 33 and 109 qualify
    ],
)
def test_special_filter_examples(input_list, expected):
    assert specialFilter(input_list) == expected


# Empty input should return 0
def test_special_filter_empty():
    assert specialFilter([]) == 0


# Numbers exactly at the boundary (10 is not >10, 11 is)
@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([10, 11, 12, 13], 2),   # 11 and 13 qualify
        ([10, 20, 30], 0),       # none qualify
    ],
)
def test_special_filter_boundary_values(input_list, expected):
    assert specialFilter(input_list) == expected


# Mixed qualifying and non‑qualifying numbers
@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([11, 22, 33, 44, 55], 3),          # 11, 33, 55 qualify
        ([101, 202, 303, 404, 505], 3),    # 101, 303, 505 qualify
        ([19, 29, 39, 49, 59], 5),         # all qualify
        ([20, 30, 40, 50], 0),             # none qualify
        ([999999999, 123456789, 2468, -135], 2),  # first two qualify
    ],
)
def test_special_filter_mixed_cases(input_list, expected):
    assert specialFilter(input_list) == expected


# All numbers qualify
def test_special_filter_all_qualify():
    nums = [11, 111, 1111, 11111]
    assert specialFilter(nums) == len(nums)


# Large numbers with many digits
def test_special_filter_large_numbers():
    nums = [9_999_999_991, 8_888_888_888, 7_777_777_777]
    # 9_999_999_991 (first 9 odd, last 1 odd) qualifies; the others do not
    assert specialFilter(nums) == 1


# Verify that non‑integer elements raise a TypeError (implementation‑defined)
def test_special_filter_invalid_type():
    with pytest.raises(TypeError):
        specialFilter([1, "2", 3])