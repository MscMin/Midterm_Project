def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide (x,y):
    if y==0:
        Error_str = "Divide By Zero!"
        return Error_str
    return x/y