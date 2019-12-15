import math

# def circle_area(r):
#
#     if type(r) not in [int, float]:
#         return "Podałeś nieprawidłowy typ. Podaj liczbę"
#     elif r<0:
#         return "Koło o takim promieniu nie istnieje"
#
#     else:
#         return math.pi * r ** 2


def circle_area(r):
    if r < 0:
        raise Exception("promien nie moze byc ujemny")
    try:
        return math.pi * r ** 2
    except:
        return "cos poszlo nie tak"


print(circle_area(1))
print(circle_area(0))
print(circle_area(-1))
print(circle_area(2+5j))
print(circle_area(True))
print(circle_area("asd"))