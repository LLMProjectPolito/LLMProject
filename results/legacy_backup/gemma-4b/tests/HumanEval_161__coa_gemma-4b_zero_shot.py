import pytest
import math


# Focus: Boundary Values
import pytest

def test_empty_string():
    assert solve("") == ""

def test_no_letters():
    assert solve("1234") == "4321"

def test_mixed_case_boundary():
    assert solve("aB") == "Ab"

# Focus: Type Scenarios
import pytest

def test_no_letters():
    assert solve("1234") == "4321"

def test_lowercase_to_uppercase():
    assert solve("ab") == "AB"

def test_mixed_case_reverse():
    assert solve("#a@C") == "#A@c"

# Focus: Logic Branches
import pytest

def test_no_letters():
    assert solve("1234") == "4321"

def test_lowercase_to_uppercase():
    assert solve("ab") == "AB"

def test_mixed_case_reversal():
    assert solve("#a@C") == "#A@c"