import pytest
import mymath

# Setup fixture
@pytest.fixture()
def calculator():
    calculator0 = mymath.Calculator(8, 2)
    calculator1 = mymath.Calculator(12, 4)
    return calculator0, calculator1

@pytest.fixture()
def myfixture1():
    print("  <-- running fixture: myfixture1")

# Testing functions: add, multiply
def test_add():
    assert mymath.add(7, 3) == 10
    assert mymath.add(0.1, 0.2) == pytest.approx(0.3)

def test_multiply():
    assert mymath.multiply(7, 3) == 21

# Testing methods: subtract, divide
def test_subtract(calculator):
    assert calculator[0].subtract() == 6
    assert calculator[1].subtract() == 8

def test_divide(calculator):
    assert calculator[0].divide() == 4
    assert calculator[1].divide() == 3

# Disregard raised expected Exception
def test_raise_exc():
    with pytest.raises(Exception):
        mymath.raise_exc()

# Using decorators to call fixture
@pytest.mark.usefixtures("myfixture1")
def test_mytest1():
    print("running test: mytest1")
