def add(a=0, b=0):
    return a + b

def subtract(a=0, b=0):
    return a - b

def multiply(a=1, b=1):
    return a * b

def divide(a=1, b=1):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b