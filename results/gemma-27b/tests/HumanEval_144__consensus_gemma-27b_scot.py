import pytest

def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))

    result_num = x_num * n_num
    result_den = x_den * n_den

    return result_num % result_den == 0

# STEP 2: PLAN
# Test functions:
# - test_simplify_whole_number: Tests cases where the result is a whole number.
# - test_simplify_not_whole_number: Tests cases where the result is not a whole number.
# - test_simplify_edge_cases: Tests edge cases like 1/1, small numbers, and larger numbers.
# - test_simplify_invalid_input: Tests cases with invalid input (although the problem states input is valid, good to have).

@pytest.mark.parametrize(
    "x, n, expected",
    [
        ("1/5", "5/1", True),
        ("1/6", "2/1", False),
        ("7/10", "10/2", False),
        ("1/1", "1/1", True),
        ("2/3", "3/2", True),
        ("1/2", "2/1", True),
        ("3/4", "4/3", True),
        ("1/3", "2/1", False),
        ("2/5", "5/2", True),
        ("1/7", "7/1", True),
        ("5/2", "2/5", True),
        ("10/3", "3/10", True),
        ("11/2", "2/11", True),
        ("1/4", "4/1", True),
        ("3/5", "5/3", True),
        ("2/7", "7/2", True),
        ("1/8", "8/1", True),
        ("8/1", "1/8", True),
        ("1/9", "9/1", True),
        ("9/1", "1/9", True),
        ("1/100", "100/1", True),
        ("100/1", "1/100", True),
        ("1/2", "3/1", False),
        ("2/3", "1/2", False),
        ("3/4", "1/2", False),
        ("4/5", "1/3", False),
        ("5/6", "1/4", False),
    ],
)
def test_simplify_whole_number(x, n, expected):
    assert simplify(x, n) == expected

@pytest.mark.parametrize(
    "x, n, expected",
    [
        ("1/2", "1/3", False),
        ("1/4", "1/2", False),
        ("2/3", "1/4", False),
        ("3/4", "1/3", False),
        ("1/5", "1/2", False),
        ("2/5", "1/3", False),
        ("3/5", "1/4", False),
        ("4/5", "1/6", False),
        ("1/7", "1/2", False),
        ("2/7", "1/3", False),
        ("3/7", "1/4", False),
        ("4/7", "1/5", False),
        ("5/7", "1/6", False),
        ("6/7", "1/8", False),
        ("1/10", "1/2", False),
        ("2/10", "1/3", False),
        ("3/10", "1/4", False),
        ("4/10", "1/5", False),
        ("5/10", "1/6", False),
        ("6/10", "1/7", False),
        ("7/10", "1/8", False),
        ("8/10", "1/9", False),
        ("9/10", "1/10", False),
    ],
)
def test_simplify_not_whole_number(x, n, expected):
    assert simplify(x, n) == expected

@pytest.mark.parametrize(
    "x, n, expected",
    [
        ("1/1", "1/1", True),
        ("1/2", "2/1", True),
        ("2/1", "1/2", True),
        ("1/10", "10/1", True),
        ("10/1", "1/10", True),
        ("1/100", "100/1", True),
        ("100/1", "1/100", True),
        ("1/1000", "1000/1", True),
        ("1000/1", "1/1000", True),
    ],
)
def test_simplify_edge_cases(x, n, expected):
    assert simplify(x, n) == expected