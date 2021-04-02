#!/usr/bin/env python
import mymath2
import pytest
import sys

@pytest.mark.int
def test_add():
    assert mymath2.add(7, 3) == 10
    assert mymath2.add(7) == 9
    assert mymath2.add(5) == 7
    print("hi from test_add")

@pytest.mark.int
# @pytest.mark.skip('skiping this test')
# @pytest.mark.skipif(sys.version_info > (3, 8), reason='skiping test due to python version')
def test_product():
    assert mymath2.product(5, 5) == 25
    assert mymath2.product(5) == 10
    assert mymath2.product(7) == 14

@pytest.mark.str
def test_add_strings():
    result = mymath2.add('Hello', ' World')    # the result of invoked func can bee assigned to a var
    assert result == 'Hello World'             # then the var can be asserted
    assert type(result) is str
    assert 'HelloWorld' not in result
    assert 'o W' in result

@pytest.mark.str
def test_product_strings():
    mymath2.product('Hello ', 3) == 'Hello Hello Hello'
    result = mymath2.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result
