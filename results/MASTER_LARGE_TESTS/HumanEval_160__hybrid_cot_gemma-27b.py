import pytest

# Assume do_algebra is already defined and imported

@pytest.mark.parametrize(
    "operators, operands, expected",
    [
        (['+'], [1, 2], 3),
        (['-'], [5, 2], 3),
        (['*'], [3, 4], 12),
        (['//'], [10, 2], 5),
        (['**'], [2, 3], 8),
        (['+', '*'], [2, 3, 4], 14),
        (['-', '+'], [10, 5, 2], 13),
        (['*', '/', '+'], [10, 2, 5, 1], 26),
        (['+', '-', '*', '//', '**'], [1, 2, 3, 4, 5, 2], 1),
        (['+'], [0, 5], 5),
        (['-'], [5, 0], 5),
        (['*'], [0, 5], 0),
        (['**'], [2, 0], 1),
        (['**'], [0, 5], 0),
        (['**'], [2, 1], 2),
        (['+'], [-1, 2], 1),
        (['+'], [10, 5], 15),
        (['-'], [10, 5], 5),
        (['+'], [1000000, 2000000], 3000000),
        (['*'], [1000, 1000], 1000000),
        (['**'], [2, 100], 1267650600228229401496703205376),
    ],
)
def test_algebra(operators, operands, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            do_algebra(operators, operands)
    else:
        assert do_algebra(operators, operands) == expected

@pytest.mark.parametrize(
    "operators, operands",
    [
        (['//'], [5, 0],),
        ([], [1, 2, 3]),
        ([ '+'], []),
    ],
)
def test_edge_cases(operators, operands):
    if operators == ['//'] and operands == [5, 0]:
        with pytest.raises(ZeroDivisionError):
            do_algebra(operators, operands)
    else:
        with pytest.raises(IndexError):
            do_algebra(operators, operands)

@pytest.mark.parametrize(
    "operators, operands, expected",
    [
        (['*', '+'], [2, 3, 4], 14),
        (['+', '*'], [2, 3, 4], 14),
        (['-', '*', '+'], [10, 2, 3, 5], 10 - 2 * 3 + 5),
    ],
)
def test_precedence(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

@pytest.mark.parametrize(
    "operators, operands",
    [
        (['+'], [1000000, 2000000]),
        (['*'], [1000, 1000]),
        (['**'], [2, 100]),
    ],
)
def test_large_numbers(operators, operands):
    result = do_algebra(operators, operands)
    assert isinstance(result, int)