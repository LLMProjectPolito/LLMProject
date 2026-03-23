import pytest
import math

def do_algebra(a, b):
    assert math.isclose(a + b, b*b)
    assert math.isclose(a - b, b*b)
    assert math.isclose(a * b, b*b)
    assert math.isclose(a // b, b)
    assert math.isclose(a % b, b)
    assert math.isclose(a ** b, b * b)

def test_algebra():
    assert do_algebra('+', '2') == 2
    assert do_algebra('-', '3') == 3
    assert do_algebra('*', '4') == 4
    assert do_algebra('/', '5') == 5
    assert do_algebra('//', '10') == 10
    assert do_algebra('**', '2') == 2

def test_algebra():
    assert do_algebra('+', '2') == 9
    assert do_algebra('-', '3') == 9
    assert do_algebra('*', '4') == 16
    assert do_algebra('/', '5') == 5
    assert do_algebra('//', '2') == 1
    assert do_algebra('**', '3') == 27

def test_algebra():
    assert do_algebra('+', '2') == 9
    assert do_algebra('-', '3') == 9
    assert do_algebra('*', '4') == 16
    assert do_algebra('/', '5') == 5
    assert do_algebra('//', '2') == 1
    assert do_algebra('**', '3') == 27