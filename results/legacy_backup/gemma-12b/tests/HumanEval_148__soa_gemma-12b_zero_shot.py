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
    assert bf("Earth", "Jupiter") == ("Mars", "Jupiter", "Saturn")
    assert bf("Mercury", "Mars") == ("Venus", "Earth")

def test_bf_invalid_planet_names():
    assert bf("Pluto", "Neptune") == ()
    assert bf("Jupiter", "Xenon") == ()
    assert bf("Invalid", "Earth") == ()
    assert bf("Earth", "Invalid") == ()
    assert bf("Invalid1", "Invalid2") == ()

def test_bf_same_planet():
    assert bf("Earth", "Earth") == ()
    assert bf("Mercury", "Mercury") == ()
    assert bf("Neptune", "Neptune") == ()

def test_bf_planet1_after_planet2():
    assert bf("Neptune", "Mercury") == ()
    assert bf("Uranus", "Venus") == ()
    assert bf("Saturn", "Earth") == ()

def test_bf_empty_tuple_edge_cases():
    assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert bf("Venus", "Jupiter") == ("Earth", "Mars", "Saturn")
    assert bf("Earth", "Saturn") == ("Mars", "Jupiter")
    assert bf("Mars", "Uranus") == ("Jupiter", "Saturn")
    assert bf("Jupiter", "Uranus") == ("Saturn")
    assert bf("Saturn", "Neptune") == ("Uranus")

def test_bf_planet_names_case_sensitive():
    assert bf("mercury", "Neptune") == ()
    assert bf("Jupiter", "neptune") == ()
    assert bf("EARTH", "mars") == ()

def test_bf_planet_names_with_spaces():
    assert bf(" Earth", "Neptune") == ()
    assert bf("Jupiter", " Neptune") == ()
    assert bf("Earth ", "Mars") == ()