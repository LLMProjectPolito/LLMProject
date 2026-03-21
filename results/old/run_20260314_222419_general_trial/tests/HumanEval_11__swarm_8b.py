import pytest
import math

def test_string_xor_edge_cases():
    """ Test string_xor function with edge case inputs.
    
    This test case checks if the function behaves correctly when one or both of the input strings are empty,
    or when the input strings contain leading zeroes.
    """
    assert string_xor('', '110') == '110'
    assert string_xor('', '') == ''
    assert string_xor('0000', '1100') == '1100'