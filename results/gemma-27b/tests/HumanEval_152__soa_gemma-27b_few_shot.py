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

def test_compare_single_element():
    assert compare([5],[5]) == [0]

def test_compare_single_incorrect():
    assert compare([5],[6]) == [1]

def test_compare_negative_numbers():
    assert compare([-1,-2,-3],[-1,-2,-3]) == [0,0,0]

def test_compare_negative_incorrect():
    assert compare([-1,-2,-3],[-2,-1,-4]) == [1,1,1]

def test_compare_zeroes():
    assert compare([0,0,0],[0,0,0]) == [0,0,0]

def test_compare_zeroes_incorrect():
    assert compare([0,0,0],[1,2,3]) == [1,2,3]