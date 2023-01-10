import doctest
import random
import math

def pi_mc(num_darts: int) -> float:
    """Estimates pi using the Monte Carlo simulation
    >>> round(pi_mc(500_000),2)
    3.14
    >>> round(pi_mc(432_423),2)
    3.14

    :param num_darts: integer
    :return:an estimation of pi that is float
    """
    in_circle = 0

    for dart in range(num_darts):
        x = random.random()
        y = random.random()

        if math.sqrt(x**2 + y**2) < 1.0:
            in_circle += 1

    pi = in_circle / num_darts * 4
    return pi

doctest.testmod()
