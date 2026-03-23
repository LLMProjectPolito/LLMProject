import pytest
from math import comb
# Import the implementation – adjust the module name if it differs.
# The function must be defined elsewhere; we only import it here.
from solution import get_max_triples


def brute_max_triples(n: int) -> int:
    """
    Simple O(n³) reference implementation used only for tiny n.
    """
    a = [i * i - i + 1 for i in range(1, n + 1)]
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    cnt += 1
    return cnt


def formula_max_triples(n: int) -> int:
    """
    Closed‑form derived from the observation that
        a[i] % 3 == 0  ⇔  i % 3 == 2
        a[i] % 3 == 1  ⇔  i % 3 == 0 or 1

    The answer is C(cnt0, 3) + C(cnt1, 3) where
        cnt0 = number of i with i % 3 == 2
        cnt1 = n - cnt0
    """
    cnt0 = n // 3                     # every third index (i = 2,5,8,…)
    cnt1 = n - cnt0
    return comb(cnt0, 3) + comb(cnt1, 3)


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),   # n is positive in the statement, but we test 0 for robustness
        (1, 0),
        (2, 0),
        (3, 0),   # only one triple (1,3,7) → sum = 11 % 3 != 0
        (4, 0),
        (5, 1),   # example from the prompt
        (6, 4),
        (7, 8),
        (8, 13),
        (9, 20),
        (10, 28),
    ],
)
def test_small_values_against_brute(n, expected):
    """Validate the function for small n where a brute‑force check is feasible."""
    assert get_max_triples(n) == expected
    # Double‑check with the brute implementation for n ≤ 9
    if n <= 9:
        assert get_max_triples(n) == brute_max_triples(n)


@pytest.mark.parametrize("n", [11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
def test_small_range_against_formula(n):
    """Cross‑check the implementation against the derived closed form."""
    assert get_max_triples(n) == formula_max_triples(n)


@pytest.mark.parametrize("n", [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])
def test_medium_range_against_formula(n):
    """Medium‑sized inputs – still trivial to compute with the formula."""
    assert get_max_triples(n) == formula_max_triples(n)


@pytest.mark.parametrize("n", [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
def test_larger_values_against_formula(n):
    """Larger values to ensure the implementation stays O(1) and matches the formula."""
    assert get_max_triples(n) == formula_max_triples(n)


def test_very_large_input():
    """
    Stress test with a very large n (10⁶). The function should return instantly
    and the result must match the combinatorial formula.
    """
    n = 1_000_000
    expected = formula_max_triples(n)
    assert get_max_triples(n) == expected


def test_type_and_non_negative():
    """The function must always return a non‑negative integer."""
    for n in range(0, 20):
        result = get_max_triples(n)
        assert isinstance(result, int)
        assert result >= 0