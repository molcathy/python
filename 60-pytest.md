# [pytest](https://docs.pytest.org/en/stable/)
* one of the most popular python testing frameworks
* must be installed as a package with pip
* when used must be imported as a module
* comes with a command line

## definitions
**framework**
: a platform/set of tools that can be used to achieve a goal

**implementation module**
: the module (or file) containing the code you want to test

**test module**:
: the module (or file) containing the testing code

**code refactoring**:
: rewriting your code in a better way, e.g. eliminating duplication

**pip**
: piton package manger

**fixtures**
: decorated function objects

**fixture: setup code**
: code to be executed before tests to preparing the environment for tests to run e.g. initializing a class and returning the object, starting a db connection and returning the db connection
: required

**fixture: teardown code**
: code to be executed after tests have run to teardown the environment built by setup fixture
: optional

## testing in general
*  necessary to make sure:
    - your code works as expected
    - changes do not break your code in a way you did not expect
* testing can be implemented either:
    - manually: tedious, prone to errors
    - automatically: by writing tests once with a framework such as pytest and run them with only one command as many time as we need
* manual testing example for a function that takes two numbers and returns their sum:
    - invoke the function providing two numbers
    - check if it returns the expected values
* an application can be tested at many levels but the most important and granular tests are **unit tests**
* unit tests are making sure the functions and class methods (I'll simply refer to them as methods henceforth) of a program return desired result
* it is implemented through test functions (henceforth I will refer to test functions simply as tests) in a test module file
* the tests test the actual code of your regular functions/methods
* the tests can be organized in test classes but we will not study this


## tdd
* one of the strategies for implementing unit testing is called TDD (Test Driven Development)
* tdd has 3 phases:
    1. red: write tests to detail what your function/method is expected to return
    2. green: write code just enough to for your test to pass
    3. refactor: refactor code and test
* the developer reiterates through those phases continuously until all the desired functionality is implemented
* we will use a variant of tdd to implement testing


## strategy
* note in this context module and files are referring to the same thing and I might use them interchangeably:
    - implementation module = implementation file
    - test module           = test file

1. write a dummy/method function want to implement (in the implementation module):
    * name
    * parameters
    * `pass` as body
2. write a test that tests your functions use cases one at a time (in the test module):
    * for specific parameters
    * specific return is expected
3. run tests => expected failure
4. update code to satisfy the test
5. refactor as necessary both the code and its test
6. repeat 2 -> 5 until test cases are exhausted

## implementation / syntax
* before using pytest you must install it with pip

* for each implementation module there should be a corresponding test module starting or ending in test e.g.:
    - implementation module: `app.py`
    - test module either: `test_app.py` or `app_test.py`

* each test module must import its implementation module e.g.:
    - for implementation module: `app.py`
    - `app_test.py` must have the following import `import app`

* each test module should import the pytest module if uses pytest specific functionality e.g. `@pytest.mark.int`

* for each function/method should be a test function starting with test e.g.:
    - func/meth: `myfunc()`
    - test function: `test_myfunc()`

* additionally a test function that tests a method must instantiate the class to which the method belongs e.g. for a class `MyClass` and a method `mymethod()` the test function:
    - should be named `test_mymethod()`
    - and should instantiate the class: `myclassinst = MyClass()`
    - then the object will be used to call the method `myclassinst.mymethod()`

* each test function will have one or more assert statements that will:
    - call the original function
    - pass parameters to implement a specific case
    - pass expected result

* assert operators:
    - comparison: `=, !=, <, >, <=, >=`
    - membership: `in, not in`
    - identity: `is, is not`

* when used with assert statements floating-point results must be passed as a parameter of `approx(my.float)`


## decorators
* special functions which modify the behaviour other functions `@mydecorator`
* they go in the top the regular functions they modify
* in pytest implement features such as:
    - `fixtures`: used setup and teardown
    - `markers`: used to run specific tests
    - `markers.parametrize`: used to pass list of tuple of parameters and results

## markers
Are used to:
* run tests matching markers e.g. `@pytest.mark.myMark`
* skip tests marked with e.g. `@pytest.mark.skip('some message')`
* skip tests marked that match a specific condition
* use multiple parameters with the same test with `@pytest.mark.parametrize()`

## fixtures: setup & teardown
**NOTE: Primarily See Examples In mymath1**
Fixtures scopes:
* function: the default scope, the fixture is destroyed at the end of the test
* class
* module
* package
* session

### setup
* fixtures are created by decorating a function with `@pytest.fixture()`
* tests use fixtures either by:
    - taking the fixture as one of the arguments: this is required if the test needs to access the return of the fixture
    - being decorated with `@pytest.mark.usefixtures("myFixture")`
* the fixtures can also set their `autouse` parameter to true => will be executed by all tests in its scope
* fixtures can use other fixtures passed as parameters

* example on how to create a setup fixture for method tests:
    1. create fixture:
        - define a function that performs the required setup e.g. instantiate one or more classes in one or more objects each and return these objects
        - decorate it with `@pytest.fixture()` decorator
    2. pass the fixture (just the function name without calling it) as a parameter to the tests that are supposed to use it
    3. in the test function you can refer to the object returned by fixture through the parameter which now accepts methods since it is an object of the class instantiated at #1
    4. if the fixture returns multiple objects you can access these objects in the tests through `param[index]` since the params are tuples - not sure if returning multiple arguments

### teardown
* optional
* if needed it cleans up after setup and tests have run
* is executed after a fixture goes out of scope
* its feature can specify its teardown code
* there are two ways for specifying teardown code:
    1. `yield` keyword
    2. request's context object's `addfinalizer` method
* yield:
    - it is like it splits the function in 2 and teardown resume with yield
    - `yield` replacement for `return` and any value that you want to be returned should be passed to it
* `addfinalizer`:
    - more capable
    - allows for multiple finalizer methods to be passed to it

### returning data
* fixtures can return data
* data can be passed by the decorated to the fixture through the params array `parmas=[value1, ...]` and then to the tests
* when a params has multiple values the test will be called for each value
* this can be used the tests with multiple values - will not study the implementation here


## passing multiple parameters
* can be achieved with `pytest.mark.parametrize`


## configuration
* pytest can be configured with `pytest.ini` e.g. registering markers


## testing exceptions
* by default tests are failing if exceptions are raised
* you can write your test to **not fail** if the tested function raised a specific excepted error
* you can also write your test to **fail** if the test does not raises an expected error


## asserting
**NOTE: Primarily See Examples In mymath2**
* assert statements are used to compare the expected results with actual results


## running tests
```sh
## NOTE: Primarily See Examples In mymath2

## install pytest
pip install pytest

## run tests
pytest                                # all tests in all the test files recursively
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

pytest -s                             # print statements from within the test

## notice marker must be registered to be used
❯ cat pytest.ini
[pytest]
markers =
    int: mark test as number
    str: mark test as number
```

## !!
* it is considered good practice to:
    - ran multiple times tests that intermittently fail - there are tools for that but not sure which
    - ran tests in random order - there are tools for that but not sure which

## ??
* positive vs negative test cases
* how to returns values with both teardown alternatives:
    - `yield`
    - `addfinalizer`
* how to make use of the default parameters value when using mark.parametrize decorators:
    - write a function that takes 2 params, where the 2nd has a default value
    - when creating a test with mark.parametrize there is no way to pass a parameter default value; not specifying the 2nd parameter instead of using param's default value errs

