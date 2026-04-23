
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
from math import comb

@pytest.mark.parametrize("n, expected", [
    (5, 1),      # Example case: a = [1, 3, 7, 13, 21], a % 3 = [1, 0, 1, 1, 0]. Triples: (1, 7, 13)
    (1, 0),      # n < 3, no triples possible
    (2, 0),      # n < 3, no triples possible
    (3, 0),      # a % 3 = [1, 0, 1], sum = 2
    (4, 1),      # a % 3 = [1, 0, 1, 1], only (1, 7, 13) works
    (6, 4),      # a % 3 = [1, 0, 1, 1, 0, 1], 1s: 4, 0s: 2. comb(4,3) + comb(2,3) = 4 + 0 = 4
    (10, 36),    # a % 3 = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1], 1s: 7, 0s: 3. comb(7,3) + comb(3,3) = 35 + 1 = 36
])
def test_get_max_triples_known_cases(n, expected):
    """Test the function against specific known correct outputs."""
    assert get_max_triples(n) == expected

def test_get_max_triples_mathematical_consistency():
    """
    Test a range of values using the derived mathematical property.
    The sequence a[i] % 3 follows the pattern: 1, 0, 1, 1, 0, 1, 1, 0, 1...
    A triple sum is divisible by 3 if all three elements are 0 mod 3 or all three are 1 mod 3.
    """
    for n in range(1, 101):
        # Count of elements where i % 3 == 2 (which results in a[i] % 3 == 0)
        count_0 = (n + 1) // 3
        # Count of elements where i % 3 != 2 (which results in a[i] % 3 == 1)
        count_1 = n - count_0
        
        expected = comb(count_0, 3) + comb(count_1, 3)
        assert get_max_triples(n) == expected

def test_get_max_triples_large_input():
    """Test with a larger input to ensure performance and integer handling."""
    n = 500
    # count_0 = 501 // 3 = 167
    # count_1 = 500 - 167 = 333
    # expected = comb(167, 3) + comb(333, 3)
    count_0 = (n + 1) // 3
    count_1 = n - count_0
    expected = comb(count_0, 3) + comb(count_1, 3)
    
    assert get_max_triples(n) == expected

def test_get_max_triples_type_safety():
    """Ensure the function handles the input as expected (basic sanity check)."""
    # This is a placeholder for checking if the function returns an integer
    result = get_max_triples(10)
    assert isinstance(result, int)