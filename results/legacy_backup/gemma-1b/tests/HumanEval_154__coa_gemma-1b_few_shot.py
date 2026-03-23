import pytest
import math


# Focus: Boundary Values
def test_cycpattern_check_positive():
    assert cycpattern_check("abcd","abd") == False
    assert cycpattern_check("hello","ell") == True
    assert cycpattern_check("whassup","psus") == False
    assert cycpattern_check("abab","baa") == True
    assert cycpattern_check("efef","eeff") == False
    assert cycpattern_check("himenss","simen") == True

def test_cycpattern_check_negative():
    assert cycpattern_check("abcd","abd") == False
    assert cycpattern_check("hello","ell") == False
    assert cycpattern_check("whassup","psus") == False
    assert cycpattern_check("abab","baa") == False
    assert cycpattern_check("efef","eeff") == False
    assert cycpattern_check("himenss","simen") == False

# Focus: Type Scenarios
def test_cycpattern_check_positive():
    assert cycpattern_check("abcd","abd") == False
    assert cycpattern_check("hello","ell") == True
    assert cycpattern_check("whassup","psus") == False
    assert cycpattern_check("abab","baa") == True
    assert cycpattern_check("efef","eeff") == False
    assert cycpattern_check("himenss","simen") == True

def test_cycpattern_check_negative():
    assert cycpattern_check("abcd","abd") == False
    assert cycpattern_check("hello","ell") == False
    assert cycpattern_check("whassup","psus") == False
    assert cycpattern_check("abab","baa") == False
    assert cycpattern_check("efef","eeff") == False
    assert cycpattern_check("himenss","simen") == False

# Focus: Logic Branches
def test_cycpattern_check_positive():
    assert cycpattern_check("abcd","abd") == False
    assert cycpattern_check("hello","ell") == True
    assert cycpattern_check("whassup","psus") == False
    assert cycpattern_check("abab","baa") == True
    assert cycpattern_check("efef","eeff") == False
    assert cycpattern_check("himenss","simen") == True

def test_cycpattern_check_negative():
    assert cycpattern_check("abcd","abd") == False
    assert cycpattern_check("hello","ell") == False
    assert cycpattern_check("whassup","psus") == False
    assert cycpattern_check("abab","baa") == False
    assert cycpattern_check("efef","eeff") == False
    assert cycpattern_check("himenss","simen") == False

def test_cycpattern_check_mixed():
    assert cycpattern_check("abcd","abd") == False
    assert cycpattern_check("hello","ell") == False
    assert cycpattern_check("whassup","psus") == False
    assert cycpattern_check("abab","baa") == False
    assert cycpattern_check("efef","eeff") == False
    assert cycpattern_check("himenss","simen") == False