def add(a, b):
    return a + b


def product(x, y):
    return x * y


def kwadrat(x):
    return x ** 2

def palindrom(napis):
    napis = "".join(napis.lower().split())
    return napis == napis[::-1]