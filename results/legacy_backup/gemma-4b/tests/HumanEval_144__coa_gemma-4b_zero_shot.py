import pytest
import math


# Focus: Boundary Values
import pytest

def test_simplify_positive_whole_numbers():
    assert simplify("1/5", "5/1") == True
    assert simplify("2/3", "3/2") == True
    assert simplify("10/2", "2/1") == True

def test_simplify_non_whole_numbers():
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("3/4", "5/1") == False

def test_simplify_large_numbers():
    assert simplify("100/10", "10/1") == True
    assert simplify("123/4", "4/1") == False

# Focus: Type Scenarios
import pytest

def test_simplify_whole_number():
    assert simplify("1/5", "5/1") == True

def test_simplify_not_whole_number():
    assert simplify("1/6", "2/1") == False

def test_simplify_not_whole_number_2():
    assert simplify("7/10", "10/2") == False

# Focus: Logic Branches
import pytest

def test_simplify_whole_number():
    assert simplify("1/5", "5/1") == True

def test_simplify_not_whole_number():
    assert simplify("1/6", "2/1") == False

def test_simplify_not_whole_number_2():
    assert simplify("7/10", "10/2") == False