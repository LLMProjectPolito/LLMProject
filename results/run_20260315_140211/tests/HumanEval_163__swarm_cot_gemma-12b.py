import pytest
import math

def test_generate_integers_identical_negative_input():
    """Test with identical negative inputs."""
    assert generate_integers(-2, -2) == []