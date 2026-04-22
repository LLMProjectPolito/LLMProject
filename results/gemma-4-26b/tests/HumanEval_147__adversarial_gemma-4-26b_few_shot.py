
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

# Note: The function get_max_triples is assumed to be imported from the source module
# from solution import get_max_triples

@pytest.mark.parametrize("n, expected", [
    (1, 0),   # n < 3: Not enough elements to form a triple
    (2, 0),   # n < 3: Not enough elements to form a triple
    (3, 0),   # a = [1, 3, 7], mods = [1, 0, 1]. Sum mod 3 = 2. No triples.
    (4, 1),   # a = [1, 3, 7, 13], mods = [1, 0, 1, 1]. Triple (1, 7, 13) works.
    (5, 1),   # Example case from problem description
    (6, 4),   # a mods = [1, 0, 1, 1, 0, 1]. 1s: 4, 0s: 2. Comb(4,3) = 4.
    (8, 11),  # a mods = [1, 0, 1, 1, 0, 1, 1, 0]. 1s: 5, 0s: 3. Comb(5,3) + Comb(3,3) = 10 + 1 = 11.
])
def test_get_max_triples_logic(n, expected):
    """
    Tests the mathematical correctness for small n, including the 
    first instance where a triple of zeros (a[i] % 3 == 0) becomes possible.
    """
    assert get_max_triples(n) == expected

def test_get_max_triples_example():
    """Explicitly tests the example provided in the docstring."""
    assert get_max_triples(5) == 1

def test_get_max_triples_large_n_performance():
    """
    Tests for performance. 
    A naive O(n^3) implementation will be extremely slow for n=1000.
    An efficient O(n) or O(1) implementation should pass instantly.
    """
    # If the implementation is O(n^3), 1000^3 is 1 billion operations.
    # This test ensures the developer used the mathematical pattern.
    n = 1000
    # Calculation for n=1000:
    # i % 3 == 2 gives a[i] % 3 == 0. 
    # Indices: 2, 5, 8... 998. This is an AP: 2 + (k-1)3 = 998 => 3(k-1)=996 => k=334.
    # Count of 0s = 333 (Wait, let's re-calc: 2, 5... 998. 998 = 2 + 3(332). So 333 elements)
    # Let's use a simpler way: 1000 // 3 = 333. 
    # If i % 3 == 2, then i is 2, 5, 8... 998. 
    # The number of such elements is floor((1000-2)/3) + 1 = 333.
    # Count of 0s = 333. Count of 1s = 1000 - 333 = 667.
    # Result = Comb(333, 3) + Comb(667, 3)
    # Comb(333, 3) = (333 * 332 * 331) / 6 = 6,101,546
    # Comb(667, 3) = (667 * 666 * 665) / 6 = 49,234,105
    # Total = 55,335,651
    expected_large = 55335651
    assert get_max_triples(n) == expected_large

def test_get_max_triples_invalid_input():
    """
    Tests how the function handles non-positive integers.
    Depending on requirements, this should either return 0 or raise an error.
    """
    # Assuming the function should return 0 for n <= 0 based on 'positive integer' constraint
    assert get_max_triples(0) == 0
    
    # If the requirement is strict, we might check for ValueError
    # with pytest.raises(ValueError):
    #     get_max_triples(-5)

def test_get_max_triples_type_safety():
    """Checks if the function handles float inputs gracefully if passed."""
    # This is a defensive test to see if the function is robust against type errors
    with pytest.raises(TypeError):
        get_max_triples("5") # type: ignore