import pytest

@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 1),
    (25, 15, 5),
    (48, 18, 6),
    (101, 103, 1),
    (0, 5, 5),
    (17, 0, 17),
    (12, 18, 6),
    (7, 7, 7),
    (10, 0, 10),
    (-5, 5, 5),
    (5, -5, 5),
    (0, 0, 0),
    (-3, -5, 1),
    (-25, -15, 5),
    (-3, 5, 1),
    (3, -5, 1),
])
def test_greatest_common_divisor(a, b, expected):
    assert greatest_common_divisor(a, b) == expected

def test_greatest_common_divisor_negative():
    assert greatest_common_divisor(-3, 5) == greatest_common_divisor(3, 5)
    assert greatest_common_divisor(3, -5) == greatest_common_divisor(3, 5)
    assert greatest_common_divisor(-3, -5) == greatest_common_divisor(3, 5)

def test_greatest_common_divisor_same():
    assert greatest_common_divisor(5, 5) == 5
    assert greatest_common_divisor(25, 25) == 25

def test_greatest_common_divisor_invalid_input():
    with pytest.raises(TypeError):
        greatest_common_divisor("a", 5)
    with pytest.raises(TypeError):
        greatest_common_divisor(5, "a")
    with pytest.raises(TypeError):
        greatest_common_divisor("a", "b")