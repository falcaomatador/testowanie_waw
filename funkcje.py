import math

def add(a, b):
    return a + b


def product(x, y):
    return x * y


def kwadrat(x):
    return x ** 2

def palindrom(napis):
    napis = "".join(napis.lower().split())
    return napis == napis[::-1]


def circle_area(r):
    if r<0:
        raise ValueError("The radius cannot be negative")
    if type(r) not in [int, float]:
        raise TypeError("The radius has to be a non-negative real number")

    return math.pi * r ** 2