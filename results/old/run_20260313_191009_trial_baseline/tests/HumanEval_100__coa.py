import pytest
import math


# Focus: Boundary Values
def test_make_a_pile_min_input():
    assert make_a_pile(1) == [1, 3, 5]

def test_make_a_pile_max_input():
    assert make_a_pile(100) == [100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200]

def test_make_a_pile_boundary_input():
    assert make_a_pile(2) == [2, 4]

# Focus: Type Scenarios
def test_make_a_pile_odd_input():
    assert make_a_pile(3) == [3, 5, 7]

def test_make_a_pile_even_input():
    assert make_a_pile(4) == [4, 6, 8]

def test_make_a_pile_single_level():
    assert make_a_pile(1) == [1]

# Focus: Logic Branches
def test_make_a_pile_odd_start():
    assert make_a_pile(3) == [3, 5, 7]

def test_make_a_pile_even_start():
    assert make_a_pile(4) == [4, 6, 8]

def test_make_a_pile_multiple_levels():
    assert make_a_pile(5) == [5, 7, 9, 11]