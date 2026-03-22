import pytest

@pytest.mark.parametrize(
    "number, need, remaining, expected",
    [
        (1000, 0, 500, [1000, 500]),   # max eaten, need zero, carrots left
        (1000, 0, 0,   [1000, 0]),     # max eaten, need zero, no carrots left
        (0,    1000, 0, [0, 0]),       # no carrots, still need to eat
        (0,    0,    500, [0, 500]),   # no need, carrots available
        (7,    5,    0, [7, 0]),       # need positive but no carrots left
    ],
)
def test_eat(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected