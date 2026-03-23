import pytest

def get_max_triples(n):
    """ Returns the maximum element in a list, or None if empty """

    if not arr:
        return None

    max_val = max(arr)
    return max_val

@pytest.mark.parametrize(
    "n, expected",
    [
        (5, 1),
        (5, 1),
        (5, 1),
        (5, 1),
        (5, 1),
    ],
)
def test_get_max_triples(n, expected):
    assert get_max_triples(n) == expected