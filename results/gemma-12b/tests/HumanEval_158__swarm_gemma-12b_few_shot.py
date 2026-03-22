import pytest
import math

def test_find_max_mixed_case():
    assert find_max(["Name", "name", "STRING"]) == "STRING"