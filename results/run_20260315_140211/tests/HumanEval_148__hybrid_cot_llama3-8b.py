import pytest
from planets import bf

PLANETS = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

def test_planet1_and_planet2_out_of_order():
    assert bf("Neptune", "Jupiter") == ("Uranus", "Saturn", "Mars", "Earth", "Venus")

def test_planet1_and_planet2_out_of_order_with_duplicates():
    assert bf("Jupiter", "Jupiter") == ()

def test_planet1_and_planet2_with_multiple_duplicates():
    assert bf("Jupiter", "Jupiter") == ()

def test_planet1_and_planet2_with_empty_string():
    assert bf("", "Jupiter") == ()
    assert bf("Jupiter", "") == ()

def test_planet1_and_planet2_with_non_string_input():
    with pytest.raises(TypeError):
        bf(123, "Jupiter")
    with pytest.raises(TypeError):
        bf("Jupiter", 123)

def test_boundary_case_1():
    assert bf("Mercury", PLANETS[-1]) == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_boundary_case_2():
    assert bf(PLANETS[0], "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_planet1_and_planet2_reverse_order():
    assert bf("Neptune", "Jupiter") == ("Uranus", "Saturn", "Mars", "Earth", "Venus")

def test_planet1_and_planet2_leading_trailing_whitespace():
    assert bf("  Jupiter  ", " Neptun e  ") == ("Saturn", "Uranus")

def test_planet1_and_planet2_sort_order():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")