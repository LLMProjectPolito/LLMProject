import pytest
import math


# Focus: Boundary Values
import pytest

def test_int_to_mini_roman_boundary_1():
    assert int_to_mini_roman(1) == 'i'

def test_int_to_mini_roman_boundary_1000():
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_boundary_4():
    assert int_to_mini_roman(4) == 'iv'

def test_int_to_mini_roman_boundary_9():
    assert int_to_mini_roman(9) == 'ix'

def test_int_to_mini_roman_boundary_40():
    assert int_to_mini_roman(40) == 'xl'

def test_int_to_mini_roman_boundary_90():
    assert int_to_mini_roman(90) == 'xc'

def test_int_to_mini_roman_boundary_400():
    assert int_to_mini_roman(400) == 'cd'

def test_int_to_mini_roman_boundary_900():
    assert int_to_mini_roman(900) == 'cm'

# Focus: Equivalence Partitioning
import pytest

def test_int_to_mini_roman_valid_partitions():
    """Tests with numbers representing equivalence partitions."""
    assert int_to_mini_roman(1) == 'i'  # Partition: 1
    assert int_to_mini_roman(5) == 'v'  # Partition: 5
    assert int_to_mini_roman(10) == 'x' # Partition: 10
    assert int_to_mini_roman(50) == 'l' # Partition: 50
    assert int_to_mini_roman(100) == 'c' # Partition: 100
    assert int_to_mini_roman(500) == 'd' # Partition: 500
    assert int_to_mini_roman(1000) == 'm' # Partition: 1000
    assert int_to_mini_roman(4) == 'iv' # Partition: 4
    assert int_to_mini_roman(9) == 'ix' # Partition: 9
    assert int_to_mini_roman(40) == 'xl' # Partition: 40
    assert int_to_mini_roman(90) == 'xc' # Partition: 90
    assert int_to_mini_roman(400) == 'cd' # Partition: 400
    assert int_to_mini_roman(900) == 'cm' # Partition: 900

def test_int_to_mini_roman_boundary_values():
    """Tests boundary values of the input range."""
    assert int_to_mini_roman(1) == 'i'  # Lower boundary
    assert int_to_mini_roman(1000) == 'm' # Upper boundary

def test_int_to_mini_roman_representative_values():
    """Tests representative values within partitions."""
    assert int_to_mini_roman(2) == 'ii'
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(6) == 'vi'
    assert int_to_mini_roman(7) == 'vii'
    assert int_to_mini_roman(8) == 'viii'
    assert int_to_mini_roman(11) == 'xi'
    assert int_to_mini_roman(15) == 'xv'
    assert int_to_mini_roman(16) == 'xvi'

# Focus: Logic Branches
import pytest

def test_int_to_mini_roman_single_digit():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_combinations():
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(900) == 'cm'

def test_int_to_mini_roman_complex():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(888) == 'dccclxxxviii'
    assert int_to_mini_roman(399) == 'cccxcmix'