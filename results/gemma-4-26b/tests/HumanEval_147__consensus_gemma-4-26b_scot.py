
def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """

import pytest

def test_get_max_triples_example():
    """Test the example provided in the problem description."""
    assert get_max_triples(5) == 1

@pytest.mark.parametrize("n, expected", [
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 1),
    (5, 1),
    (6, 4),
    (7, 10),
    (8, 11),
    (9, 21),
    (10, 36),
])
def test_get_max_triples_small_values(n, expected):
    """Test small values of n to ensure the logic holds for basic sequences."""
    assert get_max_triples(n) == expected

@pytest.mark.parametrize("n, expected", [
    (15, 130),
    (20, 321),
    (100, 53361),
    (1000, 55333551),
])
def test_get_max_triples_large_values(n, expected):
    """Test various input sizes including larger values to ensure correctness and scale."""
    assert get_max_triples(n) == expected

def test_get_max_triples_logic_consistency():
    """Verifies that the result is non-decreasing as n increases."""
    prev_val = 0
    for n in range(1, 21):
        current_val = get_max_triples(n)
        assert current_val >= prev_val
        prev_val = current_val

@pytest.mark.parametrize("n", [1, 10, 50, 100, 500])
def test_get_max_triples_input_type(n):
    """Ensure the function accepts positive integers and returns an integer."""
    result = get_max_triples(n)
    assert isinstance(result, int)
    assert result >= 0