import pytest
from scientific_calculator.scientific_calculator import sine, cosine, tangent, logarithm, exponential

def test_sine():
    assert pytest.approx(sine(90), 0.001) == 1.0
    assert pytest.approx(sine(0), 0.001) == 0.0

def test_cosine():
    assert pytest.approx(cosine(0), 0.001) == 1.0
    assert pytest.approx(cosine(90), 0.001) == 0.0

def test_tangent():
    assert pytest.approx(tangent(45), 0.001) == 1.0
    assert tangent(90) > 1e10  # As tangent is undefined at 90 degrees, it should be a very large number

def test_logarithm():
    assert pytest.approx(logarithm(100, 10), 0.001) == 2.0
    assert pytest.approx(logarithm(8, 2), 0.001) == 3.0

def test_exponential():
    assert pytest.approx(exponential(1), 0.001) == pytest.approx(2.718, 0.001)
    assert pytest.approx(exponential(0), 0.001) == 1.0

def test_logarithm_base_change():
    assert pytest.approx(logarithm(100), 0.001) == 2.0
    assert pytest.approx(logarithm(1000, 10), 0.001) == 3.0