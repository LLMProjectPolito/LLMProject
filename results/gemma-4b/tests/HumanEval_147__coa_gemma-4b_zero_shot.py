
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
import math


# Focus: Boundary Values
import pytest

def test_max_triples_n_1():
    assert get_max_triples(1) == 0

def test_max_triples_n_2():
    assert get_max_triples(2) == 0

def test_max_triples_n_3():
    assert get_max_triples(3) == 0

def test_max_triples_n_4():
    assert get_max_triples(4) == 1

def test_max_triples_n_5():
    assert get_max_triples(5) == 1

# Focus: Type Scenarios
import pytest

def test_type_scenario_n_1():
    assert get_max_triples(1) == 0

def test_type_scenario_n_2():
    assert get_max_triples(2) == 0

def test_type_scenario_n_3():
    assert get_max_triples(3) == 0

# Focus: Logic Branches
import pytest

def test_logic_branches_empty():
    assert get_max_triples(0) == 0

def test_logic_branches_small():
    assert get_max_triples(5) == 1

def test_logic_branches_larger():
    assert get_max_triples(10) == 4