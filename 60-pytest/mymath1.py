def add(num1, num2):
    return num1 + num2

def multiply(num1, num2):
    return num1 * num2

def square(num1, num2):
    return num1 ** num2


class Calculator:
    '''Performs simple operations'''
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def subtract(self):
        return self.num1 - self.num2

    def divide(self):
        return self.num1 / self.num2

# Functions will raise exceptions
def raise_exc1():
    raise(Exception)

def raise_exc2():
    raise(ValueError)
