def sum(a,b):
    """
    >>> sum(5,5)
    11
    """
    return  a + b


def substract(a,b):
    return  a - b


def multiplication(a,b):
    return  a * b


def division(a,b):
    if b == 0:
        raise   ValueError("La division por 0 no esta permitida")
    return  a / b

