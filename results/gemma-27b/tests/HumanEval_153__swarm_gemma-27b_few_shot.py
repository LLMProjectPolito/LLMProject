import pytest

def test_strongest_extension_tie():
    assert Strongest_Extension('Class', ['aA', 'Aa']) == 'Class.aA'