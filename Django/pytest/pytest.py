def add(x, y=2):
    return x + y

def prod(x, y=2):
    return x * y


def add_test():
    assert add(2,5) == 7
    assert add(2) == 5