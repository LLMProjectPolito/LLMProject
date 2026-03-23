import pytest
from your_module import bf  # Replace your_module

planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

def test_bf_valid_range():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus",)
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Mars", "Saturn") == ("Jupiter",)
    assert bf("Venus", "Earth") == ("Mercury",)
    assert bf("Neptune", "Uranus") == ()
    assert bf("Saturn", "Jupiter") == ("Uranus", "Neptune")
    assert bf("Earth", "Earth") == ()

def test_bf_invalid_planet_names():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Jupiter", "Xenon") == ()
    assert bf("Invalid", "Valid") == ()
    assert bf("Valid", "Invalid") == ()
    assert bf("Invalid1", "Invalid2") == ()
    assert bf("Mercury", "Mercury") == ()

def test_bf_case_sensitivity():
    assert bf("mercury", "Neptune") == ()
    assert bf("Jupiter", "neptune") == ()
    assert bf("jUpItEr", "uRaNuS") == ()

def test_bf_empty_input():
    assert bf("", "") == ()

def test_bf_planet_order():
    assert bf("Venus", "Mars") == ("Earth",)
    assert bf("Mars", "Venus") == ()

def test_bf_edge_cases():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Neptune", "Mercury") == ()
    assert bf("Uranus", "Saturn") == ("Neptune",)
    assert bf("Saturn", "Uranus") == ()

def test_bf_with_duplicate_planets():
    assert bf("Earth", "Earth") == ()

def test_bf_planets_at_extremes():
    assert bf("Mercury", "Venus") == ()
    assert bf("Uranus", "Neptune") == ()

def test_bf_valid_range_reverse():
    assert bf("Neptune", "Jupiter") == ("Uranus", "Saturn")

def test_bf_valid_range_mercury_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_valid_range_mercury_mercury():
    assert bf("Mercury", "Mercury") == ()

def test_bf_valid_range_neptune_neptune():
    assert bf("Neptune", "Neptune") == ()

def test_bf_invalid_planet1():
    assert bf("Pluto", "Neptune") == ()

def test_bf_invalid_planet2():
    assert bf("Jupiter", "Pluto") == ()

def test_bf_invalid_planets():
    assert bf("Pluto", "Eris") == ()

def test_bf_planet1_before_planet2():
    assert bf("Venus", "Earth") == ("Mercury",)

def test_bf_planet1_equal_planet2():
    assert bf("Earth", "Earth") == ()

def test_bf_planet1_last_planet2_first():
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")

def test_bf_planet1_first_planet2_last():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

def test_bf_empty_string_planet1():
    assert bf("", "Neptune") == ()

def test_bf_empty_string_planet2():
    assert bf("Mercury", "") == ()

def test_bf_both_empty_strings():
    assert bf("", "") == ()

def test_bf_case_insensitive():
    assert bf("earth", "NEPTUNE") == ("venus", "mars", "jupiter", "saturn", "uranus")

def test_bf_planet1_and_planet2_same_case():
    assert bf("mercury", "venus") == ("earth", "mars", "jupiter", "saturn", "uranus", "neptune")