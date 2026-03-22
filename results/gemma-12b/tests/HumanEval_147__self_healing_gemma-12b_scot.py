import pytest
from solution import get_max_triples  # Replace your_module

class TestGetMaxTriples:

    def test_n_equals_1(self):
        assert get_max_triples(1) == 0

    def test_n_equals_2(self):
        assert get_max_triples(2) == 0

    def test_n_equals_3(self):
        assert get_max_triples(3) == 0

    def test_n_equals_4(self):
        assert get_max_triples(4) == 0

    def test_n_equals_5(self):
        assert get_max_triples(5) == 1

    def test_n_equals_6(self):
        assert get_max_triples(6) == 2

    def test_n_equals_7(self):
        assert get_max_triples(7) == 3

    def test_n_equals_8(self):
        assert get_max_triples(8) == 4

    def test_n_equals_9(self):
        assert get_max_triples(9) == 6

    def test_n_equals_10(self):
        assert get_max_triples(10) == 8

    def test_large_n(self):
        assert get_max_triples(100) == 1617

    def test_n_equals_15(self):
        assert get_max_triples(15) == 241