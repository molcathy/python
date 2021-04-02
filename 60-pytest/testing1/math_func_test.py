#!/usr/bin/env python
import math_func
import pytest
import sys

@pytest.mark.int
def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7
    print("hi from test_add")

@pytest.mark.int
# @pytest.mark.skip('skiping this test')
# @pytest.mark.skipif(sys.version_info > (3, 8), reason='skiping test due to python version')
def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10
    assert math_func.product(7) == 14

@pytest.mark.str
def test_add_strings():
    result = math_func.add('Hello', ' World')  # the result of invoked func can bee assigned to a var
    assert result == 'Hello World'             # then the var can be asserted
    assert type(result) is str
    assert 'HelloWorld' not in result
    assert 'o W' in result

@pytest.mark.str
def test_product_strings():
    math_func.product('Hello ', 3) == 'Hello Hello Hello'
    result = math_func.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result

@pytest.mark.parametrize(
    'arg1, arg2, result',
    [
        (7, 3, 4),
        (5, 4, 1),
        (6.5, 2.5, 4)
    ]
)
def test_subtract(arg1, arg2, result):
    assert math_func.subtract(arg1, arg2) == result