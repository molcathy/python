# [pytest](https://docs.pytest.org/en/stable/)
* terminology:
    - framework: a platform/set of tools which can be used to achieve a goal, a
* one of the most popular python testing frameworks
* must be installed as a package with pip
* when used must be imported as a module
* comes with a command line

## testing
*  necessary to make sure:
    - your code works as expected
    - changes do not brake your code in a way you did not expect
* testing can be implemented either:
    - manually: tedious, prone to errors
    - automatically: by writing tests once with framework such as pytest and run them with only one command as many time as we need
* manual testing example for a function that takes two numbers and returns their sum:
    - invoke the function providing two numbers
    - check if it returns the expected values
* an application can be tested at many levels but the most important and granular tests are **unit tests**
* unit tests are making sure the functions and class methods (I'll simple refer them as methods henceforth) of a program behave as expected
* it is implemented through test functions in a test module file
* the test functions test the actual code of your regular functions/methods
* the test functions can bee organized in test classes but we will not study this
* henceforth I will refer to test functions simply as tests

## tdd
* one of the strategies for implementing unit testing is called TDD (Test Driven Development)
* tdd has 3 phases:
    1. red: write tests to detail what your function/method is supposed to accomplish
    2. green: write code just enough to pass your test
    3. refactor: refactor code and test
* the developer reiterates through those phases continuously until all the desired functionality is implemented
* we will use a variant of tdd to implement testing

## strategy
* vocabulary / terminology:
    -  implementation module: the module (or file) containing the code you want to test
    -  test module: the module (or file) containing the testing code
    -  code refactoring: rewriting your code in a better way, e.g. eliminating duplication
* note in this context module and files are referring to the same thing and I might use them interchangeably:
    - implementation module = implementation file
    - test module           = test file
* based on the red - green - refactor TDD

1. write a dummy / method function want to implement (implementation module):
    * name
    * parameters
    * pass as body
2. write a test that tests your functions use cases one at the time where (test module):
    * for specific parameters
    * specific return is expected
3. run tests => expected failure
4. update code to satisfy test (implementation module)
5. refactor as necessary:
    * code (implementation module)
    * tests (test module)
6. repeat 2 -> 5 until test cases are exhausted

## implementation / syntax
* vocabulary / terminology:
    - pip: piton package manger

* before using pytest you must install it with pip

* for each implementation module there should be a corresponding test module starting or ending in test e.g.:
    - implementation module: `app.py`
    - test module either: `test_app.py` or `app_test.py`

* each test module must import its implementation module e.g.:
    - for implementation module: `app.py`
    - `app_test.py` must have the following import `import app`

* each test module should import the pytest module; to make it easier we will always import it

* for each function/method should be a test function starting with test e.g.:
    - func/meth: `myfunc()`
    - test function: `test_myfunc()`

* additionally a test function that tests a method must instantiate the class to which the method belongs e.g. for a class `MyClass` and a method `mymethod()` the test function:
    - should be named `test_mymethod()`
    - and should instantiate the class: `myclassinst = MyClass()`
    - then the object will be used to call the method `myclassinst.mymethod()`

* each test function will have one ore more assert statements that will:
    - call original function
    - pass parameters to implement a specific case
    - pass expected result

* assert operators:
    - comparison: `=, !=, <, >, <=, >=`
    - membership: `in, not in`
    - identity: `is, is not`

* you can use decorators/markers to:
    - run tests matching markers e.g. `@pytest.mark.myMark`
    - skip tests marked with e.g. `@pytest.mark.skip('some message')`
    - skip tests marked that match condition
    - use multiple type of parameters with same test function with `@pytest.mark.parametrize()`

## running tests
```sh
## install pytest
pip install pytest

## run tests
pytest                                # all tests in all the test files
                                      # passed tests are denoted by green dots at the right of the test file
                                      # failed tests are denoted by red 'F' at the right of the test file
pytest -v                             # all tests in all the test files in verbose mode
pytest -q                             # all tests in all the test files in quiet mode

pytest test_math_func.py              # all tests in a specific test file


pytest test_math_func.py::test_add    # specific test from a specific test file

pytest -k 'add'                       # all tests that match keyword
pytest -k 'add or string'             # all tests that match keyword or keyword
pytest -k 'add and string'            # all tests that match keyword and keyword

pytest -m 'int'                       # run all tests that match marker; implemented through fixtures
pytest -m 'str'                       # run all tests that match marker; implemented through fixtures

pytest -x                             # exit testing after 1st test failure
pytest --maxfail=2                    # stop after a maximum of 2 failures

pytest --tb=no                        # do not print stacktrace

pytest -s                             # print print statements from within the test
```

## notice marker must be registered in order to be used
❯ cat pytest.ini
[pytest]
markers =
    int: mark test as number
    str: mark test as number

## decorators
* are special functions who modify the behavior other functions `@mydecorator`; they go in the top the regular functions they modify
* in pytest implement features such as:
    - fixtures: used setup and teardown
    - markers: used to run specific tests
    - markers.parametrize: used to pass list of tuple of parameters and results


## setup & teardown fixtures
**fixtures**
: decorated function objects

**setup fixture**
: code to be executed before tests to preparing the environment for tests to run e.g. initializing a class and returning the object, starting a db connections and returning the db connection

**teardown fixture**
: code to be executed after tests have run to teardown the environment built by setup fixture

* setup & teardown fixtures can be invoked at different levels:
    - session
    - module
    - class
    - test (i.e. test function)

* example on how to create a fixtures for method tests:
    1. create fixture:
        - define a function that performs the required setup e.g.instantiate one or more classes in one or more objects each and return these objects
        - decorate it with `@pytest.fixture()` decorator
    2. pass the fixture (just the function name without calling it) as a parameter to the tests that are supposed to use it
    3. in the test function you can refer to the object returned by fixture through

## !!
* importing pytest in the test module only need pytest imported in the test module if you use pytest functionality e.g. fixtures,  markers `@pytest.mark.int`

## ??
* positive vs negative test cases
* how to make use of the default parameters value when using mark.parametrize decorators:
    - write a function that takes 2 params, where the 2nd has a default value
    - when creating a test with mark.parametrize there is no way to pass a parameter default value; not specifying the 2nd parameter instead of using param's default value errs

