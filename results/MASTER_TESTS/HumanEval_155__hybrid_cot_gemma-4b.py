import pytest
from your_module import even_odd_count  # Replace your_module

@pytest.mark.parametrize(
    "input_num, expected",
    [
        (0, (1, 0)),
        (-12, (1, 1)),
        (123, (1, 2)),
        (2468, (4, 0)),
        (13579, (0, 5)),
        (1000, (3, 0)),
        (-1000, (3, 0)),
        (1234567890, (5, 5)),
        (9876543210, (5, 5)),
        (1, (0, 1)),
        (2, (1, 0)),
        (-1, (0, 1)),
        (-2, (1, 0)),
        (10, (1, 1)),
        (11, (0, 2)),
        (121, (2, 1)),
        (12345678901234567890, (10, 10)),
    ],
)
def test_even_odd_count_parametrized(input_num, expected):
    assert even_odd_count(input_num) == expected

def test_even_odd_count_additional():
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(2) == (1, 0)
    assert even_odd_count(1) == (0, 1)
    assert even_odd_count(2468) == (4, 0)
    assert even_odd_count(13579) == (0, 5)
    assert even_odd_count(1234567890) == (5, 5)
    assert even_odd_count(-1234567890) == (5, 5)
    assert even_odd_count(102030405) == (5, 5)
    assert even_odd_count(-102030405) == (5, 5)
    assert even_odd_count(12) == (2, 0)
    assert even_odd_count(11) == (0, 2)
    assert even_odd_count(-11) == (0, 2)
    assert even_odd_count(101010) == (5, 5)
    assert even_odd_count(-101010) == (5, 5)
    assert even_odd_count(9876543210) == (5, 5)
    assert even_odd_count(-9876543210) == (5, 5)