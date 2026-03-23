import pytest
from your_module import int_to_mini_roman  # Replace your_module

class TestIntToMiniRoman:
    """
    Comprehensive pytest suite for the int_to_mini_roman function.
    """

    def test_valid_input_range(self):
        """Tests that the function handles numbers within the valid range (1-1000)."""
        with pytest.raises(ValueError):
            int_to_mini_roman(0)
        with pytest.raises(ValueError):
            int_to_mini_roman(1001)
        with pytest.raises(TypeError):
            int_to_mini_roman("10")
        with pytest.raises(TypeError):
            int_to_mini_roman(1.5)

    def test_basic_numbers(self):
        """Tests single-digit and simple numbers."""
        assert int_to_mini_roman(1) == "i"
        assert int_to_mini_roman(2) == "ii"
        assert int_to_mini_roman(3) == "iii"
        assert int_to_mini_roman(4) == "iv"
        assert int_to_mini_roman(5) == "v"
        assert int_to_mini_roman(6) == "vi"
        assert int_to_mini_roman(7) == "vii"
        assert int_to_mini_roman(8) == "viii"
        assert int_to_mini_roman(9) == "ix"
        assert int_to_mini_roman(10) == "x"

    def test_teen_numbers(self):
        """Tests numbers between 11 and 19."""
        assert int_to_mini_roman(11) == "xi"
        assert int_to_mini_roman(12) == "xii"
        assert int_to_mini_roman(13) == "xiii"
        assert int_to_mini_roman(14) == "xiv"
        assert int_to_mini_roman(15) == "xv"
        assert int_to_mini_roman(16) == "xvi"
        assert int_to_mini_roman(17) == "xvii"
        assert int_to_mini_roman(18) == "xviii"
        assert int_to_mini_roman(19) == "xix"

    def test_tens(self):
        """Tests multiples of 10."""
        assert int_to_mini_roman(20) == "xx"
        assert int_to_mini_roman(30) == "xxx"
        assert int_to_mini_roman(40) == "xl"
        assert int_to_mini_roman(50) == "l"
        assert int_to_mini_roman(60) == "lx"
        assert int_to_mini_roman(70) == "lxx"
        assert int_to_mini_roman(80) == "lxxx"
        assert int_to_mini_roman(90) == "xc"
        assert int_to_mini_roman(100) == "c"

    def test_hundreds(self):
        """Tests multiples of 100."""
        assert int_to_mini_roman(100) == "c"
        assert int_to_mini_roman(200) == "cc"
        assert int_to_mini_roman(300) == "ccc"
        assert int_to_mini_roman(400) == "cd"
        assert int_to_mini_roman(500) == "d"
        assert int_to_mini_roman(600) == "dc"
        assert int_to_mini_roman(700) == "dcc"
        assert int_to_mini_roman(800) == "dccc"
        assert int_to_mini_roman(900) == "cm"
        assert int_to_mini_roman(1000) == "m"

    def test_complex_numbers(self):
        """Tests numbers requiring combinations of roman numerals."""
        assert int_to_mini_roman(152) == "clii"
        assert int_to_mini_roman(426) == "cdxxvi"
        assert int_to_mini_roman(999) == "cmxciX"
        assert int_to_mini_roman(388) == "cccLXXXVIII"
        assert int_to_mini_roman(744) == "dCCLXXXIV"
        assert int_to_mini_roman(57) == "lvii"
        assert int_to_mini_roman(299) == "ccxcix"

    def test_edge_cases(self):
        """Tests edge cases and boundary conditions."""
        assert int_to_mini_roman(1) == "i"
        assert int_to_mini_roman(1000) == "m"
        assert int_to_mini_roman(500) == "d"
        assert int_to_mini_roman(900) == "cm"
        assert int_to_mini_roman(400) == "cd"
        assert int_to_mini_roman(4) == "iv"
        assert int_to_mini_roman(9) == "ix"