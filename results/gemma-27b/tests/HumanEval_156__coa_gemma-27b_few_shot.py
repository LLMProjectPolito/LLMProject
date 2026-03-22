import pytest
import math


# Focus: Boundary Values
def test_mini_roman_boundary_1():
    assert int_to_mini_roman(1) == 'i'

def test_mini_roman_boundary_1000():
    assert int_to_mini_roman(1000) == 'm'

def test_mini_roman_boundary_4():
    assert int_to_mini_roman(4) == 'iv'

def test_mini_roman_boundary_9():
    assert int_to_mini_roman(9) == 'ix'

def test_mini_roman_boundary_40():
    assert int_to_mini_roman(40) == 'xl'

def test_mini_roman_boundary_90():
    assert int_to_mini_roman(90) == 'xc'

def test_mini_roman_boundary_400():
    assert int_to_mini_roman(400) == 'cd'

def test_mini_roman_boundary_900():
    assert int_to_mini_roman(900) == 'cm'

# Focus: Equivalence Partitioning
def test_mini_roman_equivalence_partitions():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(1000) == 'm'

def test_mini_roman_boundary_values():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(1000) == 'm'

def test_mini_roman_representative_values():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(888) == 'dccclxxxviii'

# Focus: Logic Branches
def test_mini_roman_single_digit():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(10) == 'x'

def test_mini_roman_combinations():
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(900) == 'cm'

def test_mini_roman_complex():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(888) == 'dccclxxxviii'