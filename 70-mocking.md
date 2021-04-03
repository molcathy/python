# mocking

**NOTE**
This is my attempt of understanding mocking.
Was not able to find tutorials to help me understand how to use:
    - pytest
    - MagicMock
    - monkeypatch
    - fixtures

* is required for cases where your application interacts with systems outside your program aka collaborators:
    - file system
    - APIs
* mocking is needed where your code does not interact with collaborator objects i.e. objects outside your code e.g.:
    - files
    - network calls to APIs
    - subprocess calls
* is one of the doubles:
    - dummies: placeholders
    - fakes
    - stubs
    - spies
    - mocks: the most sophisticated
* frameworks:
    - `unitest.mock`

## unitest.mock
* comes by default with python
* provides classes:
    - `Mock`
    - `MagicMock`

### Mock
* `Mock` supports: fakes, stubs, spies, mokes
* `Mock` provides functions that assert if and how it was called:
    - assert_called
    - assert_called_once
    - assert_called_with
    - assert_called_once_with
    - assert_any_called
    - assert_not_called
    - assert_has_called
    - called
    - call_count
    - call_args
    - call_args_list

* you use the `Mock` class to create mock objects
* mock objects are used to "patch" collaborator objects in your code i.e. replace, imitate, mock
* way to apply mock:
    1. decorator
    2. context manager
    3. inline
* we have to mock functions where they are used not where they are defined `package.module.functionORClassName`

### MagicMock
* subclass of `Mock`
* implements many of default objects magic methods
* can simplify test setup


## monkeypatch
* test fixture provided by pytest
* unitest provides a similar decorators but which can conflict with pytest
* allows to dynamically change:
    - module attributes
    - class attributes
    - dictionary entries
    - environment variables

## example1: magic_line_reader
* tools:
    - class: `MagicMock`
    - test fixture: `MonkeyPatch`
* read and return 1st line from a file
* test cases:
    - can call readFromFile
    - readFromFile return the correct string
    - throws exception when file does not exists

## examples
* 70-mocking:
    1. fs_test1.py: using unittest & Mock
    2. fs_test2.py: using pytest & Mock
    3. fs_test3.py: using pytest & monkeypatch
    4. magic_line_reader_test.py: using MagicMock, monkeypatch, fixtures  - but I do not understand how it works