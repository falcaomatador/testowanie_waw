import funkcje


def test_add():
    assert funkcje.add(5, 10) == 15
    assert funkcje.add(7, -1) == 6
    assert funkcje.add(4.3, 5.3) == 9.6


def test_product():
    assert funkcje.product(3, 3) == 9
    assert funkcje.product(12.5, 4) == 50
    assert funkcje.product(0, 1) == 0


def test_kwadrat():
    assert funkcje.kwadrat(3) == 9
    assert funkcje.kwadrat(4) == 16
    assert funkcje.kwadrat(1) == 1
    assert funkcje.kwadrat(0) == 0


def test_palindrom():
    assert funkcje.palindrom("ala")
    assert funkcje.palindrom("ada")

test_add()
test_product()
test_kwadrat()
test_palindrom()