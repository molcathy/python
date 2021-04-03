# classes
* python supports OOP (**O**bject-**O**riented **P**rogramming)
* OOP is implemented through classes
* classes describe [classes of entities](https://www.google.co.uk/search?q=class+definition)
* classes are instantiated as objects which is why programing languages that support classes are called OOP languages
* classes are similar to functions but more complex:
    - functions encapsulate only behaviour: allow you to invoke the function to **do** something
    - classes encapsulate behaviour (in methods) and properties (in attributes)
* after you define a class to make use of the class you have to instantiate it:
    - instantiate it
    - and assign it to a variable
* variables to which instantiated class are assigned are considered objects
* once instantiate you can access the functionality of the class through its object e.g.:
    - ask the object to return one or more of its attributes
    - ask the object to perform one or more actions
* classes are useful for representing in code real-life entities (things, animals, plants, humans ...) by implementing their attributes (their defining properties) and methods (what they can do)
* you cave classes inside classes (inner classes)

## inheritance
* in nature a set of entities can belong to a wider set while containing narrower sets:
    - widest: animals
    - narrower: mammals
    - even narrower: dogs, cats
* the narrower set share a set of properties and behaviours with the wider set but also have properties and behaviours specific to them:
    - some animals have paws while others have hooves
    - some animals speak meow while others neigh
* we say that the narrow sets (aka children) inherit properties from the wider sets (aka parents)
* similarly with classes we have child classes that inherit from parent classes their attributes and methods
* while inheriting from parents child classes can also have some attributes and methods of their own
* you can check how classes and classes inheritance was implemented in `25-classes-example.py`

## tutorials
    - [classes intro](https://www.youtube.com/watch?v=ZDa-Z5JzLYM)
    - [classes inheritance](https://www.youtube.com/watch?v=BJ-VvGyQxho)

```python
# Defining a class
Class Employees:
    # Defining Class attributes
    def __init__(self, attr1, attr2):
        pass

    # Defining Class methods
    def method1(self):
        print("doing something 1")

    # Defining Class methods
    def method2(self):
        print("doing something 2")

class Manager(Worker):
    def __init__(self, attr1, attr2, attr3):
        super().__init__(fName, lName, salary)

    # Defining Class methods
    def method3(self):
        print("doing something 3")

# Instantiating Employees class: emp1, and emp2 are objects
emp1 = Employees(attr1, attr2)
emp2 = Employees(attr1, attr2)
man1 = Employees(attr1, attr2, attr3)

# Accessing object properties
emp1.attr1
emp2.attr1
man1.attr1

emp1.attr2
emp2.attr2
man1.attr2

man1.attr3

# Accessing object methods
emp1.method1()
emp2.method1()
man1.method1()

emp1.method2()
emp2.method2()
man1.method2()

man2.method3()
```