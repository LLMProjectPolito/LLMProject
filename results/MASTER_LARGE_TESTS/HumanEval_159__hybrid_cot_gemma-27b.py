import pytest

@pytest.mark.parametrize(
    "number, need, remaining, expected",
    [
        (5, 6, 10, [11, 4]),
        (4, 8, 9, [12, 1]),
        (1, 10, 10, [11, 0]),
        (2, 11, 5, [7, 0]),
        (0, 0, 0, [0, 0]),
        (0, 0, 5, [0, 5]),
        (5, 0, 5, [5, 5]),
        (0, 5, 0, [0, 0]),
        (1000, 1000, 1000, [2000, 0]),
        (1000, 1000, 0, [1000, 0]),
        (0, 1000, 1000, [1000, 0]),
        (5, 10, 3, [8, 0]),
        (5, 3, 10, [8, 7]),
        (5, 5, 5, [10, 0]),
        (500, 600, 100, [600, 0]),
        (5, 6, 0, [5, 0]),
        (0, 5, 0, [0, 0]),
        (5, 0, 10, [5, 10]),
        (0, 0, 0, [0, 0]),
        (5, 6, 5, [11, 0]),
        (1, 2, 10, [3, 8]),
        (5, 10, 3, [8, 0]),
        (1, 5, 2, [3, 0]),
        (0, 5, 5, [5, 0]),
        (5, 0, 5, [5, 5]),
        (5, 5, 0, [5, 0]),
        (1000, 500, 500, [1500, 0]),
        (500, 1000, 500, [1000, 0]),
        (500, 500, 1000, [1000, 500]),
        (5, 5, 5, [10, 0]),
        (5, 6, 1, [6, 0]),
        (999, 1000, 1000, [1999, 0]),
        (500, 999, 500, [1000, 0]),
        (500, 500, 999, [1000, 0]),
        pytest.param(-1, 5, 5, [4, 5], marks=pytest.mark.xfail(reason="Negative input")),
        pytest.param(5, -1, 5, [4, 5], marks=pytest.mark.xfail(reason="Negative input")),
        pytest.param(5, 5, -1, [5, 0], marks=pytest.mark.xfail(reason="Negative input")),
    ],
)
def test_eat(number, need, remaining, expected):
    from your_module import eat  # Replace your_module
    result = eat(number, need, remaining)
    assert result == expected