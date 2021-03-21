# classes
* classes tutorials:
    - https://www.youtube.com/watch?v=ZDa-Z5JzLYM
    - https://www.youtube.com/watch?v=BJ-VvGyQxho
* python supports OOP (Object-oriented programming)
* OOP is implemented through classes
* classes are similar to functions but more complex:
    - functions encapsulate behavior: allow you to invoke the function to **do** something
    - classes encapsulate behavior (in methods) and properties (in attributes): allows you to call invoke (more precisely instantiate) the class to either: do something or to access one if its properties
* are useful for representing in code real life objects

## topics
* creating
* instantiating
* inheritance
* class variable
* instance variable
* static methods
* class methods

```python
# Defining a class
Class Employees:
    # Defining Class attributes
    def __init__(self, ...):
        pass

    # Defining Class methods
    def my_method_1(self):
        pass

    # Defining Class methods
    def my_method_2(self):
        pass

# Invaginating class: emp1, and emp2 are objects
emp1 = Employees(param1, ...)
emp2 = Employees(param1, ...)

# Accessing object properties
emp1.someProperty
emp2.someProperty

# Accessing object methods
emp1.someMethod()
emp2.someMethod()
```