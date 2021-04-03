import mymath1
import pytest

# Fixture: setup only
@pytest.fixture()
def calculator():
    calculator0 = mymath1.Calculator(8, 2)
    calculator1 = mymath1.Calculator(12, 4)
    return calculator0, calculator1


# Fixture: setup and teardown with yeld
@pytest.fixture()
def setup_teardown_fix_1():
    print("\t<-- running fixture SETUP: setup_teardown_fix")
    yield
    print("\t\t\t\t\t<-- running fixture TEARDOWN: setup_teardown_fix")

# Fixture: setup and teardown with request.addfinalizer()
@pytest.fixture()
def setup_teardown_fix_2(request):
    print("\t<-- running fixture SETUP: setup_teardown_fix")
    def tear_down_a():
        print("\t\t\t\t\t<-- running fixture TEARDOWN: setup_teardown_fix A")
    def tear_down_b():
        print("\t\t\t\t\t<-- running fixture TEARDOWN: setup_teardown_fix B")
    request.addfinalizer(tear_down_a)
    request.addfinalizer(tear_down_b)

# Fixture to be called as per its scope
# @pytest.fixture(autouse=True)               # <----- this will be run for every test which the default
@pytest.fixture(scope="module", autouse=True) # <----- this will be run for this module
def scope_fixture():
    print("\t\t<-- running fixture SCOPE: scope_fixture")

# Testing functions: add, multiply
def test_add():
    assert mymath1.add(7, 3) == 10
    assert mymath1.add(0.1, 0.2) == pytest.approx(0.3)

def test_multiply():
    assert mymath1.multiply(7, 3) == 21

# Testing methods: subtract, divide
def test_subtract(calculator):
    assert calculator[0].subtract() == 6
    assert calculator[1].subtract() == 8

def test_divide(calculator):
    assert calculator[0].divide() == 4
    assert calculator[1].divide() == 3

# Using decorators to call fixture
@pytest.mark.usefixtures("setup_teardown_fix_1")
def test_setup_teardown_1():
    print("\t\t\t\t\trunning TEST: setup_teardown_1")


@pytest.mark.usefixtures("setup_teardown_fix_2")
def test_setup_teardown_2():
    print("\t\t\t\t\trunning TEST: setup_teardown_2")


@pytest.mark.parametrize(
    'num1, num2, result',
    [
        (2, 3, 8),
        (3, 3, 27),
        (4, 5, 1024)
    ]
)
def test_square(num1, num2, result):
    assert mymath1.square(num1, num2) == result

# Disregard raised expected exception
def test_raise_exc1():
    with pytest.raises(Exception):
        mymath1.raise_exc1()

# Fail if tested function does not raises expected exception
def test_raise_exc2():
    with pytest.raises(ValueError):
       mymath1.raise_exc2()
