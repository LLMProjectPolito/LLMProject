
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

# The function is provided here for context
def get_max_triples(n: int) -> int:
    """
    Implementation placeholder.
    Logic: a[i] % 3 follows pattern 1, 0, 1, 1, 0, 1...
    """
    pass

@pytest.mark.parametrize("n, expected, reason", [
    # --- Edge Cases: Insufficient elements ---
    (1, 0, "n < 3: Not enough elements for a triple"),
    (2, 0, "n < 3: Not enough elements for a triple"),
    
    # --- Boundary Case: Minimum elements ---
    (3, 0, "n=3: Residues [1, 0, 1] sum to 2 (not multiple of 3)"),
    
    # --- Standard Progression: Small n ---
    (4, 1, "n=4: Residues [1, 0, 1, 1] -> C(3, 3) ones = 1"),
    (5, 1, "n=5: Example case [1, 0, 1, 1, 0] -> C(3, 3) ones = 1"),
    (6, 4, "n=6: Residues [1, 0, 1, 1, 0, 1] -> C(4, 3) ones = 4"),
    (7, 10, "n=7: Residues [1, 0, 1, 1, 0, 1, 1] -> C(5, 3) ones = 10"),
    (8, 11, "n=8: Residues [1, 0, 1, 1, 0, 1, 1, 0] -> C(3, 3) zeros + C(5, 3) ones = 1 + 10"),
    
    # --- Large/Mathematical Property Cases ---
    (10, 36, "n=10: 3 zeros (C(3,3)=1) + 7 ones (C(7,3)=35) = 36"),
    (12, 60, "n=12: 4 zeros (C(4,3)=4) + 8 ones (C(8,3)=56) = 60"),
])
def test_get_max_triples_scenarios(n, expected, reason):
    """
    Tests a wide range of n values covering edge cases, the problem example,
    arithmetic progression, and mathematical properties.
    """
    assert get_max_triples(n) == expected, f"Failed at n={n}: {reason}"

def test_get_max_triples_return_type():
    """Ensures the function adheres to the integer return type contract."""
    result = get_max_triples(5)
    assert isinstance(result, int), "The function must return an integer."

def test_get_max_triples_non_negative():
    """Ensures the count of triples is never negative."""
    assert get_max_triples(100) >= 0