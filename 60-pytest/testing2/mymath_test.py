import pytest
import mymath


@pytest.fixture()
def calculator():
    calculator0 = mymath.Calculator(8, 2)
    calculator1 = mymath.Calculator(12, 4)
    return calculator0, calculator1

def test_add():
    assert mymath.add(7, 3) == 10
    assert mymath.add(0.1, 0.2) == pytest.approx(0.3)

def test_multiply():
    assert mymath.multiply(7, 3) == 21

def test_subtract(calculator):
    assert calculator[0].subtract() == 6
    assert calculator[1].subtract() == 8

def test_divide(calculator):
    assert calculator[0].divide() == 4
    assert calculator[1].divide() == 3