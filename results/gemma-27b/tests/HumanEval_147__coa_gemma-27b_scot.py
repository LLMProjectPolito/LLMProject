import pytest
import math


# Focus: Boundary Values
import pytest

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
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

@pytest.mark.parametrize("n", [0, 1, 2])
def test_get_max_triples_boundary(n):
    """Tests boundary values for n (0, 1, 2)."""
    expected = {
        0: 0,
        1: 0,
        2: 0
    }.get(n)
    assert get_max_triples(n) == expected

@pytest.mark.parametrize("n", [3, 4, 5])
def test_get_max_triples_small_values(n):
    """Tests small values of n to check basic functionality."""
    expected = {
        3: 0,
        4: 0,
        5: 1
    }.get(n)
    assert get_max_triples(n) == expected

# Focus: Equivalence Partitioning
import pytest

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
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

@pytest.mark.parametrize("n", [0, 1, 2])
def test_get_max_triples_edge_cases(n):
    """
    Equivalence Partitioning: Test edge cases (n=0, n=1, n=2) where the number of possible triples is limited.
    These represent partitions where the loop conditions result in zero or minimal iterations.
    """
    assert get_max_triples(n) == 0

@pytest.mark.parametrize("n", [3, 4, 5])
def test_get_max_triples_small_values(n):
    """
    Equivalence Partitioning: Test small values of n (3, 4, 5) to cover cases with a manageable number of triples.
    These values allow for manual verification of the results and cover different combinations of remainders when divided by 3.
    """
    if n == 3:
        assert get_max_triples(n) == 0
    elif n == 4:
        assert get_max_triples(n) == 0
    elif n == 5:
        assert get_max_triples(n) == 1

@pytest.mark.parametrize("n", [6, 7, 8])
def test_get_max_triples_larger_values(n):
    """
    Equivalence Partitioning: Test larger values of n (6, 7, 8) to cover cases with a larger number of triples.
    These values test the scalability of the function and cover more complex combinations of remainders.
    """
    if n == 6:
        assert get_max_triples(n) == 3
    elif n == 7:
        assert get_max_triples(n) == 6
    elif n == 8:
        assert get_max_triples(n) == 10

# Focus: Large Input/Performance
import pytest
import time

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
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

@pytest.mark.parametrize("n", [100, 500, 1000])
def test_get_max_triples_large_input(n):
    """Tests the function with large input sizes to assess performance."""
    start_time = time.time()
    result = get_max_triples(n)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Input size: {n}, Result: {result}, Execution time: {execution_time:.4f} seconds")
    assert execution_time < 5  # Adjust threshold based on acceptable performance

@pytest.mark.parametrize("n", [2000, 3000])
def test_get_max_triples_very_large_input(n):
    """Tests the function with very large input sizes to assess performance."""
    start_time = time.time()
    result = get_max_triples(n)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Input size: {n}, Result: {result}, Execution time: {execution_time:.4f} seconds")
    assert execution_time < 10 # Adjust threshold based on acceptable performance