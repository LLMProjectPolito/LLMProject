import pytest
import math


# Focus: Boundary Values
def test_empty_string_boundary():
    assert string_to_md5("") is None

def test_single_character_boundary():
    assert string_to_md5("a") == "0cc175b9c0f1b6a831c399e269772661"

def test_short_string_boundary():
    assert string_to_md5("ab") == "2bac8ff347732135f24a73c691c6739a"

# Focus: Error Handling
def test_string_to_md5_empty_string():
    assert string_to_md5("") is None

def test_string_to_md5_none_input():
    assert string_to_md5(None) is None

def test_string_to_md5_invalid_input_type():
    assert string_to_md5(123) is None

# Focus: Logic Branches
def test_empty_string():
    assert string_to_md5("") is None

def test_non_empty_string():
    assert string_to_md5("test") != None

def test_different_string():
    assert string_to_md5("another test") != None