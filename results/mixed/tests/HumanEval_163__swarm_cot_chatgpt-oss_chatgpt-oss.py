import pytest

@pytest.mark.parametrize(
    "lower, upper, expected",
    [
        (4, 4, [4]),   # even singleton
        (8, 8, [8]),   # another even singleton
        (5, 5, []),    # odd singleton
    ],
)
def test_generate_integers_singleton_cases(lower, upper, expected):
    assert generate_integers(lower, upper) == expected