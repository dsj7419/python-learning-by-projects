def add(a, b):
    """
    Return the sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Return the difference between a and b.
    """
    return a - b

def multiply(a, b):
    """
    Return the product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Return the division of a by b. If b is 0, return a message indicating division by zero is undefined.
    """
    if b == 0:
        return "Undefined (division by zero)"
    return a / b
