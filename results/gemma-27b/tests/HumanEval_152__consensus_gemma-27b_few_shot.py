import pytest

def test_compare_basic():
    assert compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) == [0,0,0,0,3,3]

def test_compare_all_correct():
    assert compare([1,2,3],[1,2,3]) == [0,0,0]

def test_compare_all_incorrect():
    assert compare([1,2,3],[4,5,6]) == [3,3,3]

def test_compare_mixed():
    assert compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) == [4,4,1,0,0,6]

def test_compare_empty():
    assert compare([],[]) == []

def test_compare_single_element_correct():
    assert compare([5],[5]) == [0]

def test_compare_single_element_incorrect():
    assert compare([5],[6]) == [1]

def test_compare_negative_numbers():
    assert compare([-1,-2,-3],[-1,-2,-3]) == [0,0,0]

def test_compare_negative_and_positive():
    assert compare([-1,2,-3],[1,-2,3]) == [2,4,6]

def test_compare_large_numbers():
    assert compare([1000,2000,3000],[1000,2001,2999]) == [0,1,1]