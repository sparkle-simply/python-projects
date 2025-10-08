import pytest
from roman_calculator.roman_calculator import int_to_roman_conversion

def test_single_digit():
    assert int_to_roman_conversion(1) == 'I'
    assert int_to_roman_conversion(5) == 'V'

def test_double_digits():
    assert int_to_roman_conversion(10) == 'X'
    assert int_to_roman_conversion(44) == 'XLIV'

def test_triple_digits():
    assert int_to_roman_conversion(100) == 'C'
    assert int_to_roman_conversion(399) == 'CCCXCIX'

def test_thousands():
    assert int_to_roman_conversion(1000) == 'M'
    assert int_to_roman_conversion(3999) == 'MMMCMXCIX'

def test_invalid_input_zero():
    with pytest.raises(ValueError):
        int_to_roman_conversion(0)

def test_invalid_input_negative():
    with pytest.raises(ValueError):
        int_to_roman_conversion(-1)

def test_invalid_input_above_limit():
    with pytest.raises(ValueError):
        int_to_roman_conversion(4000)