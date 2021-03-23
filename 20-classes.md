# classes
* python supports OOP (**O**bject-**O**riented **P**rogramming)
* OOP is implemented through classes
* classes describe [classes of entities](https://www.google.co.uk/search?q=class+definition)
* classes are instantiated as objects which is why languages that support classes are called OOP
* classes are similar to functions but more complex:
    - functions encapsulate only behaviour: allow you to invoke the function to **do** something
    - classes encapsulate behaviour (in methods) and properties (in attributes)
* after you define a class to make use of the class you have to instantiate it:
    - call it
    - and assign it to a variable
* variables to which instantiated class are assigned are considered object
* once instantiate you can access the functionality of the class through its object e.g.:
    - ask the object to return one ore more of its properties
    - ask the object to perform one ore more actions
* classes are useful for representing in code real-life entities (things, animals, plants, humans ...) by implementing their attributes (their defining properties) and methods (what they can do)

## inheritance
* in nature a set of entities can be considered as belonging to wider e.g.:
    - widest set: animals
    - narrower then animals but wider set a more specific set: mammals
    - narrower set: dogs, cats
* the narrower set share a set of properties and behaviours with the wider set they belong too but implement those in a particular way e.g.:
    - some animals have paws while others have hooves
    - some animals bite other animals bite
* we say that the narrow sets inherit properties from the wider sets
* similarly classes we  have child classes inherit from parent classes their attributes and methods
* while inheriting attributes and methods from parents child classes can have some attributes and methods of their own
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