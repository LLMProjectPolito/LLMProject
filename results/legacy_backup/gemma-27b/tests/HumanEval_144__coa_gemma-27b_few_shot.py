import pytest
import math


# Focus: Boundary Values
def test_simplify_boundary_whole_numbers():
    assert simplify("1/1", "1/1") == True
    assert simplify("2/1", "3/1") == True
    assert simplify("1/1", "2/1") == True

def test_simplify_boundary_zero_numerator():
    assert simplify("0/1", "1/1") == True
    assert simplify("1/1", "0/1") == True
    assert simplify("0/5", "5/1") == True

def test_simplify_boundary_large_numbers():
    assert simplify("1000/1", "1/1000") == True
    assert simplify("1000/2", "1/500") == True
    assert simplify("999/1", "1/999") == True

# Focus: Equivalence Partitioning
def test_simplify_whole_times_whole():
    assert simplify("1/1", "1/1") == True
    assert simplify("2/1", "3/1") == True

def test_simplify_whole_times_fraction():
    assert simplify("1/1", "2/3") == False
    assert simplify("2/1", "3/1") == True
    assert simplify("1/2", "4/1") == True

def test_simplify_fraction_times_fraction():
    assert simplify("1/2", "2/1") == True
    assert simplify("1/3", "3/1") == True
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("2/3", "3/2") == True
    assert simplify("4/5", "5/4") == True
    assert simplify("1/4", "4/1") == True

# Focus: Error Handling (Invalid Input Format)
def test_simplify_invalid_x_format():
    assert simplify("1/5a", "5/1") is False

def test_simplify_invalid_n_format():
    assert simplify("1/5", "5/1b") is False

def test_simplify_invalid_x_and_n_format():
    assert simplify("1/5a", "5/1b") is False