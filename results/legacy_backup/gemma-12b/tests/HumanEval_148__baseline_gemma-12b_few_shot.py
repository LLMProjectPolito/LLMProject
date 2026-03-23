def test_bf_jupiter_neptune():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

def test_bf_earth_mercury():
    assert bf("Earth", "Mercury") == ("Venus",)

def test_bf_mercury_uranus():
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

def test_bf_neptune_mercury():
    assert bf("Neptune", "Mercury") == ("Uranus", "Saturn", "Jupiter", "Mars", "Earth", "Venus")

def test_bf_mercury_mercury():
    assert bf("Mercury", "Mercury") == ()

def test_bf_invalid_planet1():
    assert bf("Pluto", "Neptune") == ()

def test_bf_invalid_planet2():
    assert bf("Mercury", "Pluto") == ()

def test_bf_invalid_both():
    assert bf("Pluto", "Pluto") == ()

def test_bf_earth_earth():
    assert bf("Earth", "Earth") == ()

def test_bf_venus_mars():
    assert bf("Venus", "Mars") == ("Earth",)

def test_bf_mars_venus():
    assert bf("Mars", "Venus") == ()